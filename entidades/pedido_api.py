from fastapi import APIRouter, HTTPException
from modelo.pedido_model import PedidoModel
from typing import List
from datetime import date

class PedidoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.pedidos: List[PedidoModel] = [
            PedidoModel(
                id=1,
                id_cliente=1,
                id_metodopago=1,
                total=100.0,
                estado=True,
                fecha_registro=date.today()
            )
        ]

        self.router.get("/", response_model=List[PedidoModel])(self.obtener_pedidos)
        self.router.post("/", response_model=PedidoModel)(self.crear_pedido)
        self.router.put("/{pedido_id}", response_model=PedidoModel)(self.actualizar_pedido)
        self.router.delete("/{pedido_id}")(self.borrar_pedido)

    def obtener_pedidos(self) -> List[PedidoModel]:
        return self.pedidos

    def crear_pedido(self, pedido: PedidoModel) -> PedidoModel:
        pedido.id = len(self.pedidos) + 1
        pedido.fecha_registro = date.today()
        self.pedidos.append(pedido)
        return pedido

    def actualizar_pedido(self, pedido_id: int, pedido: PedidoModel) -> PedidoModel:
        for index, p in enumerate(self.pedidos):
            if p.id == pedido_id:
                pedido.id = pedido_id
                pedido.fecha_registro = p.fecha_registro
                self.pedidos[index] = pedido
                return pedido
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    def borrar_pedido(self, pedido_id: int) -> dict:
        for index, p in enumerate(self.pedidos):
            if p.id == pedido_id:
                del self.pedidos[index]
                return {"mensaje": "Pedido eliminado"}
        raise HTTPException(status_code=404, detail="Pedido no encontrado")


pedido_router = PedidoAPI().router
