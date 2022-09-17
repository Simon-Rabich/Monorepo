# 1. Standard library imports.
from contextvars import ContextVar
from typing import Dict, Optional

# 2. Related third party imports.
from sqlalchemy.orm.session import Session, sessionmaker

# 3. Local application/library specific imports.
from parking_decision.db.get_db_engine import get_db_engine

_Session: Optional[sessionmaker] = None
_session: ContextVar[Optional[Session]] = ContextVar("_session", default=None)


class MissingSessionError(Exception):
    """Exception raised for when the user tries to access a database sessions before it is created."""

    def __init__(self):
        msg = """
        No sessions found! Either you are not currently in a request context,
        or you need to manually create a sessions context by using a `sqlalchemy.orm.sessions.Session` instance as
        a context manager e.g.:
        with Session():
            Session.sessions.query(DnssUser).all()
        """

        super().__init__(msg)


class SessionNotInitialisedError(Exception):
    """Exception raised when the user creates a new DB sessions without first initialising it."""

    def __init__(self):
        msg = """
        Session not initialised! Ensure that DBSessionMiddleware has been initialised before
        attempting database access.
        """

        super().__init__(msg)


class DBSessionMeta(type):
    # using this metaclass means that we can access sa.sessions as a property at a class level,
    # rather than sa().sessions
    @property
    def session(self) -> Session:
        """Return an instance of Session local to the current async context."""
        if _Session is None:
            raise SessionNotInitialisedError

        session = _session.get()
        if session is None:
            raise MissingSessionError

        return session


class BasicDBSession(metaclass=DBSessionMeta):
    def __init__(self, service: str, session_args: Dict = None, commit_on_exit: bool = True):
        self.token = None
        self.session_args = session_args or {}
        self.commit_on_exit = commit_on_exit
        self.__service = service

    def __enter__(self) -> Session:
        global _Session
        if not isinstance(_Session, sessionmaker):
            _Session = sessionmaker(bind=get_db_engine(service=self.__service))
        self.token = _session.set(_Session(**self.session_args))
        return type(self).session

    def __exit__(self, exc_type, exc_value, traceback):
        sess = _session.get()
        if exc_type is not None:
            sess.rollback()

        if self.commit_on_exit:
            sess.commit()

        sess.close()
        _session.reset(self.token)

    def get_session(self) -> Session:
        return type(self).session

# ParkingDecisionDBSession: DBSessionMeta = DBSession
