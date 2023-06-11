from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(Text("contacts"))
async def result_friend_club(callback: CallbackQuery):
    await callback.answer(
        f"Мы обязательно с вами свяжемся!"
        u"\U00002764",
    )

    await callback.answer()
