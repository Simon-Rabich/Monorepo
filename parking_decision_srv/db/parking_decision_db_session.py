from parking_decision_srv.db.basic_db_session import BasicDBSession

service: str = "a"

ParkingDecisionDBSession: BasicDBSession = BasicDBSession(service=service)
