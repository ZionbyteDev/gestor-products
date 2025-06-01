from db import conectar
from utils import producto_existe

def test_producto_existe():
    # Conectar a la base de datos
    conexion = conectar()

    if conexion:
        # Caso 1: Producto que existe
        nombre_existente = "Laptop"
        existe = producto_existe(nombre_existente, conexion)
        print(f"¿El producto '{nombre_existente}' existe? {existe}")

        # Caso 2: Producto que no existe
        nombre_inexistente = "ProductoFalso"
        existe = producto_existe(nombre_inexistente, conexion)
        print(f"¿El producto '{nombre_inexistente}' existe? {existe}")

        # Cerrar la conexión
        conexion.close()
    else:
        print("No se pudo conectar a la base de datos.")

# Ejecutar la prueba
if __name__ == "__main__":
    test_producto_existe()