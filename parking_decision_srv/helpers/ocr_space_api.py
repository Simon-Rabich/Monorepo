import json

import requests


class OCRSpaceAPi:

    def get_text_from_file(self, file_name: str, file: bytes) -> str:
        payload = {'isOverlayRequired': False,
                   'apikey': "K82904764288957",
                   'language': "eng",
                   }
        r = requests.post('https://api.ocr.space/parse/image',
                          files={f"{file_name}": file},
                          data=payload,
                          )

        return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]
