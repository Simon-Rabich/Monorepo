import json
from unittest import TestCase

from micro_service.helpers.ocr_space_api import OCRSpaceAPi


class TestOcrSpaceAPI(TestCase):

    def setUp(self) -> None:
        self._ocr_space_api = OCRSpaceAPi()

    def test_api(self):
        file = '/parking-decision-service/micro_service/helpers/31d5L5y.jpeg'
        name = "31d5L5y.jpeg"
        result = self._ocr_space_api.get_text_from_file(file_name=name, file=file)
        print(result)
        return json.loads(result.content.decode())
