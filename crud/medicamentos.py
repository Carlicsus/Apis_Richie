from sqlalchemy.orm import Session

from models.medicamentos import Medicamento
from schemas.medicamentos import MedicamentoCreate, MedicamentoUpdate


def get_medicamento(db: Session, medicamento_id: int):
    return db.query(Medicamento).filter(Medicamento.ID == medicamento_id).first()

def get_medicamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Medicamento).offset(skip).limit(limit).all()

def create_medicamento(db: Session, medicamento: MedicamentoCreate):
    db_medicamento = Medicamento(**medicamento.dict())
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento

def update_medicamento(db: Session, medicamento_id: int, medicamento: MedicamentoUpdate):
    db_medicamento = db.query(Medicamento).filter(Medicamento.ID == medicamento_id).first()
    if db_medicamento:
        for var, value in vars(medicamento).items():
            if value is not None:
                setattr(db_medicamento, var, value)
        db.commit()
        db.refresh(db_medicamento)
    return db_medicamento

def delete_medicamento(db: Session, medicamento_id: int):
    db_medicamento = db.query(Medicamento).filter(Medicamento.ID == medicamento_id).first()
    if db_medicamento:
        db.delete(db_medicamento)
        db.commit()
    return db_medicamento
