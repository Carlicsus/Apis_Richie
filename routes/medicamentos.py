from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import config.db
import crud.medicamentos
import schemas.medicamentos
from portadortoken import Portador

medicamento_router = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@medicamento_router.get(
    "/medicamentos/",
    response_model=List[schemas.medicamentos.Medicamento],
    tags=["Medicamentos"],
    dependencies=[Depends(Portador())]
)
async def read_medicamentos(skip: Optional[int] = None, limit: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.medicamentos.get_medicamentos(db=db, skip=skip, limit=limit)

@medicamento_router.get(
    "/medicamento/{ID}",
    response_model=schemas.medicamentos.Medicamento,
    tags=["Medicamentos"],
    dependencies=[Depends(Portador())]
)
async def read_medicamento(ID: int, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.get_medicamento(db=db, medicamento_id=ID)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado")
    return db_medicamento

@medicamento_router.post(
    "/medicamentos/",
    response_model=schemas.medicamentos.Medicamento,
    tags=["Medicamentos"],
    dependencies=[Depends(Portador())]
)
def create_medicamento(medicamento: schemas.medicamentos.MedicamentoCreate, db: Session = Depends(get_db)):
    return crud.medicamentos.create_medicamento(db=db, medicamento=medicamento)

@medicamento_router.put(
    "/medicamento/{ID}",
    response_model=schemas.medicamentos.Medicamento,
    tags=["Medicamentos"],
    dependencies=[Depends(Portador())]
)
async def update_medicamento(ID: int, medicamento: schemas.medicamentos.MedicamentoUpdate, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.update_medicamento(db=db, medicamento_id=ID, medicamento=medicamento)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado, no actualizado")
    return db_medicamento

@medicamento_router.delete(
    "/medicamento/{ID}",
    response_model=schemas.medicamentos.Medicamento,
    tags=["Medicamentos"],
    dependencies=[Depends(Portador())]
)
async def delete_medicamento(ID: int, db: Session = Depends(get_db)):
    db_medicamento = crud.medicamentos.delete_medicamento(db=db, medicamento_id=ID)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento no encontrado, no eliminado")
    return db_medicamento
