import json
from typing import BinaryIO

import requests


class OCRSpaceAPi:

    def get_text_from_file(self, file_name: str, file: BinaryIO) -> str:
        payload = {'isOverlayRequired': False,
                   'apikey': "K82904764288957",
                   'language': "eng",
                   }
        r = requests.post('https://api.ocr.space/parse/image',
                          files={f"{file_name}": file},
                          data=payload,
                          )
        answer = json.loads(r.content.decode())
        print(answer)
        return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]
