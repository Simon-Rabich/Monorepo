# from fastapi_utils.session import get_engine

from parking_decision_srv.db.get_db_engine import get_db_engine
from parking_decision_srv.db.models import Base, DBSession


def setup_db_schema():

    engine = get_db_engine()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    setup_db_schema()
