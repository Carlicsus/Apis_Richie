from sqlalchemy.orm import Session
from datetime import datetime
from models.lotes_medicamentos import LoteMedicamento  # Modelo SQLAlchemy
from schemas.lotes import LoteMedicamentoCreate, LoteMedicamentoUpdate
from schemas.lotes import LoteMedicamento as LoteMedicamentoSchema  # Schema Pydantic
from typing import List


# 📌 Crear un lote en MySQL
def create_lote(db: Session, lote_data: LoteMedicamentoCreate):
    db_lote = LoteMedicamento(
        Medicamento_ID=lote_data.Medicamento_ID,
        PersonalMedico_ID=lote_data.PersonalMedico_ID,
        Clave=lote_data.Clave,
        Estatus=lote_data.Estatus,
        Costo_Total=lote_data.Costo_Total,
        Cantidad=lote_data.Cantidad,
        Ubicacion=lote_data.Ubicacion,
        Fecha_registro=datetime.utcnow()
    )
    
    db.add(db_lote)
    db.commit()
    db.refresh(db_lote)
    
    return db_lote


# 📌 Obtener un lote desde MySQL
def get_lote(db: Session, lote_id: int):
    db_lote = db.query(LoteMedicamento).filter(LoteMedicamento.ID == lote_id).first()
    
    if db_lote:
        return LoteMedicamentoSchema(
            ID=db_lote.ID,
            Medicamento_ID=db_lote.Medicamento_ID,
            PersonalMedico_ID=db_lote.PersonalMedico_ID,
            Clave=db_lote.Clave,
            Estatus=db_lote.Estatus,
            Costo_Total=db_lote.Costo_Total,
            Cantidad=db_lote.Cantidad,
            Ubicacion=db_lote.Ubicacion,
            Fecha_registro=db_lote.Fecha_registro,
            Fecha_actualizacion=db_lote.Fecha_actualizacion
        )
    
    return None


# 📌 Obtener lista de lotes desde MySQL
def get_lotes(db: Session, skip: int = 0, limit: int = 10):
    db_lotes = db.query(LoteMedicamento).offset(skip).limit(limit).all()

    return [
        LoteMedicamentoSchema(
            ID=lote.ID,
            Medicamento_ID=lote.Medicamento_ID,
            PersonalMedico_ID=lote.PersonalMedico_ID,
            Clave=lote.Clave,
            Estatus=lote.Estatus,
            Costo_Total=lote.Costo_Total,
            Cantidad=lote.Cantidad,
            Ubicacion=lote.Ubicacion,
            Fecha_registro=lote.Fecha_registro,
            Fecha_actualizacion=lote.Fecha_actualizacion
        )
        for lote in db_lotes
    ]


# 📌 Actualizar un lote en MySQL
def update_lote(db: Session, lote_id: int, lote_data: LoteMedicamentoUpdate):
    db_lote = db.query(LoteMedicamento).filter(LoteMedicamento.ID == lote_id).first()
    if not db_lote:
        return None

    update_data = lote_data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_lote, key, value)
    db_lote.Fecha_actualizacion = datetime.utcnow()
    
    db.commit()
    db.refresh(db_lote)

    return db_lote


# 📌 Eliminar un lote en MySQL
def delete_lote(db: Session, lote_id: int):
    db_lote = db.query(LoteMedicamento).filter(LoteMedicamento.ID == lote_id).first()
    if not db_lote:
        return None

    db.delete(db_lote)
    db.commit()

    return db_lote
