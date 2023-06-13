from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def greeting_keyboard_hello(user_name):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f"Ой, извините.\n Меня зовут {user_name} ...",
                             callback_data="greeting"),
    )
    return keyboard.as_markup()


def greeting_keyboard_sorry():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f"Прости, у меня ничего с собой нет 😔",
                             callback_data="sorry"),
    )
    return keyboard.as_markup()


def greeting_keyboard_know():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f"Нет, но я бы очень хотел это узнать!",
                             callback_data="know"),
    )
    return keyboard.as_markup()


def greeting_keyboard_start_journey():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f"Вперед!",
                             callback_data="start_journey"),
    )
    return keyboard.as_markup()
