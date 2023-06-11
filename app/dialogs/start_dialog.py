from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, ContentType
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, SwitchTo
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const


class StartDialog(StatesGroup):
    greeting = State()
    second = State()
    third = State()


async def start_journey(c: CallbackQuery, button: Button, manager: DialogManager):
    pass


ui = Dialog(
    Window(
        Const(
            f"Я Тимофей, манул из Московского зоопарка. Я очень рад тебя видеть! А ты случайно не принес мне еды? "
            f"Я очень люблю есть вкусняшки. 😻 \n"
        ),
        SwitchTo(Const("Прости, у меня ничего с собой нет"), id="second", state=StartDialog.second),
        state=StartDialog.greeting,
    ),
    Window(
        StaticMedia(
            path=r'app/crs/pic/Timofei_sad.jpg',
            type=ContentType.PHOTO,
        ),
        Const(
            f"Очень жаль. Так зачем ты здесь? \n"
            f"Наверное ты хочешь стать частью моей команды? \n"
            f"Я чувствую в тебе огромную силу, твой внутренний зверь так и рвется на волю! \n"
            f"Ты знаешь кто он? \n"
        ),
        SwitchTo(Const("Нет, но думаю это будет интересно!"), id="third", state=StartDialog.third),
        state=StartDialog.second,
    ),
    Window(
        Const(
            f"Неожиданно! \n"
            f"Тогда я предлагаю тебе отправиться в небольшое путешествие, что бы выяснить кто ты есть на самом деле! \n"
            f"В путь? \n"
        ),
        Button(Const("Вперед!"), id="start_journey", on_click=start_journey),
        state=StartDialog.third,
    )
)
