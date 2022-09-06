#!/usr/bin/env python3
import json
import multiprocessing
from os import kill
from signal import SIGKILL

import requests
from unittest import TestCase

from parking_decision.common.configurations.get_config import get_config
from parking_decision.db.migrations.setup_db_schema import setup_db_schema
from parking_decision_service import ParkingDecisionService


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
        payload = {'file': '/parking-decision-service/parking_decision/helpers/31d5L5y.jpeg',
                   'name': "31d5L5y.jpeg"}
        # Act
        decision_result = requests.post(f'http://{get_config()["WEB_HOST"]}:{get_config()["WEB_PORT"]}/get_decision_parking',
                                        data=payload)

        # Assert
        self.assertTrue(json.loads(decision_result.content.decode()))
