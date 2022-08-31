from typing import Optional

from sqlalchemy.future import Engine

from parking_decision.common.configurations.get_config import get_config
from sqlalchemy import create_engine

engine: Optional[Engine] = None


def get_engine():
    global engine
    if engine is None:
        url = get_config()['DB_URL']
        engine = create_engine(url=url, echo=True)
    return engine
