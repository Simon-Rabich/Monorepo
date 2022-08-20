from typing import BinaryIO

from parking_decision.dals.decision_dal import DecisionDAL
from parking_decision.helpers.ocr_space_api import OCRSpaceAPi


class ParkingDeciderBP:

    def __init__(self, ocr_space_api: OCRSpaceAPi, decision_dal: DecisionDAL):
        self._ocr_space_api = ocr_space_api
        self._decision_dal = decision_dal

    def execute(self, file_name: str, file: bytes) -> str:
        text_from_file: str = self._ocr_space_api.get_text_from_file(file_name=file_name, file=file)

        # Rules

        self._decision_dal.create_decision(decision=True)

        return text_from_file


    @classmethod
    def construct(cls) -> 'ParkingDeciderBP':
        ocr_space_api = OCRSpaceAPi()
        decision_dal = DecisionDAL.construct()
        return cls(ocr_space_api=ocr_space_api,
                   decision_dal=decision_dal)
