from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_IDS
from database.db import get_all_appointments

router = Router()


# клавиатура админ панели
def admin_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📅 Все записи", callback_data="admin_apps")]
        ]
    )


# команда /admin
@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id not in ADMIN_IDS:
        return

    await message.answer(
        "⚙️ Админ панель",
        reply_markup=admin_keyboard()
    )


# просмотр всех записей
@router.callback_query(F.data == "admin_apps")
async def show_all_apps(callback: CallbackQuery):

    if callback.from_user.id not in ADMIN_IDS:
        return

    apps = get_all_appointments()

    if not apps:

        await callback.message.answer("📅 Записей пока нет")
        return

    text = "📅 Все записи:\n\n"

    for user_id, service, master, date, time in apps:

        text += (
            f"👤 Пользователь: {user_id}\n"
            f"✂️ Услуга: {service}\n"
            f"👨‍🔧 Мастер: {master}\n"
            f"📅 Дата: {date}\n"
            f"🕐 Время: {time}\n\n"
        )

    await callback.message.answer(text)