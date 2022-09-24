from unittest import TestCase
from unittest.mock import MagicMock

from parking_decision_srv.business_processes.parking_decider_bp import (
    ParkingDeciderBP,
)
from parking_decision_srv.busniess_components.check_plate_bc import CheckPlateBC
from parking_decision_srv.dals.decision_dal import DecisionDAL
from parking_decision_srv.helpers.ocr_space_api import OCRSpaceAPi


class TestParkingDeciderBP(TestCase):

    def setUp(self) -> None:
        self._ocr_space_api_mock = MagicMock(spec=OCRSpaceAPi)
        self._decision_dal_mock = MagicMock(spec=DecisionDAL)
        self._check_plate_bc_mock = MagicMock(spec=CheckPlateBC)
        self._parking_decision_bp = ParkingDeciderBP(ocr_space_api=self._ocr_space_api_mock,
                                                     decision_dal=self._decision_dal_mock,
                                                     check_plate_bc=self._check_plate_bc_mock)

    def test_execute(self):
        # Arrange
        self._file_name_mock = "_file_name_mock"
        self._file_mock: bytes = b"dummy_bytes"
        self._text_from_file_mock = "_text_from_file_mock"
        self._decision_mock = True
        self._ocr_space_api_mock.get_text_from_file.return_value = self._text_from_file_mock
        self._check_plate_bc_mock.execute.return_value = self._decision_mock
        # Act
        result: bool = self._parking_decision_bp.execute(file_name=self._file_name_mock, file=self._file_mock)
        # Assert
        self._ocr_space_api_mock.get_text_from_file.\
            assert_called_once_with(file_name=self._file_name_mock, file=self._file_mock)
        self._check_plate_bc_mock.execute.assert_called_once_with(text=self._text_from_file_mock)
        self._decision_dal_mock.add_decision.assert_called_once_with(decision=self._decision_mock,
                                                                     text=self._text_from_file_mock)
        self.assertEqual(result, self._decision_mock)
