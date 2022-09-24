
from micro_service.busniess_components.check_plate_bc import CheckPlateBC
from micro_service.dals.decision_dal import DecisionDAL
from micro_service.helpers.ocr_space_api import OCRSpaceAPi


class ParkingDeciderBP:

    def __init__(self, ocr_space_api: OCRSpaceAPi,
                 decision_dal: DecisionDAL,
                 check_plate_bc: CheckPlateBC):
        self._ocr_space_api = ocr_space_api
        self._decision_dal = decision_dal
        self._check_plate_bc = check_plate_bc

    def execute(self, file_name: str, file: bytes) -> bool:
        text_from_file: str = self._ocr_space_api.get_text_from_file(file_name=file_name, file=file)
        decision = self._check_plate_bc.execute(text=text_from_file)
        self._decision_dal.add_decision(decision=decision, text=text_from_file)
        return decision

    @classmethod
    def construct(cls) -> 'ParkingDeciderBP':
        ocr_space_api = OCRSpaceAPi()
        decision_dal = DecisionDAL()
        check_plate_bc = CheckPlateBC()
        return cls(ocr_space_api=ocr_space_api,
                   decision_dal=decision_dal,
                   check_plate_bc=check_plate_bc)
