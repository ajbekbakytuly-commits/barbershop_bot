from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# главное меню
def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✂️ Записаться", callback_data="booking")],
            [InlineKeyboardButton(text="📅 Мои записи", callback_data="my_apps")]
        ]
    )


# услуги
def services_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✂️ Мужская стрижка", callback_data="service_cut")],
            [InlineKeyboardButton(text="🧔 Стрижка + борода", callback_data="service_beard")],
            [InlineKeyboardButton(text="🪒 Бритье", callback_data="service_shave")],
            [InlineKeyboardButton(text="👦 Детская стрижка", callback_data="service_kids")]
        ]
    )


# мастера
def masters_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👨‍🔧 Барбер Ахмет", callback_data="master_1")],
            [InlineKeyboardButton(text="👨‍🔧 Барбер Данияр", callback_data="master_2")],
            [InlineKeyboardButton(text="👨‍🔧 Барбер Руслан", callback_data="master_3")]
        ]
    )


# выбор даты
def dates_keyboard(dates):

    keyboard = []

    for d in dates:
        keyboard.append(
            [InlineKeyboardButton(text=d, callback_data=f"date_{d}")]
        )

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# выбор времени
def times_keyboard(times):

    keyboard = []

    for t in times:
        keyboard.append(
            [InlineKeyboardButton(text=t, callback_data=f"time_{t}")]
        )

    return InlineKeyboardMarkup(inline_keyboard=keyboard)