from aiogram import Bot, F, Router, types
from aiogram.filters import CommandStart, Text
from aiogram.types import FSInputFile, Message

from app.db.functions import User
from app.keyboards.inline_start_dialog import greeting_keyboard_hello

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    user_id = message.from_user.id

    if not await User.is_registered(user_id):
        await User.register(user_id)

    video_note = FSInputFile(r'app/crs/video/Timosha_startV_1.mp4')
    await bot.send_video_note(message.chat.id, video_note)

    await message.answer(f"<b> Кто здесь? 😾</b>\n", reply_markup=greeting_keyboard_hello(message.from_user.full_name))
