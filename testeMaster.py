import sqlite3

def check_master_data():
    conn = sqlite3.connect('master.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    print("Dados no banco de dados master:")
    for user in users:
        print(f'ID: {user[0]}, Name: {user[1]}, Email: {user[2]}')

    conn.close()

if __name__ == '__main__':
    check_master_data()
