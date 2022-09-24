from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from .item import Item
from .user import User

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

