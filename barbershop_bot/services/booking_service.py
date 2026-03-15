from datetime import datetime, timedelta
from config import START_TIME, END_TIME


def generate_time_slots(duration):

    start = datetime.strptime(START_TIME, "%H:%M")
    end = datetime.strptime(END_TIME, "%H:%M")

    slots = []

    while start < end:
        slots.append(start.strftime("%H:%M"))
        start += timedelta(minutes=duration)

    return slots