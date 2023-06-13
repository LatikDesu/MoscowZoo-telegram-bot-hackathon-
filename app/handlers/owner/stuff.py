import time

from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import CallbackQuery, Message

from app.db.functions import User
from app.filters.is_owner import IsOwner
from app.keyboards.admin_kayboard import admin_menu, back_button

router = Router()


@router.message(IsOwner(is_owner=True), Command(commands=["admin"]))
async def admin_command(message: Message) -> None:
    await message.answer("<b>Меню администратора:</b>", reply_markup=admin_menu(), parse_mode='HTML')


@router.callback_query(Text('admin'))
async def back_admin_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text("<b>Меню администратора</b>", reply_markup=admin_menu(), parse_mode='HTML')


@router.callback_query(IsOwner(is_owner=True), Text('requests'))
async def admin_traffic_statistics(callback: CallbackQuery):
    requests_list = await User.user_requests()
    if not requests_list:
        requests_list = "Нет новых заявок!"

    await callback.message.edit_text(requests_list, reply_markup=back_button(), parse_mode='HTML')


@router.callback_query(IsOwner(is_owner=True), Text('statistics'))
async def admin_traffic_statistics(callback: CallbackQuery):
    count = await User.get_count()
    totem_count = await User.get_totem_count()
    contact_count = await User.get_contact_count()

    text = f"📊 <b>Количество пользователей бота -</b> <code> {count} </code>  \n 📊 <b>Количество пользователей, " \
           f"прошедших викторину -</b> <code> {totem_count} </code> \n 📊 <b>Количество заявок для связи -</b> " \
           f"<code> {contact_count} </code> \n"

    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode='HTML')


@router.callback_query(Text('close'))
async def admin_close_menu(callback: CallbackQuery) -> None:
    await callback.message.delete()
