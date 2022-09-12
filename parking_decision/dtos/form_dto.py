from dataclasses import dataclass


@dataclass
class FormDTO:
    name: str
    form_fields: list
