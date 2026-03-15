import sqlite3

DB_NAME = "barbershop.db"


# создание таблицы
def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        service TEXT,
        master TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()


# добавить запись
def add_appointment(user_id, service, master, date, time):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO appointments (user_id, service, master, date, time) VALUES (?, ?, ?, ?, ?)",
        (user_id, service, master, date, time)
    )

    conn.commit()
    conn.close()


# проверить занято ли время
def is_time_busy(master, date, time):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM appointments WHERE master=? AND date=? AND time=?",
        (master, date, time)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


# записи пользователя
def get_user_appointments(user_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT service, master, date, time FROM appointments WHERE user_id=?",
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


# все записи (для админа)
def get_all_appointments():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, service, master, date, time FROM appointments"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows