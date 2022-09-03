from parking_decision.dals.decision_dal import DecisionDAL
from parking_decision.db.migrations.setup_db_schema import set_db_schema
from parking_decision.db.parking_decision_db_session import ParkingDecisionDBSession

if __name__ == '__main__':

    set_db_schema()
    with ParkingDecisionDBSession() as pddb_session:
        dal = DecisionDAL(db_session=pddb_session)
        dal.add_decision(decision=False, text="fdssssssccccgjh")
