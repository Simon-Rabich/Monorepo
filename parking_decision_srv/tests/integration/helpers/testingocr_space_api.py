import json
from unittest import TestCase

from parking_decision_srv.helpers.ocr_space_api import OCRSpaceAPi


class TestOcrSpaceAPI(TestCase):

    def setUp(self) -> None:
        self._ocr_space_api = OCRSpaceAPi()

    def test_api(self):
        file = '/parking-decision-service/parking_decision_srv/helpers/31d5L5y.jpeg'
        name = "31d5L5y.jpeg"
        result = self._ocr_space_api.get_text_from_file(file_name=name, file=file)
        print(result)
        return json.loads(result.content.decode())
