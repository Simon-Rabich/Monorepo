from parking_decision.db.get_engine import get_engine
from parking_decision.db.models import Base, DBSession


def set_db_schema():
    from parking_decision.db.models.decision import Decision

    engine = get_engine()
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
