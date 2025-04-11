from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RecetaBase(BaseModel):
    Paciente_Nombre: str
    Paciente_Edad: int
    Medico_Nombre: str
    Fecha: datetime
    Diagnostico: Optional[str] = None
    Medicamentos: Optional[str] = None
    Indicaciones: Optional[str] = None
    Fecha_registro: Optional[datetime] = None

class RecetaCreate(RecetaBase):
    pass

class RecetaUpdate(RecetaBase):
    pass

class Receta(RecetaBase):
    ID: int

    class Config:
        from_attributes = True
