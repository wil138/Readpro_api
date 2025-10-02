

# 📦 API para Gestión de Pedidos de Comerciantes y Distribuidores

Este proyecto implementa una API REST usando FastAPI para un sistema tipo PedidosYa,
enfocado a comerciantes y distribuidores.
Permite gestionar clientes, proveedores, productos, categorías, pedidos,
detalles de pedidos, métodos de pago, establecimientos y estados.

El objetivo es ofrecer una API robusta para la gestión de pedidos,
optimizando procesos de comercio y distribución.

## 🗂 Estructura del Proyecto

proyecto_pedidos/
│── main.py
│── entidades/
│   ├── __init__.py
│   ├── cliente_api.py
│   ├── proveedor_api.py
│   ├── producto_api.py
│   ├── categoria_api.py
│   ├── pedido_api.py
│   ├── detallepedido_api.py
│   ├── metodopago_api.py
│   ├── establecimiento_api.py
│   ├── estado_api.py
│   └── cliente.py              # Lógica de negocio específica del cliente
│── modelos/
│   ├── cliente_model.py
│   ├── proveedor_model.py
│   ├── producto_model.py
│   ├── categoria_model.py
│   ├── pedido_model.py
│   ├── detallepedido_model.py
│   ├── metodopago_model.py
│   ├── establecimiento_model.py
│   └── estado_model.py
│── README.md
│── LICENSE

## 🚀 Instalación

1. Clonar el repositorio:
git clone https://github.com/wil138/proyecto_pedidos.git
cd proyecto_pedidos

2. Crear entorno virtual:
python -m venv venv

3. Activar entorno virtual:
- Linux/Mac: source venv/bin/activate
- Windows: venv\\Scripts\\activate

4. Instalar dependencias:
pip install fastapi uvicorn

## ⚙️ Ejecución

Ejecutar el servidor:
uvicorn main:app --reload

La API estará disponible en:
http://127.0.0.1:8000

## 📜 Documentación

FastAPI genera documentación automática:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- 
## 📌 Endpoints principales

| Entidad          | GET               | POST              | PUT                    | DELETE                 |
| ---------------- | ----------------- | ----------------- | ---------------------- | ---------------------- |
| Clientes         | /clientes         | /clientes         | /clientes/{id}         | /clientes/{id}         |
| Proveedores      | /proveedores      | /proveedores      | /proveedores/{id}      | /proveedores/{id}      |
| Productos        | /productos        | /productos        | /productos/{id}        | /productos/{id}        |
| Categorías       | /categorias       | /categorias       | /categorias/{id}       | /categorias/{id}       |
| Pedidos          | /pedidos          | /pedidos          | /pedidos/{id}          | /pedidos/{id}          |
| DetallePedidos   | /detallepedidos   | /detallepedidos   | /detallepedidos/{id}   | /detallepedidos/{id}   |
| Métodos de Pago  | /metodospago      | /metodospago      | /metodospago/{id}      | /metodospago/{id}      |
| Establecimientos | /establecimientos | /establecimientos | /establecimientos/{id} | /establecimientos/{id} |
| Estados          | /estados          | /estados          | /estados/{id}          | /estados/{id}          |

## 📌 Ejemplo de uso

curl -X POST "http://127.0.0.1:8000/clientes" \
-H "Content-Type: application/json" \
-d '{
    "id": 0,
    "numero_ruc": "123456789",
    "nombre": "Luis",
    "apellido": "Gonzalez",
    "telefono": "88888888",
    "correo": "luis@example.com",
    "estado": true,
    "fecha_registro": "2025-09-30"
}'

Obtener todos los clientes:
curl http://127.0.0.1:8000/clientes

## 📚 Tecnologías utilizadas

- Python 3.12+
- FastAPI
- Uvicorn

## 👤 Autor

- Nombre: [Grupo#5]
- Email: [w138jvc@gmail.com]
- GitHub: [@TuUsuario](https://github.com/wil138/Redpro_api)

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
"""


