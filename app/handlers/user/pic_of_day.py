import io

from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import BufferedInputFile, Message

from app.db.functions import Animals
from app.db.image_generator import create_pic_of_day
from app.keyboards.inline_result_dialog import result_keyboard_animal_url

router = Router()


@router.message(Command(commands=["pic_of_day"]))
async def daypic_handler(message: Message, bot: Bot):
    animal = await Animals.get_random_animal()

    image = create_pic_of_day(f"app/{animal.image}", f"{animal.name}")

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    await bot.send_photo(message.chat.id,
                         BufferedInputFile(
                             img_bytes,
                             filename="pic_of_day.jpg"
                         ),
                         caption='',
                         reply_markup=result_keyboard_animal_url(animal.name, animal.url))
