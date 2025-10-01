from fastapi import APIRouter, HTTPException
from modelo.cliente_model import ClienteModel
from typing import List
from datetime import date

class ClienteAPI:
    def __init__(self):
        self.router = APIRouter()
        self.clientes: List[ClienteModel] = [
            ClienteModel(
                id=1,
                numero_ruc="123456789",
                nombre="Juan",
                apellido="Pérez",
                telefono="88888888",
                correo="juan@example.com",
                estado=True,
                fecha_registro=date.today()
            )
        ]

        # Endpoints
        self.router.get("/", response_model=List[ClienteModel])(self.obtener_clientes)
        self.router.post("/", response_model=ClienteModel)(self.crear_cliente)
        self.router.put("/{cliente_id}", response_model=ClienteModel)(self.actualizar_cliente)
        self.router.delete("/{cliente_id}")(self.borrar_cliente)

    def obtener_clientes(self) -> List[ClienteModel]:
        return self.clientes

    def crear_cliente(self, cliente: ClienteModel) -> ClienteModel:
        cliente.id = len(self.clientes) + 1
        cliente.fecha_registro = date.today()
        self.clientes.append(cliente)
        return cliente

    def actualizar_cliente(self, cliente_id: int, cliente: ClienteModel) -> ClienteModel:
        for index, c in enumerate(self.clientes):
            if c.id == cliente_id:
                cliente.id = cliente_id
                cliente.fecha_registro = c.fecha_registro  # Mantener fecha original
                self.clientes[index] = cliente
                return cliente
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    def borrar_cliente(self, cliente_id: int) -> dict:
        for index, c in enumerate(self.clientes):
            if c.id == cliente_id:
                del self.clientes[index]
                return {"mensaje": "Cliente eliminado"}
        raise HTTPException(status_code=404, detail="Cliente no encontrado")


cliente_router = ClienteAPI().router
