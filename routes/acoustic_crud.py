from sqlalchemy.orm import Session

from models.measurement_model import Measurement
from schemas import MeasurementBase, MeasurementType


def create_acoustic_measurement(db: Session, measurement: MeasurementBase):
    db_measurement = Measurement(
        type=MeasurementType.acoustic.value,
        details=measurement.details,
        timestamp=measurement.timestamp)
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement


def get_acoustic_measurements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Measurement).filter(Measurement.type == MeasurementType.acoustic.value).offset(skip).limit(limit).all()