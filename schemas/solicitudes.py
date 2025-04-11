from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SolicitudBase(BaseModel):
    Paciente_ID: int
    Medico_ID: int
    Servicio_ID: int
    Prioridad: str
    Descripcion: str
    Estatus: Optional[str] = "Registrada"
    Estatus_Aprobacion: Optional[bool] = False

class SolicitudCreate(SolicitudBase):
    pass

class SolicitudUpdate(BaseModel):
    Prioridad: Optional[str]
    Descripcion: Optional[str]
    Estatus: Optional[str]
    Estatus_Aprobacion: Optional[bool]
    Fecha_Actualizacion: Optional[datetime] = Field(default_factory=datetime.utcnow)

class SolicitudInDBBase(SolicitudBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime]
    
    class Config:
        from_attributes = True

class Solicitud(SolicitudInDBBase):
    pass