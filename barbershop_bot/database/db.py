import aiosqlite

DB_NAME = "barbershop.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            name TEXT,
            username TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS masters(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS services(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            duration INTEGER
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS appointments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            master_id INTEGER,
            service_id INTEGER,
            date TEXT,
            time TEXT,
            status TEXT
        )
        """)

        await db.commit()