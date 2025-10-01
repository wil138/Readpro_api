from pydantic import BaseModel
from datetime import date

class ProductoModel(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    estado: bool
    fecha_registro: date
