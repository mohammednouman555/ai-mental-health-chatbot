import sqlite3

DB_NAME = "chat_history.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        emotion TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_chat(user_message, bot_response, emotion):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chats (user_message, bot_response, emotion) VALUES (?, ?, ?)",
        (user_message, bot_response, emotion)
    )

    conn.commit()
    conn.close()


def get_chat_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT user_message, bot_response, emotion FROM chats")
    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "user_message": row[0],
            "bot_response": row[1],
            "emotion": row[2]
        }
        for row in rows
    ]


# Initialize DB on import
init_db()