from micro_service.db.basic_db_session import BasicDBSession

service: str = "a"

ParkingDecisionDBSession: BasicDBSession = BasicDBSession(service=service)
