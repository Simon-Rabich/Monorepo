from typing import Dict

import requests


class ParkingDecisionServiceClient:
    HOST_URL: str = "http://0.0.0.0:8001/"
    # f"{self.protocol}://{self.server}:{self.port}/{self.root_url}"
    DEFAULT_HEADER: Dict[str, str] = {'accept': 'application/json'}

    def health_check(self) -> None:
        return requests.get(url=f'{self.HOST_URL}{ParkingDecisionServiceClient.health_check.__name__}',
                            headers=self.DEFAULT_HEADER).json()

    def read_root(self) -> None:
        return requests.get(url=f'{self.HOST_URL}{ParkingDecisionServiceClient.read_root.__name__}',
                            headers=self.DEFAULT_HEADER).json()

    def read_item(self) -> None:
        return requests.get(url=f'{self.HOST_URL}{"items/6?q=hello"}',
                            headers=self.DEFAULT_HEADER).json()


if __name__ == '__main__':
    print(ParkingDecisionServiceClient().health_check())
    print(ParkingDecisionServiceClient().read_root())
    print(ParkingDecisionServiceClient().read_item())
