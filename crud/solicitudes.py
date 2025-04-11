from sqlalchemy.orm import Session
from models.solicitudes import Solicitud
from schemas.solicitudes import SolicitudCreate, SolicitudUpdate

def create_solicitud(db: Session, solicitud: SolicitudCreate):
    db_solicitud = Solicitud(**solicitud.dict())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud

def get_solicitud(db: Session, solicitud_id: int):
    return db.query(Solicitud).filter(Solicitud.ID == solicitud_id).first()

def get_solicitudes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Solicitud).offset(skip).limit(limit).all()

def update_solicitud(db: Session, solicitud_id: int, solicitud: SolicitudUpdate):
    db_solicitud = db.query(Solicitud).filter(Solicitud.ID == solicitud_id).first()
    if db_solicitud:
        for key, value in solicitud.dict(exclude_unset=True).items():
            setattr(db_solicitud, key, value)
        db.commit()
        db.refresh(db_solicitud)
    return db_solicitud

def delete_solicitud(db: Session, solicitud_id: int):
    db_solicitud = db.query(Solicitud).filter(Solicitud.ID == solicitud_id).first()
    if db_solicitud:
        db.delete(db_solicitud)
        db.commit()
    return db_solicitud
