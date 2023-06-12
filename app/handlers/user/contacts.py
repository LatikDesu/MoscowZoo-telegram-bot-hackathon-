from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

from app.db.functions import User

router = Router()


@router.callback_query(Text("contacts"))
async def result_friend_club(callback: CallbackQuery):
    await User.user_wants_contact(telegram_id=callback.from_user.id, username=f'@{callback.from_user.username}')

    await callback.answer(
        f"Мы обязательно с вами свяжемся!"
        u"\U00002764",
    )

    await callback.answer()
