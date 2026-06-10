from utils.dates import format_datetime_short
from utils.text_style import LIGHT, join_blocks, marker, page_header
from yclients.client import YClientsClient


def _service_titles(record: dict) -> str:
    services = record.get("services", [])
    if not services:
        return "Занятие"
    return ", ".join(item.get("title", "Услуга") for item in services)


def _staff_name(record: dict) -> str:
    staff = record.get("staff", {})
    return staff.get("name") or staff.get("specialization") or "—"


def record_button_label(record: dict) -> str:
    when = format_datetime_short(record.get("datetime") or record.get("date", ""))
    service = _service_titles(record)
    label = f"{when} · {service}"
    return label[:40]


def format_next_record(record: dict) -> str:
    card = format_record_card(record)
    return (
        f"{page_header('📅', 'Ваша ближайшая запись')}\n\n"
        f"{card}\n\n"
        "Не сможете прийти — «Отменить запись» в меню."
    )


def format_record_card(record: dict) -> str:
    when = format_datetime_short(record.get("datetime") or record.get("date", ""))
    service = _service_titles(record)
    trainer = _staff_name(record)
    return (
        f"{LIGHT}\n"
        f"📌  {service}\n"
        f"🗓  {when}\n"
        f"👤  {trainer}\n"
        f"{LIGHT}"
    )


def format_upcoming_for_cancel(records: list[dict]) -> str:
    if not records:
        return (
            f"{page_header('🗑', 'Отмена записи')}\n\n"
            "У вас нет предстоящих занятий для отмены."
        )

    blocks = []
    for index, record in enumerate(records, 1):
        when = format_datetime_short(record.get("datetime") or record.get("date", ""))
        service = _service_titles(record)
        trainer = _staff_name(record)
        blocks.append(
            "\n".join([
                f"{marker(index)}  {when}",
                f"    {service}",
                f"    👤  {trainer}",
            ])
        )

    return (
        f"{page_header('🗑', 'Отмена записи')}\n\n"
        "Выберите запись для отмены:\n\n"
        + join_blocks(blocks)
    )


def format_reminder(record: dict, studio_name: str, minutes_before: int) -> str:
    when = format_datetime_short(record.get("datetime") or record.get("date", ""))
    service = _service_titles(record)
    trainer = _staff_name(record)
    return (
        f"⏰  Напоминание · {studio_name}\n"
        f"{LIGHT}\n\n"
        f"Через {minutes_before} мин у вас занятие:\n\n"
        f"📌  {service}\n"
        f"🗓  {when}\n"
        f"👤  {trainer}\n\n"
        f"Не сможете прийти — нажмите «Отменить запись» в меню."
    )


def format_cancel_success(record: dict) -> str:
    return (
        f"{page_header('✅', 'Запись отменена')}\n\n"
        f"{format_record_card(record)}\n\n"
        "Ждём вас на других занятиях 🪷"
    )
