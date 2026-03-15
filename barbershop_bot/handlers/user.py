from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.inline import main_menu

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "💈 Добро пожаловать в барбершоп!",
        reply_markup=main_menu()
    )


@router.callback_query(F.data == "booking")
async def booking(callback: CallbackQuery):
    await callback.message.answer("✂️ Вы начали запись на стрижку")


@router.callback_query(F.data == "my_apps")
async def my_apps(callback: CallbackQuery):
    await callback.message.answer("📅 У вас пока нет записей")


@router.callback_query(F.data == "confirm")
async def confirm(callback: CallbackQuery):
    await callback.message.answer("✅ Запись подтверждена")


@router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery):
    await callback.message.answer("❌ Запись отменена")