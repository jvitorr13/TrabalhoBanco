import sqlite3

def check_slave_data():
    conn = sqlite3.connect('slave.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    print("Dados no banco de dados slave:")
    for user in users:
        print(f'ID: {user[0]}, Name: {user[1]}, Email: {user[2]}')

    conn.close()

if __name__ == '__main__':
    check_slave_data()
