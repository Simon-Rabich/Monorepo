from sqlalchemy.orm import Session

from parking_decision.db.models.decision import Decision
from parking_decision.db.parking_decision_db_session import ParkingDecisionDBSession
from parking_decision.dals.base_decision_dal import BaseDecisionDAL


class DecisionDAL:

    @property
    def db_session(self) -> Session:
        return ParkingDecisionDBSession.get_session()

    def add_decision(self, decision: bool, text: str):
        self.db_session.add(Decision(decision=decision, text=text))

    def get_total_decline_vehicles_last_week(self):
        self.db_session.query(Decision.id).count()
