from multiprocessing import Process

# from multiprocessing.process import AuthenticationString
from time import sleep
from typing import Union

import uvicorn
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

    @router.get("/read_root")
    def read_root(self):
        return {"Hello": "World"}

    @router.get("/items/{item_id}")
    def read_item(self, item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

    @router.get("/health_check")
    def health_check(self):
        """Endpoint for health checks"""
        return {"statusCode": 200, "message": "Service is healthy"}

    @router.post("/get_parking_decision")
    def get_parking_decision(self, file_name: str, file: Union[bytes, None] = File(default=None)):
        with ParkingDecisionDBSession:
            result: bool = \
                ParkingDeciderBP.construct().execute(file_name=file_name, file=file)
        return result


    # global process variable
    proc = None

    @classmethod
    def run(cls):
        """
        This function to run configured uvicorn server.
        """
        app = FastAPI()
        app.include_router(router)
        web_host = get_config()["WEB_HOST"]
        web_port = get_config()["WEB_PORT"]
        uvicorn.run(app=app, host=web_host,
                    port=web_port, log_level="info")

        # process = Process(target=lambda: uvicorn.run(app, host=web_host, port=web_port, log_level="info"))
        # serialize_process = loads(dumps(process))
        # process.start()
        # sleep(1)
        # return process

    @classmethod
    def start(cls) -> Process:
        """
        This function to start a new process (start the server).
        """
        global proc
        # create process instance and set the target to run function.
        # use daemon mode to stop the process whenever the program stopped.
        proc = Process(target=ParkingDecisionService.run(), args=(), daemon=True)
        proc.start()

    @classmethod
    def stop(cls):
        """
        This function to join (stop) the process (stop the server).
        """
        global proc
        # check if the process is not None
        if proc:
            # join (stop) the process with a timeout setten to 0.25 seconds.
            # using timeout (the optional arg) is too important in order to
            # enforce the server to stop.
            proc.join(0.25)


if __name__ == '__main__':
    ParkingDecisionService.start()
    sleep(1)
    ParkingDecisionService.stop()
