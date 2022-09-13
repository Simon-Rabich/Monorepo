from contextvars import ContextVar
from typing import Dict, Optional

from sqlalchemy.orm import Session, sessionmaker

from parking_decision.db.get_engine import get_engine

_Session: Optional[sessionmaker] = None
_session: ContextVar[Optional[Session]] = ContextVar("_session", default=None)


class MissingSessionError(Exception):
    """Exception raised for when the user tries to access a database session before it is created."""

    def __init__(self):
        msg = """
        No session found! Either you are not currently in a request context,
        or you need to manually create a session context by using a `db` instance as
        a context manager e.g.:
        with db():
            db.session.query(User).all()
        """

        super().__init__(msg)


class SessionNotInitialisedError(Exception):
    """Exception raised when the user creates a new DB session without first initialising it."""

    def __init__(self):
        msg = """
        Session not initialised! Ensure that DBSessionMiddleware has been initialised before
        attempting database access.
        """

        super().__init__(msg)


class DBSessionMeta(type):
    # using this metaclass means that we can access db.session as a property at a class level,
    # rather than db().session
    @property
    def session(self) -> Session:
        """Return an instance of Session local to the current async context."""
        if _Session is None:
            raise SessionNotInitialisedError

        session = _session.get()
        if session is None:
            raise MissingSessionError

        return session


class DBSession(metaclass=DBSessionMeta):
    def __init__(self, session_args: Dict = None, commit_on_exit: bool = True):
        self.token = None
        self.session_args = session_args or {}
        self.commit_on_exit = commit_on_exit

    def __enter__(self) -> Session:
        global _Session
        if not isinstance(_Session, sessionmaker):
            _Session = sessionmaker(bind=get_engine())
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


ParkingDecisionDBSession: DBSessionMeta = DBSession
