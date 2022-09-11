# Python Imports
import array
from dataclasses import dataclass
# Third parties imports

# Local imports


@dataclass
class FormDTO:
    name: str
    form_fields: list
