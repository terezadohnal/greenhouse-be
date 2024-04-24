from sqlalchemy import Column, Integer, String

from database import Base

class Camera(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True)
    camera_name = Column(String, unique=True)
    sampling_frequency = Column(Integer)
    images_count= Column(Integer)
    camera_activation= Column(Integer)
    measurement_duration= Column(Integer)


