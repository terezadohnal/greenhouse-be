from sqlalchemy.orm import Session
import schemas
from models import camera_model

def get_camera(db: Session, camera_id: int):
    return db.query(camera_model.Camera).filter(camera_model.Camera.id == camera_id).first()

def get_cameras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(camera_model.Camera).offset(skip).limit(limit).all()

def create_camera(db: Session, camera: schemas.CameraBase):
    db_camera = camera_model.Camera(camera_name=camera.camera_name, sampling_frequency=camera.sampling_frequency, images_count=camera.images_count, camera_activation=camera.camera_activation, measurement_duration=camera.measurement_duration)
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera

def update_camera(db: Session, camera_id: int, camera: schemas.CameraBase):
    db_camera = db.query(camera_model.Camera).filter(camera_model.Camera.id == camera_id).first()
    db_camera.camera_name = camera.camera_name
    db_camera.sampling_frequency = camera.sampling_frequency
    db_camera.images_count = camera.images_count
    db_camera.camera_activation = camera.camera_activation
    db_camera.measurement_duration = camera.measurement_duration
    db.commit()
    db.refresh(db_camera)
    return db_camera

def delete_camera(db: Session, camera_id: int):
    db_camera = db.query(camera_model.Camera).filter(camera_model.Camera.id == camera_id).first()
    db.delete(db_camera)
    db.commit()
    return db_camera