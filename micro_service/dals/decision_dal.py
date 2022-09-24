from sqlalchemy.orm import Session

from micro_service.db.models.decision import Decision
from micro_service.db.parking_decision_db_session import ParkingDecisionDBSession
from micro_service.dals.base_decision_dal import BaseDecisionDAL


class DecisionDAL:

    @property
    def db_session(self) -> Session:
        return ParkingDecisionDBSession.get_session()

    def add_decision(self, decision: bool, text: str):
        self.db_session.add(Decision(decision=decision, text=text))

    def get_total_decline_vehicles_last_week(self):
        self.db_session.query(Decision.id).count()