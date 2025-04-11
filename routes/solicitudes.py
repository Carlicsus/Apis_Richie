from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import config.db
from crud.solicitudes import (create_solicitud, delete_solicitud,
                                  get_solicitud, get_solicitudes,
                                  update_solicitud)
from schemas.solicitudes import Solicitud, SolicitudCreate, SolicitudUpdate
from portadortoken import Portador

solicitudes_router = APIRouter(prefix="/solicitudes", tags=["Solicitudes"], dependencies=[Depends(Portador())])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@solicitudes_router.post("/", response_model=Solicitud)
def create(solicitud: SolicitudCreate, db: Session = Depends(get_db)):
    return create_solicitud(db, solicitud)

@solicitudes_router.get("/{solicitud_id}", response_model=Solicitud)
def read(solicitud_id: int, db: Session = Depends(get_db)):
    solicitud = get_solicitud(db, solicitud_id)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud

@solicitudes_router.get("/", response_model=list[Solicitud])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_solicitudes(db, skip, limit)

@solicitudes_router.put("/{solicitud_id}", response_model=Solicitud)
def update(solicitud_id: int, solicitud: SolicitudUpdate, db: Session = Depends(get_db)):
    updated_solicitud = update_solicitud(db, solicitud_id, solicitud)
    if not updated_solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return updated_solicitud

@solicitudes_router.delete("/{solicitud_id}", response_model=Solicitud)
def delete(solicitud_id: int, db: Session = Depends(get_db)):
    deleted_solicitud = delete_solicitud(db, solicitud_id)
    if not deleted_solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return deleted_solicitud
