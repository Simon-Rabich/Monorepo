
from parking_decision.dals.decision_dal import DecisionDAL
from parking_decision.helpers.ocr_space_api import OCRSpaceAPi


class ParkingDeciderBP:

    def __init__(self, ocr_space_api: OCRSpaceAPi, decision_dal: DecisionDAL):
        self._ocr_space_api = ocr_space_api
        self._decision_dal = decision_dal

    def execute(self, file_name: str, file: bytes) -> bool:
        text_from_file: str = self._ocr_space_api.get_text_from_file(file_name=file_name, file=file)
        # decision = self._decide(text=text_from_file)
        # self._decision_dal.add_decision(decision=decision, text=text_from_file)
        # return decision
        return text_from_file

    @classmethod
    def _decide(cls, text: str):
        last_char = text[-1]
        before_last_char = text[-2]
        last_two_chars = last_char + before_last_char
        if last_two_chars in ('85', '86', '87', '88', '89', '00') or \
                len(text) == 7 and last_char in ("5", "0"):
            return False
        return True

    @classmethod
    def construct(cls, db_session) -> 'ParkingDeciderBP':
        ocr_space_api = OCRSpaceAPi
        decision_dal = DecisionDAL(db_session=db_session)
        return cls(ocr_space_api=ocr_space_api)
            #(decision_dal=decision_dal)
