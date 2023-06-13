import asyncio

from aiogram import Bot, F, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, FSInputFile

from app.keyboards.inline_start_dialog import (greeting_keyboard_know,
                                               greeting_keyboard_sorry,
                                               greeting_keyboard_start_journey)

router = Router()


class GreetingState(StatesGroup):
    first = State()
    second = State()
    third = State()


@router.callback_query(Text("greeting"))
async def go_to_start_dialog(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    photo = FSInputFile(r'app/crs/pic/Timofei.jpg')
    await bot.send_photo(callback.from_user.id, photo)
    await callback.message.answer(
        f"Приветствую, <b>{callback.from_user.first_name} </b>! \n")

    await callback.message.answer(
        f"Я Тимофей, символ и гордость Московского зоопарка."
        f" Я очень рад тебя видеть! \n А ты случайно не принес мне еды? \n"
        f"Я очень люблю есть вкусняшки. 😻 \n",
        reply_markup=greeting_keyboard_sorry(),
    )

    await callback.answer()
    await state.set_state(GreetingState.first)


@router.callback_query(GreetingState.first, Text("sorry"))
async def greeting_second(callback: CallbackQuery, bot: Bot, state: FSMContext):
    photo = FSInputFile(r'app/crs/pic/Timofei_sad.jpg')
    await bot.send_photo(callback.from_user.id, photo)

    await callback.message.answer(
        f"Очень жаль. 🙀\n"
        f"Так зачем ты здесь? \n")

    await asyncio.sleep(3)

    await callback.message.answer(
        f"Ты хочешь стать частью моей команды? \n"
        f"Твой внутренний зверь так и рвется на волю! \n"
        f"Ты знаешь кто он? \n",
        reply_markup=greeting_keyboard_know(),
    )
    await callback.answer()
    await state.set_state(GreetingState.second)


@router.callback_query(GreetingState.second, Text("know"))
async def greeting_second(callback: CallbackQuery, bot: Bot, state: FSMContext):
    photo = FSInputFile(r'app/crs/pic/Timofei_2.jpg')
    await bot.send_photo(callback.from_user.id, photo)

    await callback.message.answer(
        f"Тогда я задам тебе несколько вопросов, что бы выяснить кто ты "
        f"есть на самом деле! \n"
        f"<b> Ты готов? </b>\n",
        reply_markup=greeting_keyboard_start_journey(),
    )

    await callback.answer()
    await state.set_state(GreetingState.third)
