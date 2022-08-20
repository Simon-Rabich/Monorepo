import sqlalchemy as db


def orm():
    engine = db.create_engine('sqlite:///shows.db')

    connection = engine.connect()

    metadata = db.MetaData()

    shows = db.Table('Shows', metadata, autoload=True, autoload_with=engine)

    query = db.select([shows])

    result_proxy = connection.execute(query)

    result_set = result_proxy.fetchall()

    print(result_set)


if __name__ == '__main__':
    a = orm()
    print(a)