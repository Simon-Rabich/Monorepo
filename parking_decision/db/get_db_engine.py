from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.future import Engine

from parking_decision.common.configurations.get_config import get_config

engine: Optional[Engine] = None


def get_db_engine():
    global engine
    if engine is None:
        url = get_config()['DB_URL']
        engine = create_engine(url=url, echo=True,  pool_pre_ping=True)
    return engine
