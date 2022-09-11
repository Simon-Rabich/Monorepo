#!/usr/bin/env python3

class ParkingDecisionException(Exception):
    """Base class for other exceptions"""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class DBInteractionException(ParkingDecisionException):
    pass
