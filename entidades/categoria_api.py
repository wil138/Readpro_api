from fastapi import APIRouter, HTTPException
from modelo.categoria_model import CategoriaModel
from typing import List
from datetime import date

class CategoriaAPI:
    def __init__(self):
        self.router = APIRouter()
        self.categorias: List[CategoriaModel] = [
            CategoriaModel(
                id=1,
                nombre="Categoría Ejemplo",
                descripcion="Descripción ejemplo",
                estado=True,
                fecha_registro=date.today()
            )
        ]

        self.router.get("/", response_model=List[CategoriaModel])(self.obtener_categorias)
        self.router.post("/", response_model=CategoriaModel)(self.crear_categoria)
        self.router.put("/{categoria_id}", response_model=CategoriaModel)(self.actualizar_categoria)
        self.router.delete("/{categoria_id}")(self.borrar_categoria)

    def obtener_categorias(self) -> List[CategoriaModel]:
        return self.categorias

    def crear_categoria(self, categoria: CategoriaModel) -> CategoriaModel:
        categoria.id = len(self.categorias) + 1
        categoria.fecha_registro = date.today()
        self.categorias.append(categoria)
        return categoria

    def actualizar_categoria(self, categoria_id: int, categoria: CategoriaModel) -> CategoriaModel:
        for index, c in enumerate(self.categorias):
            if c.id == categoria_id:
                categoria.id = categoria_id
                categoria.fecha_registro = c.fecha_registro
                self.categorias[index] = categoria
                return categoria
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    def borrar_categoria(self, categoria_id: int) -> dict:
        for index, c in enumerate(self.categorias):
            if c.id == categoria_id:
                del self.categorias[index]
                return {"mensaje": "Categoría eliminada"}
        raise HTTPException(status_code=404, detail="Categoría no encontrada")


categoria_router = CategoriaAPI().router
