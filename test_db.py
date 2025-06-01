from db import conectar
from utils import producto_existe

def test_producto_existe():
    
    conexion = conectar()

    if conexion:
        
        nombre_existente = "Laptop"
        existe = producto_existe(nombre_existente, conexion)
        print(f"¿El producto '{nombre_existente}' existe? {existe}")

        
        nombre_inexistente = "ProductoFalso"
        existe = producto_existe(nombre_inexistente, conexion)
        print(f"¿El producto '{nombre_inexistente}' existe? {existe}")

        
        conexion.close()
    else:
        print("No se pudo conectar a la base de datos.")


if __name__ == "__main__":
    test_producto_existe()
