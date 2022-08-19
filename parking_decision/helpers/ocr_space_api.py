import json
from typing import BinaryIO

import requests


class OCRSpaceAPi:

    def get_text_from_file(self, file: BinaryIO) -> str:
        payload = {'isOverlayRequired': False,
                   'apikey': "K82904764288957",
                   'language': "eng",
                   }
        r = requests.post('https://api.ocr.space/parse/image',
                          files={"filename": file},
                          data=payload,
                          )

        return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]

if __name__ == '__main__':
    file = open("31d5L5y.jpeg", "rb")
    print(OCRSpaceAPi().get_text_from_file(file=file))

