from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


DBSession = scoped_session(sessionmaker())
Base = declarative_base()
