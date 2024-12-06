import sqlite3
import time

def create_slave_db():
    conn = sqlite3.connect('slave.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def replicate_from_master():
    master_conn = sqlite3.connect('master.db')
    slave_conn = create_slave_db()

    while True:
        master_cursor = master_conn.cursor()
        master_cursor.execute('SELECT * FROM users')
        users = master_cursor.fetchall()

        slave_cursor = slave_conn.cursor()
        slave_cursor.execute('DROP TABLE IF EXISTS users')  # Limpa a tabela existente
        slave_cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')

        for user in users:
            slave_cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', user)

        slave_conn.commit()
        print("Replication completed.")
        time.sleep(5)  # Aguarda 5 segundos antes de replicar novamente

if __name__ == '__main__':
    replicate_from_master()
