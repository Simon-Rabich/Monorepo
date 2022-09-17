import datetime

from sqlalchemy import Boolean, Column, Date, Integer, String

from parking_decision.db.models import Base


class Decision(Base):
    __tablename__ = "decision"
    id = Column(Integer, primary_key=True, index=True)
    decision = Column(Boolean, default=False)
    text = Column(String)
    timestamp = Column(Date, default=datetime.datetime.now())

    def __init__(self, decision, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decision = decision
        self.text = text

    def __repr__(self):
        return f"decision={self.decision!r} && text={self.text!r} && timestamp={self.timestamp!r}"
