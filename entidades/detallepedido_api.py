from fastapi import APIRouter, HTTPException
from modelo.detallepedido_model import DetallePedidoModel
from typing import List

class DetallePedidoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.detalles: List[DetallePedidoModel] = [
            DetallePedidoModel(
                id=1,
                id_pedido=1,
                id_producto=1,
                cantidad=2,
                precio=20.0
            )
        ]

        self.router.get("/", response_model=List[DetallePedidoModel])(self.obtener_detalles)
        self.router.post("/", response_model=DetallePedidoModel)(self.crear_detalle)
        self.router.put("/{detalle_id}", response_model=DetallePedidoModel)(self.actualizar_detalle)
        self.router.delete("/{detalle_id}")(self.borrar_detalle)

    def obtener_detalles(self) -> List[DetallePedidoModel]:
        return self.detalles

    def crear_detalle(self, detalle: DetallePedidoModel) -> DetallePedidoModel:
        detalle.id = len(self.detalles) + 1
        self.detalles.append(detalle)
        return detalle

    def actualizar_detalle(self, detalle_id: int, detalle: DetallePedidoModel) -> DetallePedidoModel:
        for index, d in enumerate(self.detalles):
            if d.id == detalle_id:
                detalle.id = detalle_id
                self.detalles[index] = detalle
                return detalle
        raise HTTPException(status_code=404, detail="DetallePedido no encontrado")

    def borrar_detalle(self, detalle_id: int) -> dict:
        for index, d in enumerate(self.detalles):
            if d.id == detalle_id:
                del self.detalles[index]
                return {"mensaje": "DetallePedido eliminado"}
        raise HTTPException(status_code=404, detail="DetallePedido no encontrado")


detallepedido_router = DetallePedidoAPI().router
