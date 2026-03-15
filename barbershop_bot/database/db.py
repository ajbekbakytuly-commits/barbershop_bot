import sqlite3

conn = sqlite3.connect("barbershop.db")
cursor = conn.cursor()


def init_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        service TEXT,
        master TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()


def add_appointment(user_id, service, master, date, time):

    cursor.execute(
        "INSERT INTO appointments (user_id, service, master, date, time) VALUES (?, ?, ?, ?, ?)",
        (user_id, service, master, date, time)
    )

    conn.commit()


def get_user_appointments(user_id):

    cursor.execute(
        "SELECT service, master, date, time FROM appointments WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchall()


def is_time_busy(master, date, time):

    cursor.execute(
        "SELECT * FROM appointments WHERE master=? AND date=? AND time=?",
        (master, date, time)
    )

    return cursor.fetchone()


def get_all_appointments():

    conn = sqlite3.connect("barbershop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, service, master, date, time FROM appointments"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows