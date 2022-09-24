from typing import Optional
from unittest import TestCase

from micro_service.dals.decision_dal import DecisionDAL
from micro_service.db.migrations.setup_db_schema import setup_db_schema
from micro_service.db.models.decision import Decision
from micro_service.db.parking_decision_db_session import (
    ParkingDecisionDBSession,
)


class TestDecisionDAL(TestCase):

    def setUp(self) -> None:
        setup_db_schema()
        self._dal = DecisionDAL

    def test_add_decision(self):
        # Arrange
        decision_mock = True
        text_mock = "text_mock"
        # Act
        with ParkingDecisionDBSession() as pddb_session:
            dal = self._dal(db_session=pddb_session)
            dal.add_decision(decision=decision_mock, text=text_mock)
        # Assert
        with ParkingDecisionDBSession() as pddb_session:
            result: Optional[Decision] = pddb_session.query(Decision).one_or_none()
            self.assertTrue(result is not None)
            self.assertEqual(decision_mock, result.decision)
            self.assertEqual(text_mock, result.text)
