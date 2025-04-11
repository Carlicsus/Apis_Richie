from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import config.db
import crud.dispensaciones
import schemas.dispensaciones
from portadortoken import Portador

dispensacion_router = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@dispensacion_router.get(
    "/dispensaciones/",
    response_model=List[schemas.dispensaciones.Dispensacion],
    tags=["Dispensaciones"],
    dependencies=[Depends(Portador())]
)
async def read_dispensaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.dispensaciones.get_dispensaciones(db=db, skip=skip, limit=limit)

@dispensacion_router.get(
    "/dispensacion/{id}",
    response_model=schemas.dispensaciones.Dispensacion,
    tags=["Dispensaciones"],
    dependencies=[Depends(Portador())]
)
async def read_dispensacion(id: int, db: Session = Depends(get_db)):
    db_dispensacion = crud.dispensaciones.get_dispensacion(db=db, dispensacion_id=id)
    if db_dispensacion is None:
        raise HTTPException(status_code=404, detail="Dispensación no encontrada")
    return db_dispensacion

@dispensacion_router.post(
    "/dispensaciones/",
    response_model=schemas.dispensaciones.Dispensacion,
    tags=["Dispensaciones"],
    dependencies=[Depends(Portador())]
)
def create_dispensacion(dispensacion: schemas.dispensaciones.DispensacionCreate, db: Session = Depends(get_db)):
    return crud.dispensaciones.create_dispensacion(db=db, dispensacion=dispensacion)

@dispensacion_router.put(
    "/dispensacion/{id}",
    response_model=schemas.dispensaciones.Dispensacion,
    tags=["Dispensaciones"],
    dependencies=[Depends(Portador())]
)
async def update_dispensacion(id: int, dispensacion: schemas.dispensaciones.DispensacionUpdate, db: Session = Depends(get_db)):
    db_dispensacion = crud.dispensaciones.update_dispensacion(db=db, dispensacion_id=id, dispensacion=dispensacion)
    if db_dispensacion is None:
        raise HTTPException(status_code=404, detail="Dispensación no encontrada, no actualizada")
    return db_dispensacion

@dispensacion_router.delete(
    "/dispensacion/{id}",
    response_model=schemas.dispensaciones.Dispensacion,
    tags=["Dispensaciones"],
    dependencies=[Depends(Portador())]
)
async def delete_dispensacion(id: int, db: Session = Depends(get_db)):
    db_dispensacion = crud.dispensaciones.delete_dispensacion(db=db, dispensacion_id=id)
    if db_dispensacion is None:
        raise HTTPException(status_code=404, detail="Dispensación no encontrada, no eliminada")
    return db_dispensacion
