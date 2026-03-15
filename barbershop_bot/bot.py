import asyncio
import os
from aiogram import Bot, Dispatcher

from database.db import init_db
from handlers import user, admin
from utils.scheduler import scheduler

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():

    print("Bot started...")

    await init_db()

    dp.include_router(user.router)
    dp.include_router(admin.router)

    # запуск планировщика
    scheduler.start()

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())