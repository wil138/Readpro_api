from fastapi import FastAPI
from entidades.cliente_api import cliente_router
from entidades.proveedor_api import proveedor_router
from entidades.producto_api import producto_router
from entidades.categoria_api import categoria_router
from entidades.pedido_api import pedido_router
from entidades.detallepedido_api import detallepedido_router
from entidades.metodopago_api import metodopago_router
from entidades.establecimiento_api import establecimiento_router
from entidades.estado_api import estado_router

app = FastAPI(title="API de E-commerce", version="1.0")

app.include_router(cliente_router, prefix="/clientes", tags=["Clientes"])
app.include_router(proveedor_router, prefix="/proveedores", tags=["Proveedores"])
app.include_router(producto_router, prefix="/productos", tags=["Productos"])
app.include_router(categoria_router, prefix="/categorias", tags=["Categorías"])
app.include_router(pedido_router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(detallepedido_router, prefix="/detallepedidos", tags=["DetallePedidos"])
app.include_router(metodopago_router, prefix="/metodospago", tags=["Métodos de Pago"])
app.include_router(establecimiento_router, prefix="/establecimientos", tags=["Establecimientos"])
app.include_router(estado_router, prefix="/estados", tags=["Estados"])

