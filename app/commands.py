from aiogram import Bot
from aiogram.types import (BotCommand, BotCommandScopeChat,
                           BotCommandScopeDefault)

from app.config import Config

users_commands = {
    "start": "Начать работу",
    "journey": "Отправиться в путешествие",
    "connect": "Связаться с нами",
    "pic_of_day": "Получить животное дня",
    "help": "Показать список команд",
}

owner_commands = {**users_commands, "admin": "admin panel"}


async def setup_bot_commands(bot: Bot, config: Config):
    await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in owner_commands.items()
        ],
        scope=BotCommandScopeChat(chat_id=config.settings.owner_id),
    )

    await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in users_commands.items()
        ],
        scope=BotCommandScopeDefault(),
    )


async def remove_bot_commands(bot: Bot, config: Config):
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    await bot.delete_my_commands(
        scope=BotCommandScopeChat(chat_id=config.settings.owner_id)
    )
