from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ADMIN_IDS

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id not in ADMIN_IDS:
        return

    await message.answer(
        "⚙️ Админ панель\n\n"
        "Здесь будет управление мастерами и услугами."
    )