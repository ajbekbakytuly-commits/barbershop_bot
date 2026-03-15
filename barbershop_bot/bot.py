import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database.db import init_db
from handlers import user, admin
from utils.scheduler import scheduler


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():

    await init_db()

    dp.include_router(user.router)
    dp.include_router(admin.router)

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())