from sqlalchemy.orm import Session

from models.receta import Receta
from schemas.receta import RecetaCreate, RecetaUpdate


def get_receta(db: Session, receta_id: int):
    return db.query(Receta).filter(Receta.ID == receta_id).first()

def get_recetas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Receta).offset(skip).limit(limit).all()

def create_receta(db: Session, receta: RecetaCreate):
    db_receta = Receta(**receta.dict())
    db.add(db_receta)
    db.commit()
    db.refresh(db_receta)
    return db_receta

def update_receta(db: Session, receta_id: int, receta: RecetaUpdate):
    db_receta = db.query(Receta).filter(Receta.ID == receta_id).first()
    if db_receta:
        for var, value in vars(receta).items():
            if value is not None:
                setattr(db_receta, var, value)
        db.commit()
        db.refresh(db_receta)
    return db_receta

def delete_receta(db: Session, receta_id: int):
    db_receta = db.query(Receta).filter(Receta.ID == receta_id).first()
    if db_receta:
        db.delete(db_receta)
        db.commit()
    return db_receta
