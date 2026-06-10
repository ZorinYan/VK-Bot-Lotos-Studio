import json
from pathlib import Path

STORAGE_PATH = Path(__file__).resolve().parent.parent / "data" / "reminders.json"


def _load() -> dict:
    if not STORAGE_PATH.exists():
        return {}
    with open(STORAGE_PATH, encoding="utf-8") as file:
        return json.load(file)


def _save(data: dict) -> None:
    STORAGE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STORAGE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def was_sent(record_id: int) -> bool:
    return str(record_id) in _load()


def mark_sent(record_id: int) -> None:
    data = _load()
    data[str(record_id)] = True
    _save(data)


def clear_record(record_id: int) -> None:
    data = _load()
    if data.pop(str(record_id), None) is not None:
        _save(data)
