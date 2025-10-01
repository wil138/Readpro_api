from fastapi import APIRouter, HTTPException
from modelos.estado_model import EstadoModel
from typing import List
from datetime import date

class EstadoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.estados: List[EstadoModel] = [
            EstadoModel(
                id=1,
                nombre="Estado Ejemplo",
                descripcion="Descripción de estado",
                estado=True,
                fecha_registro=date.today()
            )
        ]

        self.router.get("/", response_model=List[EstadoModel])(self.obtener_estados)
        self.router.post("/", response_model=EstadoModel)(self.crear_estado)
        self.router.put("/{estado_id}", response_model=EstadoModel)(self.actualizar_estado)
        self.router.delete("/{estado_id}")(self.borrar_estado)

    def obtener_estados(self) -> List[EstadoModel]:
        return self.estados

    def crear_estado(self, estado: EstadoModel) -> EstadoModel:
        estado.id = len(self.estados) + 1
        estado.fecha_registro = date.today()
        self.estados.append(estado)
        return estado

    def actualizar_estado(self, estado_id: int, estado: EstadoModel) -> EstadoModel:
        for index, e in enumerate(self.estados):
            if e.id == estado_id:
                estado.id = estado_id
                estado.fecha_registro = e.fecha_registro
                self.estados[index] = estado
                return estado
        raise HTTPException(status_code=404, detail="Estado no encontrado")

    def borrar_estado(self, estado_id: int) -> dict:
        for index, e in enumerate(self.estados):
            if e.id == estado_id:
                del self.estados[index]
                return {"mensaje": "Estado eliminado"}
        raise HTTPException(status_code=404, detail="Estado no encontrado")


estado_router = EstadoAPI().router
