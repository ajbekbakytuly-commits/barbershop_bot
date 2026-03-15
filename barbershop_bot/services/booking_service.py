from datetime import datetime, timedelta
from database.db import is_time_busy


# генерация дат (7 дней)
def generate_dates():

    dates = []

    today = datetime.today()

    for i in range(7):

        d = today + timedelta(days=i)

        dates.append(d.strftime("%Y-%m-%d"))

    return dates


# генерация времени
def generate_time_slots():

    slots = []

    start = 9
    end = 18

    for hour in range(start, end):

        slots.append(f"{hour:02d}:00")
        slots.append(f"{hour:02d}:30")

    return slots


# свободные слоты
def get_free_slots(master, date):

    all_slots = generate_time_slots()

    free_slots = []

    for time in all_slots:

        if not is_time_busy(master, date, time):

            free_slots.append(time)

    return free_slots