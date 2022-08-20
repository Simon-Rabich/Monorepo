from typing import BinaryIO

from parking_decision.helpers.ocr_space_api import OCRSpaceAPi


class ParkingDeciderBP:

    def __init__(self, ocr_space_api: OCRSpaceAPi):
        self._ocr_space_api = ocr_space_api

    def execute(self, file_name: str, file: bytes) -> str:
        text_from_file: str = self._ocr_space_api.get_text_from_file(file_name=file_name, file=file)

        # Rules


        # Write using the dal the result of the rules

        return text_from_file


    @classmethod
    def construct(cls) -> 'ParkingDeciderBP':
        ocr_space_api = OCRSpaceAPi()
        return cls(ocr_space_api=ocr_space_api)
