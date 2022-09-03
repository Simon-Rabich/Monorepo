from parking_decision.db.models.decision import Decision


class DecisionDAL:

    def __init__(self, db_session):
        self._db_session = db_session

    def add_decision(self, decision: bool, text: str):
        self._db_session.add(Decision(decision=decision, text=text))

    def get_total_decline_vehicles_last_week(self):
        self._db_session.query(Decision.id).count()
