import logging
import threading
from datetime import datetime

from bot.messenger import Messenger
from config import Config
from utils import reminders_storage
from utils import storage
from bot.keyboards import main_menu
from yclients import YClientsClient
from yclients.client import YClientsClient as YC
from yclients.formatters_records import format_reminder

logger = logging.getLogger(__name__)


class ReminderService:
    def __init__(
        self,
        yclients: YClientsClient,
        messenger: Messenger,
        config: Config,
    ) -> None:
        self.yclients = yclients
        self.messenger = messenger
        self.config = config
        self._stop = threading.Event()

    def start(self) -> None:
        thread = threading.Thread(target=self._loop, name="reminders", daemon=True)
        thread.start()
        logger.info(
            "Напоминания запущены: за %s мин, проверка каждые %s сек",
            self.config.reminder_minutes_before,
            self.config.reminder_check_interval_sec,
        )

    def stop(self) -> None:
        self._stop.set()

    def _loop(self) -> None:
        # Даём основному циклу бота запуститься до первой проверки API.
        self._stop.wait(30)
        while not self._stop.is_set():
            try:
                self.check_all()
            except Exception:
                logger.exception("Ошибка в цикле напоминаний")
            self._stop.wait(self.config.reminder_check_interval_sec)

    def check_all(self) -> None:
        users = storage.get_all_users()
        if not users:
            return

        for vk_user_id, phone in users.items():
            try:
                self._check_user(vk_user_id, phone)
            except Exception:
                logger.exception("Напоминание: ошибка для VK user %s", vk_user_id)

    def _check_user(self, vk_user_id: int, phone: str) -> None:
        profile = self.yclients.find_client_by_phone(phone)
        if not profile:
            return

        records = self.yclients.get_upcoming_records(profile["id"], limit=20)
        target_minutes = self.config.reminder_minutes_before
        half_window = max(self.config.reminder_check_interval_sec / 60 / 2, 3)
        now = datetime.now()

        for record in records:
            record_id = record.get("id")
            if not record_id or reminders_storage.was_sent(record_id):
                continue

            dt = YC._parse_record_datetime(record)
            if not dt:
                continue

            minutes_until = (dt - now).total_seconds() / 60
            if minutes_until <= 0:
                continue

            if abs(minutes_until - target_minutes) > half_window:
                continue

            text = format_reminder(record, self.config.studio_name, target_minutes)
            try:
                self.messenger.send_message(vk_user_id, text, main_menu(vk_user_id))
                reminders_storage.mark_sent(record_id)
                logger.info("Напоминание отправлено: user=%s record=%s", vk_user_id, record_id)
            except Exception:
                logger.exception(
                    "Не удалось отправить напоминание user=%s record=%s",
                    vk_user_id,
                    record_id,
                )
