from fastapi import APIRouter, HTTPException
from modelo.metodopago_model import MetodoPagoModel
from typing import List
from datetime import date

class MetodoPagoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.metodospago: List[MetodoPagoModel] = [
            MetodoPagoModel(
                id=1,
                nombre="Pago Ejemplo",
                descripcion="Descripción de pago",
                estado=True,
                fecha_registro=date.today()
            )
        ]

        self.router.get("/", response_model=List[MetodoPagoModel])(self.obtener_metodospago)
        self.router.post("/", response_model=MetodoPagoModel)(self.crear_metodopago)
        self.router.put("/{metodopago_id}", response_model=MetodoPagoModel)(self.actualizar_metodopago)
        self.router.delete("/{metodopago_id}")(self.borrar_metodopago)

    def obtener_metodospago(self) -> List[MetodoPagoModel]:
        return self.metodospago

    def crear_metodopago(self, metodopago: MetodoPagoModel) -> MetodoPagoModel:
        metodopago.id = len(self.metodospago) + 1
        metodopago.fecha_registro = date.today()
        self.metodospago.append(metodopago)
        return metodopago

    def actualizar_metodopago(self, metodopago_id: int, metodopago: MetodoPagoModel) -> MetodoPagoModel:
        for index, m in enumerate(self.metodospago):
            if m.id == metodopago_id:
                metodopago.id = metodopago_id
                metodopago.fecha_registro = m.fecha_registro
                self.metodospago[index] = metodopago
                return metodopago
        raise HTTPException(status_code=404, detail="MétodoPago no encontrado")

    def borrar_metodopago(self, metodopago_id: int) -> dict:
        for index, m in enumerate(self.metodospago):
            if m.id == metodopago_id:
                del self.metodospago[index]
                return {"mensaje": "MétodoPago eliminado"}
        raise HTTPException(status_code=404, detail="MétodoPago no encontrado")


metodopago_router = MetodoPagoAPI().router
