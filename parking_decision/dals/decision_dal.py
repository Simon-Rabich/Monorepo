from parking_decision.db.database import SessionLocal
from parking_decision.db.models.decision import Decision


class DecisionDAL:

    def __init__(self, db_session):
        self._db_session = db_session

    def create_decision(self, decision: bool):
        self._db_session.add(Decision(decision=decision))

    @classmethod
    def construct(cls) -> 'DecisionDAL':
        with SessionLocal.begin() as db_session:
            return cls(db_session=db_session)
