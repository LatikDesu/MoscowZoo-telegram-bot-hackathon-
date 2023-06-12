import asyncio
import io

from aiogram import Bot, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import BufferedInputFile, CallbackQuery, Message

from app.db.functions import Animals, ResultDescription, User
from app.db.image_generator import create_totem_pic
from app.keyboards.inline_result_dialog import (result_keyboard_animal_url,
                                                result_keyboard_finish,
                                                result_keyboard_friend_club,
                                                result_keyboard_info)

router = Router()


class ResultState(StatesGroup):
    first = State()
    second = State()
    third = State()


@router.callback_query(Text(startswith="prefix_"))
async def result_image(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)

    animal_code = callback.data.split("_")[1]

    totem_animal = await Animals.get_totem_animal(int(animal_code))

    description = await ResultDescription.get_description()

    image = create_totem_pic(f"app/{totem_animal.image}", f"{totem_animal.name}")

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    totem_pic = BufferedInputFile(img_bytes, filename="totem.png")

    await User.user_complete_quiz(callback.from_user.id, totem_animal.name)

    bot_information = await bot.get_me()

    await bot.send_photo(callback.from_user.id, totem_pic,
                         caption=f'<b>{totem_animal.name} </b>{description.description}\n'
                                 f'@{bot_information.username}',
                         reply_markup=result_keyboard_animal_url(totem_animal.name, totem_animal.url))

    await asyncio.sleep(3)
    await callback.message.answer(
        f"Теперь у тебя есть возможность помочь Московскому зоопарку и поделиться своей силой и заботой  — это "
        f"прекрасная возможность принять участие в деле сохранения редких видов, помочь нам в реализации "
        f"природоохранных программ.",
        reply_markup=result_keyboard_info(),
    )

    await callback.answer()
    await state.set_state(ResultState.first)


@router.callback_query(ResultState.first, Text("info"))
async def result_friend_club(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await callback.message.answer(
        f"В рамках Программы лояльности Московского зоопарка любой желающий может взять одно из животных под свою "
        f"опеку. Все — от маленьких посетителей до больших корпораций, — кто неравнодушен к жизни обитателей "
        f"зоопарка, может стать участником программы.",
        reply_markup=result_keyboard_friend_club(),
    )

    await asyncio.sleep(3)
    await callback.message.answer(
        f"Если Вас заинтересовала программа опеки, то нажмите на сердечко и мы обязательно свяжемся с Вами.\n"
        f"Также Вы можешь связаться с нами напрямую используя команду <b>/connect</b>\n\n"
        f"<b>До встречи!</b>",
        reply_markup=result_keyboard_finish(),
    )
    await state.clear()
    await callback.answer()
