from typing import Union

from sqlalchemy.orm import Session

from parking_decision.business_processes.parking_decider_bp import ParkingDeciderBP

import uvicorn
from fastapi import FastAPI, File, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from parking_decision.db.database import SessionLocal, Base, engine


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = InferringRouter()


@cbv(router)
class ParkingDecisionService:

    @router.post("/get_parking_decision")
    def get_parking_decision(self, file_name: str, file: Union[bytes, None] = File(default=None),
                             db: Session = Depends(get_db)):
        result = ParkingDeciderBP.construct().execute(file_name=file_name, file=file)
        return result


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")
