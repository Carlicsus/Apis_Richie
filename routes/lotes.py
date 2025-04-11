import asyncio
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import SessionLocal
from crud.lotes import (create_lote, delete_lote, get_lote,
                                         get_lotes, update_lote)
from schemas.lotes import (LoteMedicamento,
                                            LoteMedicamentoCreate,
                                            LoteMedicamentoUpdate)
from portadortoken import Portador

lotes_medicamentos_router = APIRouter(prefix="/lotes_medicamentos", tags=["Lotes Medicamentos"])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@lotes_medicamentos_router.post("/", response_model=LoteMedicamento)
async def create_lote_endpoint(
    lote_data: LoteMedicamentoCreate,
    db: Session = Depends(get_db),
    _: str = Depends(Portador())  # Protección con autenticación
):
    return await create_lote(db, lote_data)

@lotes_medicamentos_router.get("/{lote_id}", response_model=LoteMedicamento)
async def get_lote_endpoint(
    lote_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(Portador())  # Protección con autenticación
):
    lote = await get_lote(db, lote_id)
    if not lote:
        raise HTTPException(status_code=404, detail="Lote no encontrado")
    return lote

@lotes_medicamentos_router.get("/", response_model=List[LoteMedicamento])
async def get_lotes_endpoint(
    skip: Optional[int] = 0,
    limit: Optional[int] = 50,
    db: Session = Depends(get_db),
    _: str = Depends(Portador())
):
    return await get_lotes(db, skip, limit)

@lotes_medicamentos_router.put("/{lote_id}", response_model=LoteMedicamento)
async def update_lote_endpoint(
    lote_id: int,
    lote_data: LoteMedicamentoUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(Portador())  # Protección con autenticación
):
    lote = await update_lote(db, lote_id, lote_data)
    if not lote:
        raise HTTPException(status_code=404, detail="Lote no encontrado")
    return lote

@lotes_medicamentos_router.delete("/{lote_id}", response_model=LoteMedicamento)
async def delete_lote_endpoint(
    lote_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(Portador())  # Protección con autenticación
):
    lote = await delete_lote(db, lote_id)
    if not lote:
        raise HTTPException(status_code=404, detail="Lote no encontrado")
    return lote
