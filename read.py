from utils import conectar_db
from utils import obtener_todos_los_productos, mostrar_lista_productos

def ver_productos():
    conexion = conectar_db()
    if conexion is None:
        print("No se pudo establecer conexión para ver los productos.")
        return

    productos = obtener_todos_los_productos(conexion)
    mostrar_lista_productos(productos)

    conexion.close()