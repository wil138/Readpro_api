from pydantic import BaseModel, EmailStr
from datetime import date

class ClienteModel(BaseModel):
    id: int
    numero_ruc: str
    nombre: str
    apellido: str
    telefono: str
    correo: EmailStr
    estado: bool
    fecha_registro: date
