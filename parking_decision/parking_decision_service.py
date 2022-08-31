from typing import Union
from parking_decision.db.set_db_schema import set_db_schema

from parking_decision.business_processes.parking_decider_bp import ParkingDeciderBP

import uvicorn
from fastapi import FastAPI, File
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from parking_decision.db.parking_decision_db_session import ParkingDecisionDBSession

router = InferringRouter()


@cbv(router)
class ParkingDecisionService:

    @router.post("/get_parking_decision")
    def get_parking_decision(self, file_name: str, file: Union[bytes, None] = File(default=None)):
        with ParkingDecisionDBSession() as pddb_session:
            result: bool = \
                ParkingDeciderBP.construct(db_session=pddb_session).execute(file_name=file_name, file=file)
        return result


if __name__ == '__main__':
    set_db_schema()
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")