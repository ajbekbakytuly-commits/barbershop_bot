from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.inline import (
    main_menu,
    services_keyboard,
    masters_keyboard,
    dates_keyboard,
    times_keyboard
)

from services.booking_service import generate_dates, get_free_slots
from database.db import add_appointment, get_user_appointments

router = Router()

# временное хранилище выбора пользователя
user_data = {}

# список услуг
services = {
    "cut": "Мужская стрижка",
    "beard": "Стрижка + борода",
    "shave": "Бритье",
    "kids": "Детская стрижка"
}

# список мастеров
masters = {
    "1": "Ахмет",
    "2": "Данияр",
    "3": "Руслан"
}


# старт
@router.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "💈 Добро пожаловать в барбершоп!",
        reply_markup=main_menu()
    )


# начать запись
@router.callback_query(F.data == "booking")
async def booking(callback: CallbackQuery):

    user_data[callback.from_user.id] = {}

    await callback.message.answer(
        "✂️ Выберите услугу:",
        reply_markup=services_keyboard()
    )


# выбор услуги
@router.callback_query(F.data.startswith("service_"))
async def choose_service(callback: CallbackQuery):

    service_key = callback.data.split("_")[1]

    user_data[callback.from_user.id]["service"] = services.get(service_key)

    await callback.message.answer(
        "👨‍🔧 Выберите мастера:",
        reply_markup=masters_keyboard()
    )


# выбор мастера
@router.callback_query(F.data.startswith("master_"))
async def choose_master(callback: CallbackQuery):

    master_key = callback.data.split("_")[1]

    user_data[callback.from_user.id]["master"] = masters.get(master_key)

    dates = generate_dates()

    await callback.message.answer(
        "📅 Выберите дату:",
        reply_markup=dates_keyboard(dates)
    )


# выбор даты
@router.callback_query(F.data.startswith("date_"))
async def choose_date(callback: CallbackQuery):

    date = callback.data.split("_")[1]

    user_data[callback.from_user.id]["date"] = date

    master = user_data[callback.from_user.id]["master"]

    times = get_free_slots(master, date)

    if not times:

        await callback.message.answer("❌ На эту дату нет свободного времени")
        return

    await callback.message.answer(
        "🕐 Выберите время:",
        reply_markup=times_keyboard(times)
    )


# выбор времени
@router.callback_query(F.data.startswith("time_"))
async def choose_time(callback: CallbackQuery):

    user_id = callback.from_user.id

    if user_id not in user_data:

        await callback.message.answer("⚠️ Начните запись заново")
        return

    time = callback.data.split("_")[1]

    data = user_data[user_id]

    service = data["service"]
    master = data["master"]
    date = data["date"]

    add_appointment(
        user_id,
        service,
        master,
        date,
        time
    )

    await callback.message.answer(
        f"✅ Вы успешно записаны!\n\n"
        f"✂️ Услуга: {service}\n"
        f"👨‍🔧 Мастер: {master}\n"
        f"📅 Дата: {date}\n"
        f"🕐 Время: {time}"
    )

    user_data.pop(user_id, None)


# мои записи
@router.callback_query(F.data == "my_apps")
async def my_apps(callback: CallbackQuery):

    apps = get_user_appointments(callback.from_user.id)

    if not apps:

        await callback.message.answer("📅 У вас пока нет записей")
        return

    text = "📅 Ваши записи:\n\n"

    for service, master, date, time in apps:

        text += (
            f"✂️ {service}\n"
            f"👨‍🔧 {master}\n"
            f"📅 {date}\n"
            f"🕐 {time}\n\n"
        )

    await callback.message.answer(text)