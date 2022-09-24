from sqlalchemy.orm import Session
from micro_service.db.parking_decision_db_session import ParkingDecisionDBSession


class BaseDecisionDAL:

    @property
    def db_session(self) -> Session:
        return ParkingDecisionDBSession.get_session()
