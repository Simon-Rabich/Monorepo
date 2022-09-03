#!/usr/bin/env python3

from typing import List, Optional

from parking_decision.common.configurations.get_config import get_config
from parking_decision.db.models.decision import Decision
from parking_decision_service import ParkingDecisionService


import requests


class TestParkingDecisionService(TestBase):

    def setUp(self) -> None:
        super().setUp()

    def test_get_decision_parking_using_requests(self):
        pass

    def test_get_decision_parking_using_class(self):
        pass

    def test_pre_run(self):
        pass