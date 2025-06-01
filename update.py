from utils import conectar_db
from utils import pedir_datos_producto
from utils import (
    buscar_producto_por_nombre,
    menu_actualizacion,
    pedir_nuevo_valor,
)
from utils import mostrar_producto

def actualizar_producto():
    conexion = conectar_db()
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    nombre = input("Ingrese el nombre del producto que desea actualizar: ").strip().lower()
    producto = buscar_producto_por_nombre(conexion, nombre)

    if not producto:
        print("Producto no encontrado.")
        conexion.close()
        return

    mostrar_producto(producto)

    opcion = menu_actualizacion()
    campos_actualizados = {}

    if opcion == "1":
        campos_actualizados["nombre"] = pedir_nuevo_valor("nombre")
    elif opcion == "2":
        campos_actualizados["descripcion"] = pedir_nuevo_valor("descripción")
    elif opcion == "3":
        campos_actualizados["categoria"] = pedir_nuevo_valor("categoría")
    elif opcion == "4":
        campos_actualizados["precio"] = float(pedir_nuevo_valor("precio"))
    elif opcion == "5":
        campos_actualizados = pedir_datos_producto()
    elif opcion == "0":
        print("Actualización cancelada.")
        conexion.close()
        return
    else:
        print("Opción no válida.")
        conexion.close()
        return

    set_clause = ", ".join([f"{clave} = %s" for clave in campos_actualizados.keys()])
    valores = list(campos_actualizados.values())
    valores.append(producto["id"])

    consulta = f"UPDATE productos SET {set_clause} WHERE id = %s"

    with conexion.cursor() as cursor:
        cursor.execute(consulta, valores)
        conexion.commit()

    print("✅ Producto actualizado con éxito.")
    conexion.close()