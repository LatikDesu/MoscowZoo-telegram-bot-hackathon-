from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Заявки', callback_data='requests'))
    builder.row(InlineKeyboardButton(text='Статистика', callback_data='statistics'))
    builder.row(InlineKeyboardButton(text='Закрыть ❌', callback_data='close'))
    return builder.as_markup(resize_keyboard=True)


def back_button() -> InlineKeyboardMarkup:
    return InlineKeyboardBuilder().button(
        text='< Назад',
        callback_data='admin'
    ).as_markup(resize_keyboard=True)
