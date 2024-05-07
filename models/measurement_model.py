from sqlalchemy import Column, Integer, String

from database import Base


class Measurement(Base):
    """
    Simple measurement table in database to store data in some format and give them to FE.
    In 'details' attribute we can put anything from the measurement that we want to display on FE.
    """
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    details = Column(String)
    timestamp = Column(String)
