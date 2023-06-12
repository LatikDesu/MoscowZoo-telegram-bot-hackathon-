from operator import itemgetter
from typing import Any

from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Row, Select
from aiogram_dialog.widgets.text import Const, Format

from app.keyboards.inline_result_dialog import result_keyboard_what

code_string = []


class QuizDialog(StatesGroup):
    first = State()
    second = State()
    third = State()
    fourth = State()
    fifth = State()
    finish = State()


async def get_data(dialog_manager: DialogManager, **kwargs):
    counter = dialog_manager.current_context().dialog_data.get("counter", 1)
    dialog_manager.current_context().dialog_data["counter"] = counter + 1

    dialog_data = dialog_manager.start_data
    code = dialog_data.get(int(counter)).get("code")
    code_line = dialog_manager.current_context().dialog_data["code"] = code

    return {
        "question": dialog_data.get(int(counter)).get("question"),
        "answers": '\n'.join(dialog_data.get(int(counter)).get("answers")),
    }


async def on_selected(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    code_line = manager.current_context().dialog_data.get("code")
    code_id = code_line[int(item_id) - 1]

    code_string.append(code_id)
    await manager.next()


async def go_back(c: CallbackQuery, button: Button, manager: DialogManager):
    counter = manager.current_context().dialog_data.get("counter", 1)
    manager.current_context().dialog_data["counter"] = counter - 2

    code_string.pop()
    await manager.back()


async def finish_quiz(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    counter = manager.current_context().dialog_data.get("counter", 1)
    code_line = manager.start_data.get(int(counter) - 1).get("code")
    code_id = code_line[int(item_id) - 1]

    code_string.append(code_id)
    code_number = "".join(code_string)
    code_string.clear()

    await c.message.answer(f"🤔", reply_markup=result_keyboard_what(code_number))

    await manager.done()


items = [("1", u"\U00000031\U0000FE0F\U000020E3"),
         ("2", u"\U00000032\U0000FE0F\U000020E3"),
         ("3", u"\U00000033\U0000FE0F\U000020E3"),
         ("4", u"\U00000034\U0000FE0F\U000020E3"),
         ("5", u"\U00000035\U0000FE0F\U000020E3")]

select = Select(
    Format("{item[1]}"),
    "select",
    itemgetter(0),
    items,
    on_click=on_selected,
)

ui = Dialog(
    Window(
        select,
        Format("<b> {question} </b>\n"),
        Format("{answers}"),
        getter=get_data,
        state=QuizDialog.first,
    ),

    Window(
        select,
        Format("<b> {question} </b>\n"),
        Format("{answers}"),
        # Button(Const("Вернуться"), id="back", on_click=go_back),
        getter=get_data,
        state=QuizDialog.second,
    ),

    Window(
        select,
        Format("<b> {question} </b>\n"),
        Format("{answers}"),
        # Button(Const("Вернуться"), id="back", on_click=go_back),
        getter=get_data,
        state=QuizDialog.third,
    ),

    Window(
        select,
        Format("<b> {question} </b>\n"),
        Format("{answers}"),
        # Button(Const("Вернуться"), id="back", on_click=go_back),
        getter=get_data,
        state=QuizDialog.fourth,
    ),

    Window(
        select,

        Format("<b> {question} </b>\n"),
        Format("{answers}"),
        # Button(Const("Вернуться"), id="back", on_click=go_back),
        getter=get_data,
        state=QuizDialog.fifth,
    ),

    Window(
        Select(
            Format("{item[1]}"),
            "select",
            itemgetter(0),
            items,
            on_click=finish_quiz,
        ),
        # Button(Const("Вернуться"), id="back", on_click=go_back),
        Format("<b> {question} </b>\n"),
        Format("{answers}"),
        getter=get_data,
        state=QuizDialog.finish,
    ),
)
