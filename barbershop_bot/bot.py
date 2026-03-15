import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database.db import init_db
from handlers import user, admin
from utils.scheduler import scheduler

# загрузка .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():

    print("Bot started...")

    # инициализация базы данных
    init_db()

    # подключаем роутеры
    dp.include_router(user.router)
    dp.include_router(admin.router)

    # запуск планировщика
    scheduler.start()

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())