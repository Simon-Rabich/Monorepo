from sqlalchemy.orm import Session
from parking_decision.db.parking_decision_db_session import ParkingDecisionDBSession


class BaseDecisionDAL:

    @property
    def db_session(self) -> Session:
        return ParkingDecisionDBSession.get_session()
