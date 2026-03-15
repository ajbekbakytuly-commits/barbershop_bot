from datetime import datetime, timedelta


def generate_dates():

    dates = []

    today = datetime.today()

    for i in range(7):
        d = today + timedelta(days=i)
        dates.append(d.strftime("%Y-%m-%d"))

    return dates


def generate_time_slots():

    slots = []

    start = 9
    end = 18

    for hour in range(start, end):

        slots.append(f"{hour:02d}:00")
        slots.append(f"{hour:02d}:30")

    return 