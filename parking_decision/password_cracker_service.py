#!/usr/bin/env python3
#    ___                      _
#   / __\   _ _ __ ___  _ __ | |_ ___  _ __ ___
#  / / | | | | '_ ` _ \| '_ \| __/ _ \| '_ ` _ \
# / /__| |_| | | | | | | |_) | || (_) | | | | | |
# \____/\__, |_| |_| |_| .__/ \__\___/|_| |_| |_|
#       |___/          |_|
#
# CYMPTOM LABS Copyright 2022. All rights reserved.
#
# Author: Naum Raviz (nraviz@tenable.com) on 01/08/2022

# STD packages
from multiprocessing import Process
from time import sleep
from typing import List

# External packages
import uvicorn
from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

# Internal packages
from apalib.base_service.base_service import BaseService
from apalib.base_service.exceptions_utils import throws
from apalib.configurations.get_config import get_config
from apalib.logging.get_logger import get_logger
from business_processes.fill_passwords_dictionary_bp import FillPasswordsDictionaryBP
from business_queries.get_cracked_passwords_bq import GetCrackedPasswordsBQ
from sdk.dtos.cracked_passwords import CrackedPasswords
from sdk.exceptions.exceptions import HashedPasswordsListTooBig, include_exceptions_in_app

router = InferringRouter()


@cbv(router)
class PasswordCrackerService(BaseService):

    @router.post("/get_cracked_passwords", response_model=CrackedPasswords)
    @throws(HashedPasswordsListTooBig)
    def get_cracked_passwords(self, hashed_passwords_to_crack: List[str]) -> CrackedPasswords:
        """
        Returns Cracked Passwords instance which describes if the cracking has succeeded for each given hashed password.
        """
        get_logger().info(f"{self.__class__.__name__}.{self.get_cracked_passwords.__name__} "
                          f"endpoint was called with hashed_passwords_to_crack: {hashed_passwords_to_crack}")
        result = GetCrackedPasswordsBQ.construct().execute(hashed_passwords=hashed_passwords_to_crack)
        get_logger().info(f"{self.__class__.__name__}.{self.get_cracked_passwords.__name__} endpoint return {result}")
        return result

    @classmethod
    def start(cls) -> Process:
        app = FastAPI()
        include_exceptions_in_app(app=app)
        app.include_router(router)
        process = Process(target=lambda: uvicorn.run(app, host=get_config()["HOST_IP_WEB_SERVICE"],
                                                     port=get_config()["HOST_PORT_WEB_SERVICE"], log_level="info"))
        process.start()
        sleep(1)
        return process

    @classmethod
    def pre_run(cls):
        FillPasswordsDictionaryBP.construct().execute()


if __name__ == '__main__':
    PasswordCrackerService.run()
