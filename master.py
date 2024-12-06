import sqlite3
import time

def create_master_db():
    conn = sqlite3.connect('master.db')
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

def insert_user(conn, name, email):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    print(f'Inserted user: {name}, {email}')

def main():
    master_conn = create_master_db()

    # Inserir alguns dados
    insert_user(master_conn, 'Alice', 'alice@example.com')
    insert_user(master_conn, 'Bob', 'bob@example.com')

    try:
        while True:
            name = input("Enter user name (or type 'exit' to quit): ")
            if name.lower() == 'exit':
                break
            email = input("Enter user email: ")
            insert_user(master_conn, name, email)
    finally:
        master_conn.close()

if __name__ == '__main__':
    main()
