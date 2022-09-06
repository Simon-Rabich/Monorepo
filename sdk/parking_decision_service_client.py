
from typing import Dict

import requests


class ParkingDecisionServiceClient:
    HOST_URL: str = "http://0.0.0.0:8001/"
    # f"{self.protocol}://{self.server}:{self.port}/{self.root_url}"
    DEFAULT_HEADERS: Dict[str, str] = {'accept': 'application/json'}

    def health_check(self) -> None:
        return requests.post(url=f'{self.HOST_URL}{ParkingDecisionServiceClient.health_check.__name__}',
                             headers=self.DEFAULT_HEADERS).json()


if __name__ == '__main__':
    ParkingDecisionServiceClient().health_check()
