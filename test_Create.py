from utils import conectar_db, producto_existe, insertar_producto, mostrar_producto

def test_crear_producto():
    # Conectar a la base de datos
    conexion = conectar_db()
    if not conexion:
        print("❌ No se pudo conectar a la base de datos. Test abortado.")
        return

    try:
        # Datos del producto para el test
        producto_test = {
            "nombre": "Pancito",
            "descripcion": "pan con sabor a chocolate",
            "categoria": "panes",
            "precio": 2.50
        }

        # Verificar si el producto ya existe
        if producto_existe(producto_test["nombre"], conexion):
            print(f"⚠️ El producto '{producto_test['nombre']}' ya existe en la base de datos. Test fallido.")
        else:
            # Insertar el producto
            insertar_producto(producto_test, conexion)

            # Verificar si el producto fue insertado correctamente
            if producto_existe(producto_test["nombre"], conexion):
                print(f"✅ Test exitoso: El producto '{producto_test['nombre']}' fue creado correctamente.")
                mostrar_producto(producto_test)
            else:
                print(f"❌ Test fallido: El producto '{producto_test['nombre']}' no se insertó en la base de datos.")
    except Exception as e:
        print(f"❌ Error durante el test: {e}")
    finally:
        # Cerrar la conexión
        conexion.close()
        print("Conexión cerrada.")

# Ejecutar el test
if __name__ == "__main__":
    test_crear_producto()