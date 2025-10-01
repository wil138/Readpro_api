from fastapi import APIRouter, HTTPException
from modelo.establecimiento_model import EstablecimientoModel
from typing import List
from datetime import date

class EstablecimientoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.establecimientos: List[EstablecimientoModel] = [
            EstablecimientoModel(
                id=1,
                nombre="Establecimiento Ejemplo",
                direccion="Calle Principal #1",
                telefono="88888888",
                estado=True,
                fecha_registro=date.today()
            )
        ]

        self.router.get("/", response_model=List[EstablecimientoModel])(self.obtener_establecimientos)
        self.router.post("/", response_model=EstablecimientoModel)(self.crear_establecimiento)
        self.router.put("/{establecimiento_id}", response_model=EstablecimientoModel)(self.actualizar_establecimiento)
        self.router.delete("/{establecimiento_id}")(self.borrar_establecimiento)

    def obtener_establecimientos(self) -> List[EstablecimientoModel]:
        return self.establecimientos

    def crear_establecimiento(self, establecimiento: EstablecimientoModel) -> EstablecimientoModel:
        establecimiento.id = len(self.establecimientos) + 1
        establecimiento.fecha_registro = date.today()
        self.establecimientos.append(establecimiento)
        return establecimiento

    def actualizar_establecimiento(self, establecimiento_id: int, establecimiento: EstablecimientoModel) -> EstablecimientoModel:
        for index, e in enumerate(self.establecimientos):
            if e.id == establecimiento_id:
                establecimiento.id = establecimiento_id
                establecimiento.fecha_registro = e.fecha_registro
                self.establecimientos[index] = establecimiento
                return establecimiento
        raise HTTPException(status_code=404, detail="Establecimiento no encontrado")

    def borrar_establecimiento(self, establecimiento_id: int) -> dict:
        for index, e in enumerate(self.establecimientos):
            if e.id == establecimiento_id:
                del self.establecimientos[index]
                return {"mensaje": "Establecimiento eliminado"}
        raise HTTPException(status_code=404, detail="Establecimiento no encontrado")


establecimiento_router = EstablecimientoAPI().router
