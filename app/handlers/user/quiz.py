from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode

from app.db.quiz_generator import create_quiz
from app.dialogs.quiz_dialog import QuizDialog
from app.handlers.user.start_dialog import GreetingState

router = Router()


@router.callback_query(GreetingState.third, Text("start_journey"))
async def first_question(callback: CallbackQuery, dialog_manager: DialogManager):
    data = await create_quiz()
    await dialog_manager.start(QuizDialog.first, data=data, mode=StartMode.RESET_STACK)


@router.message(Command(commands=["journey"]))
async def first_question(message: Message, dialog_manager: DialogManager):
    data = await create_quiz()
    await dialog_manager.start(QuizDialog.first, data=data, mode=StartMode.RESET_STACK)


@router.callback_query(Text("start_journey"))
async def first_question(callback: CallbackQuery, dialog_manager: DialogManager):
    data = await create_quiz()
    await dialog_manager.start(QuizDialog.first, data=data, mode=StartMode.RESET_STACK)
