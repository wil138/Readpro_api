from pydantic import BaseModel
from datetime import date

class EstadoModel(BaseModel):
    id: int
    nombre: str
    descripcion: str
    estado: bool
    fecha_registro: date

