from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from bot.booking_keyboards import BTN_PAGE_NEXT, BTN_PAGE_PREV, paginate
from bot.keyboards import BTN_CANCEL, BTN_MENU

BTN_CLEAR_FAVORITE = "Убрать избранного"

TRAINER_PAGE_SIZE = 6


def build_trainer_pick_keyboard(labels: list[str], page: int = 0) -> str:
    chunk, _, has_prev, has_next = paginate(labels, page, TRAINER_PAGE_SIZE)
    keyboard = VkKeyboard(one_time=True)
    for index, label in enumerate(chunk):
        if index > 0:
            keyboard.add_line()
        keyboard.add_button(label, color=VkKeyboardColor.SECONDARY)
    if has_prev or has_next:
        keyboard.add_line()
        if has_prev and has_next:
            keyboard.add_button(BTN_PAGE_PREV, color=VkKeyboardColor.SECONDARY)
            keyboard.add_button(BTN_PAGE_NEXT, color=VkKeyboardColor.SECONDARY)
        elif has_prev:
            keyboard.add_button(BTN_PAGE_PREV, color=VkKeyboardColor.SECONDARY)
        else:
            keyboard.add_button(BTN_PAGE_NEXT, color=VkKeyboardColor.SECONDARY)
    keyboard.add_line()
    keyboard.add_button(BTN_CLEAR_FAVORITE, color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button(BTN_MENU, color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()
