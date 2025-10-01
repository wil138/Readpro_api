from fastapi import APIRouter, HTTPException
from modelo.producto_model import ProductoModel
from typing import List
from datetime import date

class ProductoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.productos: List[ProductoModel] = [
            ProductoModel(
                id=1,
                nombre="Producto Ejemplo",
                descripcion="Descripción de ejemplo",
                precio=10.0,
                stock=100,
                estado=True,
                fecha_registro=date.today()
            )
        ]

        # Endpoints
        self.router.get("/", response_model=List[ProductoModel])(self.obtener_productos)
        self.router.post("/", response_model=ProductoModel)(self.crear_producto)
        self.router.put("/{producto_id}", response_model=ProductoModel)(self.actualizar_producto)
        self.router.delete("/{producto_id}")(self.borrar_producto)

    def obtener_productos(self) -> List[ProductoModel]:
        return self.productos

    def crear_producto(self, producto: ProductoModel) -> ProductoModel:
        producto.id = len(self.productos) + 1
        producto.fecha_registro = date.today()
        self.productos.append(producto)
        return producto

    def actualizar_producto(self, producto_id: int, producto: ProductoModel) -> ProductoModel:
        for index, p in enumerate(self.productos):
            if p.id == producto_id:
                producto.id = producto_id
                producto.fecha_registro = p.fecha_registro
                self.productos[index] = producto
                return producto
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    def borrar_producto(self, producto_id: int) -> dict:
        for index, p in enumerate(self.productos):
            if p.id == producto_id:
                del self.productos[index]
                return {"mensaje": "Producto eliminado"}
        raise HTTPException(status_code=404, detail="Producto no encontrado")


producto_router = ProductoAPI().router
