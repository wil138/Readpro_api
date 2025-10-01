from pydantic import BaseModel, EmailStr
from datetime import date

class ProveedorModel(BaseModel):
    id: int
    nombre: str
    telefono: str
    correo: EmailStr
    direccion: str
    estado: bool
    fecha_registro: date
