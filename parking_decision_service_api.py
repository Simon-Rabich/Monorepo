from multiprocessing import Process
from time import sleep
from typing import Union

import uvicorn
from dill import dumps, loads
from fastapi import FastAPI, File
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from parking_decision.business_processes.parking_decider_bp import (
    ParkingDeciderBP,
)
from parking_decision.common.configurations.get_config import get_config
from parking_decision.db.parking_decision_db_session import (
    ParkingDecisionDBSession,
)

router = InferringRouter()


@cbv(router)
class ParkingDecisionService:

    # @router.get("/")
    # def read_root(self):
    #     return {"Hello": "World"}
    #
    # @router.get("/items/{item_id}")
    # def read_item(self, item_id: int, q: Union[str, None] = None):
    #     return {"item_id": item_id, "q": q}

    @router.post("/get_parking_decision")
    def get_parking_decision(self, file_name: str, file: Union[bytes, None] = File(default=None)):
        with ParkingDecisionDBSession() as pddb_session:
            result: bool = \
                ParkingDeciderBP.construct(db_session=pddb_session).execute(file_name=file_name, file=file)
        return result

    @classmethod
    def start(cls) -> Process:
        app = FastAPI()
        app.include_router(router)
        web_host = get_config()["WEB_HOST"]
        web_port = get_config()["WEB_PORT"]

        process = loads(dumps(Process(target=lambda: uvicorn.run(app, host=web_host,
                                                                 port=web_port, log_level="info"))))
        process.start()
        sleep(1)
        return process

        # uvicorn.run(app, host=get_config()["WEB_HOST"],
        #             port=get_config()["WEB_PORT"], log_level="info")



if __name__ == '__main__':
    ParkingDecisionService.start()
