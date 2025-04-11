from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoteMedicamentoBase(BaseModel):
    Medicamento_ID: int
    PersonalMedico_ID: int
    Clave: str
    Estatus: str
    Costo_Total: float
    Cantidad: int
    Ubicacion: str

class LoteMedicamentoCreate(LoteMedicamentoBase):
    pass

class LoteMedicamentoUpdate(BaseModel):
    Estatus: Optional[str] = None
    Costo_Total: Optional[float] = None
    Cantidad: Optional[int] = None
    Ubicacion: Optional[str] = None
    Fecha_actualizacion: Optional[datetime] = None

class LoteMedicamentoInDBBase(LoteMedicamentoBase):
    ID: int
    Fecha_registro: datetime
    Fecha_actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True  # Asegura que los modelos se puedan convertir correctamente desde SQLAlchemy

class LoteMedicamento(LoteMedicamentoInDBBase):
    pass
