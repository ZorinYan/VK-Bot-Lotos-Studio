import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    vk_token: str
    yclients_partner_token: str
    yclients_user_token: str
    yclients_company_id: int
    studio_name: str
    reminder_minutes_before: int
    reminder_check_interval_sec: int
    yclients_booking_url: str


def load_config() -> Config:
    vk_token = os.getenv("VK_GROUP_TOKEN", "")
    partner_token = os.getenv("YCLIENTS_PARTNER_TOKEN", "")
    user_token = os.getenv("YCLIENTS_USER_TOKEN", "")

    missing = []
    if not vk_token:
        missing.append("VK_GROUP_TOKEN")
    if not partner_token:
        missing.append("YCLIENTS_PARTNER_TOKEN")
    if not user_token:
        missing.append("YCLIENTS_USER_TOKEN")

    if missing:
        raise RuntimeError(
            "Заполните переменные в .env: " + ", ".join(missing)
        )

    return Config(
        vk_token=vk_token,
        yclients_partner_token=partner_token,
        yclients_user_token=user_token,
        yclients_company_id=int(os.getenv("YCLIENTS_COMPANY_ID", "0")),
        studio_name=os.getenv("STUDIO_NAME", "Лотос"),
        reminder_minutes_before=int(os.getenv("REMINDER_MINUTES_BEFORE", "60")),
        reminder_check_interval_sec=int(os.getenv("REMINDER_CHECK_INTERVAL_SEC", "120")),
        yclients_booking_url=os.getenv(
            "YCLIENTS_BOOKING_URL", "https://n1996926.yclients.com/"
        ),
    )
