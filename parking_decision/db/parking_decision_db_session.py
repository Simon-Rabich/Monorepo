from parking_decision.db.basic_db_session import BasicDBSession

service: str = ""

ParkingDecisionDBSession: BasicDBSession = BasicDBSession(service=service)
