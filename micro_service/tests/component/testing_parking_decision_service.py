#!/usr/bin/env python3
import json
import multiprocessing
from os import kill
from signal import SIGKILL
from unittest import TestCase

import requests

from micro_service.common.configurations.get_config import get_config
from micro_service.db.migrations.setup_db_schema import setup_db_schema
from parking_decision_service_api import ParkingDecisionService


class TestParkingDecisionService(TestCase):

    service_process: multiprocessing.Process

    @classmethod
    def setUpClass(cls) -> None:
        cls.service_process: multiprocessing.Process = ParkingDecisionService.run()

    @classmethod
    def tearDownClass(cls) -> None:
        kill(cls.service_process.pid, SIGKILL)
        cls.service_process.join()

    def setUp(self) -> None:
        setup_db_schema()

    def test_get_decision_parking_using_requests(self):
        # Arrange
        payload = {'file': '/parking-decision-service/micro_service/helpers/31d5L5y.jpeg',
                   'name': "31d5L5y.jpeg"}
        # Act
        decision_result = requests.post(f'http://{get_config()["WEB_HOST"]}:{get_config()["WEB_PORT"]}/get_decision_parking',
                                        data=payload)

        # Assert
        self.assertTrue(json.loads(decision_result.content.decode()))
