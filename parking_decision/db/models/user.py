from sqlalchemy import Column, Integer, String

from parking_decision.db.models import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    def __init__(self, name, fullname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.fullname = fullname
