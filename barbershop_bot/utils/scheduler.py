from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import timedelta

scheduler = AsyncIOScheduler()


def schedule_reminder(bot, user_id, appointment_time):

    reminder_time = appointment_time - timedelta(hours=1)

    scheduler.add_job(
        send_reminder,
        "date",
        run_date=reminder_time,
        args=[bot, user_id]
    )


async def send_reminder(bot, user_id):

    await bot.send_message(
        user_id,
        "🔔 Напоминание\n\nЧерез 1 час у вас запись в барбершоп."
    )