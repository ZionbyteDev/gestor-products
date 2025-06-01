
from utils import (
    conectar_db,
    pedir_datos_producto,
    producto_existe,
    insertar_producto,
    mostrar_producto  
)

def crear_producto():
    
    conexion = conectar_db()
    if not conexion:
        print("❌ No se pudo establecer conexión con la base de datos.")
        return

    
    producto = pedir_datos_producto()

    
    if producto_existe(producto['nombre'], conexion):
        print("⚠️ El producto ya existe. Intenta con otro nombre.")
    else:
        
        insertar_producto(producto, conexion)
        print("✅ Producto creado exitosamente. Detalles:")
        mostrar_producto(producto)

    
    conexion.close()
