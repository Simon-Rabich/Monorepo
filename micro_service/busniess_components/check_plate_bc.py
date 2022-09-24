from typing import Tuple


class CheckPlateBC:

    INVALID_LAST_TWO_CHARS: Tuple[str] = \
        ('85', '86', '87', '88', '89', '00')

    def execute(self, text: str) -> bool:
        last_char = text[-1]
        before_last_char = text[-2]
        last_two_chars = before_last_char + last_char
        if last_two_chars in self.INVALID_LAST_TWO_CHARS or \
                len(text) == 7 and last_char in ("5", "0"):
            return False
        return True
