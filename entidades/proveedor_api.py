from fastapi import APIRouter, HTTPException
from modelo.proveedor_model import ProveedorModel
from typing import List
from datetime import date

class ProveedorAPI:
    def __init__(self):
        self.router = APIRouter()
        self.proveedores: List[ProveedorModel] = [
            ProveedorModel(
                id=1,
                nombre="Proveedor Ejemplo",
                telefono="99999999",
                correo="proveedor@example.com",
                direccion="Calle Principal #123",
                estado=True,
                fecha_registro=date.today()
            )
        ]

        # Endpoints
        self.router.get("/", response_model=List[ProveedorModel])(self.obtener_proveedores)
        self.router.post("/", response_model=ProveedorModel)(self.crear_proveedor)
        self.router.put("/{proveedor_id}", response_model=ProveedorModel)(self.actualizar_proveedor)
        self.router.delete("/{proveedor_id}")(self.borrar_proveedor)

    def obtener_proveedores(self) -> List[ProveedorModel]:
        return self.proveedores

    def crear_proveedor(self, proveedor: ProveedorModel) -> ProveedorModel:
        proveedor.id = len(self.proveedores) + 1
        proveedor.fecha_registro = date.today()
        self.proveedores.append(proveedor)
        return proveedor

    def actualizar_proveedor(self, proveedor_id: int, proveedor: ProveedorModel) -> ProveedorModel:
        for index, p in enumerate(self.proveedores):
            if p.id == proveedor_id:
                proveedor.id = proveedor_id
                proveedor.fecha_registro = p.fecha_registro
                self.proveedores[index] = proveedor
                return proveedor
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")

    def borrar_proveedor(self, proveedor_id: int) -> dict:
        for index, p in enumerate(self.proveedores):
            if p.id == proveedor_id:
                del self.proveedores[index]
                return {"mensaje": "Proveedor eliminado"}
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")


proveedor_router = ProveedorAPI().router
