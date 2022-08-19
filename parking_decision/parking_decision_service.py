import uvicorn
from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from parking_decision.business_processes.parking_decider_bp import ParkingDeciderBP

router = InferringRouter()


@cbv(router)
class ParkingDecisionService:

    @router.post("/get_parking_decision")
    def get_parking_decision(self, file):
        result = ParkingDeciderBP.construct().execute(file=file)
        return result


if __name__ == '__main__':
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")
