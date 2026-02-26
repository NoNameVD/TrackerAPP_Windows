import sqlite3
from datetime import datetime

def get_connect():
    return sqlite3.connect('activity.db')

def start_session():
    with get_connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO session (start_time) VALUES (?)",
                       (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),))
        id_session = cursor.lastrowid
        return id_session

def update_session(id_session: int):
    with get_connect() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE session SET end_time=? WHERE id_session=?",
                       (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_session))

def update_activity(id_session: int, process_name: str, start_time: str, end_time: str):
    with get_connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO activity (id_session, process_name, start_time, end_time) VALUES (?, ?, ?, ?)",
                       (id_session, process_name, start_time, end_time))


