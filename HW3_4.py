import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
   id     INTEGER PRIMARY KEY AUTOINCREMENT,
   name   TEXT NOT NULL,
   age    INTEGER,
   email  TEXT UNIQUE
)
""")

conn.commit()

conn.close()
