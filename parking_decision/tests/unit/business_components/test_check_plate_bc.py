from unittest import TestCase

from parking_decision.busniess_components.check_plate_bc import CheckPlateBC


class TestCheckPlateBC(TestCase):

    def setUp(self) -> None:
        self._check_plate_bc = CheckPlateBC()

    def test_execute(self):
        # Arrange
        valid_number_plate = "121"
        # Act
        result: bool = self._check_plate_bc.execute(text=valid_number_plate)
        # Assert
        self.assertTrue(result)

    def test_execute__when_invalid_number_plate__should_return_false(self):
        # Arrange
        invalid_number_plate: str = CheckPlateBC.INVALID_LAST_TWO_CHARS[0]
        # Act
        result: bool = self._check_plate_bc.execute(text=invalid_number_plate)
        # Assert
        self.assertFalse(result)

    def test_execute__when_invalid_number_plate_len_7__should_return_false(self):
        # Arrange
        invalid_number_plate: str = "1234560"
        # Act
        result: bool = self._check_plate_bc.execute(text=invalid_number_plate)
        # Assert
        self.assertFalse(result)
