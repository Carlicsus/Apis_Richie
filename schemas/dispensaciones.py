from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class DispensacionBase(BaseModel):
    RecetaMedica_ID: Optional[int] = None
    PersonalMedico_ID: int
    Departamento_ID: int
    Solicitud_ID: Optional[int] = None
    Estatus: str
    Tipo: str
    TotalMedicamentosEntregados: int
    Total_costo: float
    Fecha_registro: datetime
    Fecha_actualizacion: Optional[datetime] = None

class DispensacionCreate(DispensacionBase):
    pass

class DispensacionUpdate(DispensacionBase):
    pass

class Dispensacion(DispensacionBase):
    ID: int

    class Config:
        from_attributes = True
