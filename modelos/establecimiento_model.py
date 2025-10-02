from pydantic import BaseModel
from datetime import date

class EstablecimientoModel(BaseModel):
    id: int
    nombre: str
    direccion: str
    telefono: str
    estado: bool
    fecha_registro: date
