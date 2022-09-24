import sqlite3


def db_setup():

    """
    Recreate the tables (locally) and indexes.
    Tables -  CREATE TABLE status_text (status_id TEXT, status_text TEXT, comments TEXT)
    """

    with sqlite3.connect('database.db') as conn:
        print("Opened database successfully")

        # Try to drop the tables in case you already created it.

        try:
            conn.execute('DROP TABLE status_text')
        except:
            print('we cant drop the tables cause they are not exist !')
            pass


        conn.execute('CREATE TABLE status_text (status_id TEXT, status_text TEXT, comments TEXT)')

        print("Tables created successfully")

        conn.execute('CREATE UNIQUE INDEX idx_status_id_stat ON status_text (status_id)')

        print("Indexes created successfully")


def select(status_id: str, table: str, column: str) -> str:
    """
    Genetic select function

    :param status_id: Used to filter the table
    :param table: From table - comments, statuses
    :param column: Column to select
    :return: The value from DB or "" if didn't found
    """

    with sqlite3.connect("database.db") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select {} from {} where status_id = {}".format(column, table, status_id))
        rows = cur.fetchall()

    # We get only one row cause status_id is unique column

    if len(rows) > 0:
        return rows[0][column]

    return ""


def insert(status_id: str, status_text: str, comments: str) -> bool:
    """
    Genetic insert function

    :param status_id: Used to insert to the table
    :param table: Table to insert it - comments, statuses
    :param column:
    :param val:
    :return:
    """

    try:
        with sqlite3.connect("database.db") as con:

            cur = con.cursor()

            cur.execute("INSERT INTO status_text (status_id, status_text, comments) \
                         VALUES(?, ?, ?)",
                        (status_id, status_text, comments))

            con.commit()
    except:

        return False

    return True