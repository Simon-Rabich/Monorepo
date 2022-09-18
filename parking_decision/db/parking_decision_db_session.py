from parking_decision.db.basic_db_session import BasicDBSession

service: str = "a"

ParkingDecisionDBSession: BasicDBSession = BasicDBSession(service=service)
