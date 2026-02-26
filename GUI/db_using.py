import sqlite3

conn = sqlite3.connect('activity.db')
cursor = conn.cursor()

def get_all_session():
    return cursor.execute("SELECT id_session, start_time, end_time FROM session ORDER BY start_time DESC").fetchall()

def get_all_activity(id_session: int):
    return cursor.execute('''SELECT process_name, sum(strftime('%s', end_time) - strftime('%s', start_time)) AS diff_seconds
                          FROM activity WHERE id_session=? GROUP BY process_name ORDER BY diff_seconds DESC''',
                          (id_session,)).fetchall()
def get_detail_activity(id_session: int, process_name: str):
    return cursor.execute('''SELECT id_activity, id_session, process_name, start_time, end_time FROM activity 
                          WHERE id_session=? AND process_name=? ORDER BY start_time DESC''', (id_session, process_name)).fetchall()

def clear_db():
    cursor.execute("DELETE FROM session")
    cursor.execute("DELETE FROM activity")
    cursor.execute("DELETE FROM sqlite_sequence")
    conn.commit()

def current_session(id_session: int):
    return cursor.execute('''SELECT start_time, end_time FROM session WHERE id_session=?''', (id_session,)).fetchone()