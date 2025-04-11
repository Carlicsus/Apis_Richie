from sqlalchemy.orm import Session

from models.dispensaciones import Dispensacion
from schemas.dispensaciones import DispensacionCreate, DispensacionUpdate


def get_dispensacion(db: Session, dispensacion_id: int):
    return db.query(Dispensacion).filter(Dispensacion.ID == dispensacion_id).first()

def get_dispensaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Dispensacion).offset(skip).limit(limit).all()

def create_dispensacion(db: Session, dispensacion: DispensacionCreate):
    db_dispensacion = Dispensacion(**dispensacion.dict())
    db.add(db_dispensacion)
    db.commit()
    db.refresh(db_dispensacion)
    return db_dispensacion

def update_dispensacion(db: Session, dispensacion_id: int, dispensacion: DispensacionUpdate):
    db_dispensacion = db.query(Dispensacion).filter(Dispensacion.ID == dispensacion_id).first()
    if db_dispensacion:
        for var, value in vars(dispensacion).items():
            if value is not None:
                setattr(db_dispensacion, var, value)
        db.commit()
        db.refresh(db_dispensacion)
    return db_dispensacion

def delete_dispensacion(db: Session, dispensacion_id: int):
    db_dispensacion = db.query(Dispensacion).filter(Dispensacion.ID == dispensacion_id).first()
    if db_dispensacion:
        db.delete(db_dispensacion)
        db.commit()
    return db_dispensacion
