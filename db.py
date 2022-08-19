import sqlite3


def connect():
    connection = sqlite3.connect('shows.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Shows
                  (Title TEXT, Director TEXT, Year INT)''')

    connection.commit()
    connection.close()


class db:
    pass


if __name__ == '__main__':
    a = connect()
    print(a)