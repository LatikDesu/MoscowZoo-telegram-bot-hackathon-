from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def result_keyboard_what(code_number):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='😕', callback_data=f"prefix_{code_number}"),
    )
    return keyboard.as_markup()


def result_keyboard_animal_url(name, url):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f'{name}', url=f"{url}"),
    )
    return keyboard.as_markup()


def result_keyboard_share():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f'Поделиться', switch_inline_query='Я нашел себе новую семью! \n'
                                                                     f'https://t.me/ZooMow_bot'),
    )
    return keyboard.as_markup()


def result_keyboard_info():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f'Расскажи подробнее...', callback_data=f"info"),
    )
    return keyboard.as_markup()


def result_keyboard_friend_club():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text=f'Клуб друзей', url="https://www.justbenice.ru/work/moscowzoo/"),
        InlineKeyboardButton(text=f'Программа опекунства', url="https://moscowzoo.ru/my-zoo/become-a-guardian/"),
    )
    return keyboard.as_markup()


def result_keyboard_finish():
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(text=f'Получить контакты', callback_data=f"contacts")
    )
    keyboard.row(
        InlineKeyboardButton(text=f'Повторить викторину', callback_data=f"start_journey")
    )
    return keyboard.as_markup()
