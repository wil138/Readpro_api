from pydantic import BaseModel

class DetallePedidoModel(BaseModel):
    id: int
    id_pedido: int
    id_producto: int
    cantidad: int
    precio: float
