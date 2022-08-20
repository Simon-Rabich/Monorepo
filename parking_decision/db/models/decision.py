from sqlalchemy import Boolean, Column, Integer

from ..database import Base


class Decision(Base):
    __tablename__ = 'decisions'

    id = Column(Integer, primary_key=True, index=True)
    decision = Column(Boolean, default=False)
