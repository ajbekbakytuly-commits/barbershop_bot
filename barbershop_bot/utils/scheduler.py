from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

scheduler = AsyncIOScheduler()


def schedule_reminder(bot, user_id, service, master, date, time):

    appointment_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

    reminder_time = appointment_time - timedelta(hours=1)

    scheduler.add_job(
        bot.send_message,
        "date",
        run_date=reminder_time,
        args=[
            user_id,
            f"⏰ Напоминание!\n\nЧерез 1 час у вас запись\n\n✂️ Услуга: {service}\n👨‍🔧 Мастер: {master}\n🕐 Время: {time}"
        ]
    )