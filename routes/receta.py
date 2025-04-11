from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import config.db
import crud.receta
import schemas.receta
from portadortoken import Portador

receta_router = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@receta_router.get(
    "/recetas/",
    response_model=List[schemas.receta.Receta],
    tags=["Recetas Médicas"],
    dependencies=[Depends(Portador())]
)
async def read_recetas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.receta.get_recetas(db=db, skip=skip, limit=limit)

@receta_router.get(
    "/receta/{id}",
    response_model=schemas.receta.Receta,
    tags=["Recetas Médicas"],
    dependencies=[Depends(Portador())]
)
async def read_receta(id: int, db: Session = Depends(get_db)):
    db_receta = crud.receta.get_receta(db=db, receta_id=id)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return db_receta

@receta_router.post(
    "/recetas/",
    response_model=schemas.receta.Receta,
    tags=["Recetas Médicas"],
    dependencies=[Depends(Portador())]
)
def create_receta(receta: schemas.receta.RecetaCreate, db: Session = Depends(get_db)):
    return crud.receta.create_receta(db=db, receta=receta)

@receta_router.put(
    "/receta/{id}",
    response_model=schemas.receta.Receta,
    tags=["Recetas Médicas"],
    dependencies=[Depends(Portador())]
)
async def update_receta(id: int, receta: schemas.receta.RecetaUpdate, db: Session = Depends(get_db)):
    db_receta = crud.receta.update_receta(db=db, receta_id=id, receta=receta)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Receta no encontrada, no actualizada")
    return db_receta

@receta_router.delete(
    "/receta/{id}",
    response_model=schemas.receta.Receta,
    tags=["Recetas Médicas"],
    dependencies=[Depends(Portador())]
)
async def delete_receta(id: int, db: Session = Depends(get_db)):
    db_receta = crud.receta.delete_receta(db=db, receta_id=id)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Receta no encontrada, no eliminada")
    return db_receta
