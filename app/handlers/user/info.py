from aiogram import Bot, Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.commands import owner_commands, users_commands
from app.config import Config
from app.keyboards.inline import get_author_keyboard

router = Router()


@router.message(Command(commands=["help"]))
async def help_handler(message: Message, config: Config):
    text = "ℹ️ <b>Список команд:</b> \n\n"
    commands = (
        owner_commands.items()
        if message.from_user.id == config.settings.owner_id
        else users_commands.items()
    )
    for command, description in commands:
        text += f"/{command} - <b>{description}</b> \n"
    await message.answer(text)


@router.message(Command(commands=["connect"]))
async def about_handler(message: Message, bot: Bot, config: Config):
    bot_information = await bot.get_me()
    await message.answer(
        "<b>ℹ️ Информация для связи по вопросам программы Опеки:</b> \n\n"
        f"<b>Телефон - </b> +7 (958) 813-15-60 \n"
        f"<b>Email - </b> a.sharapova@moscowzoo.ru \n",
        reply_markup=get_author_keyboard(owner_id=config.settings.owner_id),
    )


@router.callback_query(Text("contacts"))
async def about_handler(callback: CallbackQuery, bot: Bot, config: Config):
    bot_information = await bot.get_me()
    await callback.message.answer(
        "<b>ℹ️ Информация для связи по вопросам программы Опеки:</b> \n\n"
        f"<b>Телефон - </b> +7 (958) 813-15-60 \n"
        f"<b>Email - </b> a.sharapova@moscowzoo.ru \n",
        reply_markup=get_author_keyboard(owner_id=config.settings.owner_id),
    )
    await callback.answer()
