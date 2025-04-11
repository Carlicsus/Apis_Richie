from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MedicamentoBase(BaseModel):
    Nombre_Comercial: str
    Nombre_Generico: str
    Via_Administracion: str
    Presentacion: str
    Tipo: str
    Cantidad: int
    Volumen: float
    Fecha_registro: datetime
    Fecha_actualizacion: Optional[datetime] = None

class MedicamentoCreate(MedicamentoBase):
    pass

class MedicamentoUpdate(MedicamentoBase):
    pass

class Medicamento(MedicamentoBase):
    ID: int

    class Config:
        from_attributes = True
