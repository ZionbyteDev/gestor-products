from utils import conectar_db
from utils import mostrar_producto
from update import buscar_producto_por_nombre
from utils import confirmar_eliminacion

def eliminar_producto():
    conexion = conectar_db()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip().lower()
    producto = buscar_producto_por_nombre(conexion, nombre)

    if not producto:
        print("Producto no encontrado.")
        conexion.close()
        return

    mostrar_producto(producto)

    if confirmar_eliminacion(nombre):
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM productos WHERE nombre = %s"
            cursor.execute(consulta, (nombre,))
            conexion.commit()
        print(f"✅ Producto '{nombre}' eliminado correctamente.")
    else:
        print("❌ Eliminación cancelada.")

    conexion.close()