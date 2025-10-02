from pydantic import BaseModel
from datetime import date

class PedidoModel(BaseModel):
    id: int
    id_cliente: int
    id_metodopago: int
    total: float
    estado: bool
    fecha_registro: date
