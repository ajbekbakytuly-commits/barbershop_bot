from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline import main_menu

router = Router()


@router.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "💈 Добро пожаловать в барбершоп!",
        reply_markup=main_menu()
    )