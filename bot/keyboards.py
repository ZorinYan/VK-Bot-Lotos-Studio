from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from utils import storage
from utils import user_prefs

BTN_LOGIN = "Войти"
BTN_LOGOUT = "Выйти"
BTN_CONTACT_ADMIN = "Написать администратору"
BTN_BOT_MENU = "Меню бота"
BTN_BOOK = "Записаться"
BTN_BOOK_AGAIN = "Записаться снова"
BTN_SCHEDULE_MY_TRAINER = "Мой тренер"
BTN_FAVORITE_TRAINER = "Избранный тренер"
BTN_PICK_TRAINER = "Выбрать тренера"
BTN_CANCEL_RECORD = "Отменить запись"
BTN_CABINET = "Личный кабинет"
BTN_SCHEDULE = "Расписание"
BTN_ABONEMENT = "Мой абонемент"
BTN_NEXT_RECORD = "Ближайшая запись"
BTN_INFO = "Справка"
BTN_CONTACTS = "Контакты"
BTN_FAQ = "Вопросы и ответы"
BTN_BOOK_ONLINE = "Записаться онлайн"
BTN_HOW_TO_USE = "Как пользоваться"

BTN_SCHEDULE_TODAY = "Сегодня"
BTN_SCHEDULE_TOMORROW = "Завтра"
BTN_SCHEDULE_5 = "5 дней"
BTN_SCHEDULE_10 = "10 дней"
BTN_SCHEDULE_15 = "15 дней"
BTN_CHANGE_PHONE = "Изменить номер"
BTN_HELP = "Помощь"
BTN_MENU = "В главное меню"

BTN_CABINET_REFRESH = "Обновить"
BTN_CABINET_RECORDS = "Мои записи"
BTN_CABINET_HISTORY = "История"
BTN_CABINET_ABONEMENT = "Абонемент"

BTN_CANCEL = "Отмена"


def main_menu(user_id: int) -> str:
    if not storage.get_phone(user_id):
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button(BTN_LOGIN, color=VkKeyboardColor.POSITIVE)
        keyboard.add_button(BTN_BOOK_ONLINE, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(BTN_INFO, color=VkKeyboardColor.SECONDARY)
        keyboard.add_button(BTN_CONTACT_ADMIN, color=VkKeyboardColor.SECONDARY)
        return keyboard.get_keyboard()

    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(BTN_BOOK, color=VkKeyboardColor.POSITIVE)
    keyboard.add_button(BTN_BOOK_AGAIN, color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button(BTN_NEXT_RECORD, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_CANCEL_RECORD, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_CABINET, color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button(BTN_SCHEDULE, color=VkKeyboardColor.SECONDARY)
    keyboard.add_button(BTN_ABONEMENT, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_INFO, color=VkKeyboardColor.SECONDARY)
    keyboard.add_button(BTN_CONTACT_ADMIN, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_LOGOUT, color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()


def info_menu(user_id: int) -> str:
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(BTN_CONTACTS, color=VkKeyboardColor.PRIMARY)
    keyboard.add_button(BTN_FAQ, color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button(BTN_BOOK_ONLINE, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_HOW_TO_USE, color=VkKeyboardColor.SECONDARY)
    if storage.get_phone(user_id):
        keyboard.add_button(BTN_CHANGE_PHONE, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_MENU, color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def admin_chat_menu() -> str:
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(BTN_BOT_MENU, color=VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()


def schedule_period_menu(user_id: int) -> str:
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(BTN_SCHEDULE_TODAY, color=VkKeyboardColor.PRIMARY)
    keyboard.add_button(BTN_SCHEDULE_TOMORROW, color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button(BTN_SCHEDULE_5, color=VkKeyboardColor.SECONDARY)
    keyboard.add_button(BTN_SCHEDULE_10, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_SCHEDULE_15, color=VkKeyboardColor.SECONDARY)
    if user_prefs.get_favorite_staff(user_id):
        keyboard.add_line()
        keyboard.add_button(BTN_SCHEDULE_MY_TRAINER, color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button(BTN_MENU, color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def cabinet_menu() -> str:
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(BTN_CABINET_REFRESH, color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button(BTN_CABINET_RECORDS, color=VkKeyboardColor.SECONDARY)
    keyboard.add_button(BTN_CABINET_HISTORY, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_CABINET_ABONEMENT, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_FAVORITE_TRAINER, color=VkKeyboardColor.SECONDARY)
    keyboard.add_button(BTN_PICK_TRAINER, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_MENU, color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def phone_input_menu() -> str:
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button(BTN_CANCEL, color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button(BTN_MENU, color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()
