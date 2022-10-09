import sqlite3 

def get_db_conection():
    conn = sqlite3.connect('user_info.db')
    conn.row_factory = sqlite3.Row
    return conn
