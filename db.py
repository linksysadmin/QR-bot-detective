import sqlite3

from config import DB_NAME

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()


def check_database():
    cursor.execute(f'''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='qr_codes' ''')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''CREATE TABLE qr_codes (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)''')
        conn.commit()
        conn.close()


def save_qr_data_to_db(qr_data):
    cursor.execute("INSERT INTO qr_codes (data) VALUES (?)", (qr_data,))
    conn.commit()
    conn.close()
