from parking_decision.db.get_engine import get_engine
from parking_decision.db.models import Base, DBSession


def setup_db_schema():

    engine = get_engine()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    setup_db_schema()
