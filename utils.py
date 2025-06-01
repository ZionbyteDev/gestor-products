### FUNCIONES AUXILIARES PARA CREAR PRODUCTO###

import mysql.connector
from mysql.connector import Error
from db import conectar  

def conectar_db():
    return conectar()  


def pedir_datos_producto():
    
    def validar_texto(mensaje):
        while True:
            texto = input(mensaje).lower().strip()
            if texto:
                return texto
            print("La casilla no puede estar vacía. Inténtalo de nuevo.")

    
    def validar_precio(mensaje):
        while True:
            try:
                precio = float(input(mensaje))
                if precio > 0:
                    return precio
                print("El precio debe ser un número mayor que 0. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingresa un número.")

    
    print("Ingresa los siguientes datos:")
    nombre = validar_texto("Nombre: ")
    descripcion = validar_texto("Descripción: ")
    categoria = validar_texto("Categoría: ")
    precio = validar_precio("Precio: ")

    
    return {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "precio": precio
    }
    
    
from mysql.connector import Error

def producto_existe(nombre, conexion):
    try:
        
        with conexion.cursor() as cursor:
            cursor.execute("SELECT nombre FROM productos WHERE nombre = %s", (nombre,))
            resultado = cursor.fetchone()
            return resultado is not None
    except Error as errores:
        print(f"Error al verificar si el producto existe: {errores}")
        return False
        
    
    
def insertar_producto(producto, conexion):
    try:
        with conexion.cursor() as cursor:
            consulta = """
                INSERT INTO productos (nombre, descripcion, categoria, precio)
                VALUES (%s, %s, %s, %s)
            """
            valores = (
                producto['nombre'],
                producto['descripcion'],
                producto['categoria'],
                producto['precio']
            )
            cursor.execute(consulta, valores)
            conexion.commit()
            print("✅ Producto insertado correctamente.")
    except Error as error:
        print(f"❌ Error al insertar el producto: {error}")


def mostrar_producto(producto):
    print("producto detallado")
    print(f"Nombre: ", producto["nombre"])
    print(f"Descripción: ", producto["descripcion"])
    print(f"Categoría: ", producto["categoria"])
    print(f"Precio: $", producto["precio"])
    
    
### funciones auxiliares de ver producto###

from mysql.connector import Error

def obtener_todos_los_productos(conexion):
    try:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            return productos
    except Error as error:
        print(f"Error al obtener productos: {error}")
        return []
    

def mostrar_lista_productos(productos):
    if not productos:
        print("No hay productos registrados en la base de datos.")
        return

    print("\n======= LISTA DE PRODUCTOS =======")
    for producto in productos:
        print(f"ID: {producto['id']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Categoría: {producto['categoria']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print("-" * 35)
        
        
        
### funciones auxiliares de actualizar producto###

def buscar_producto_por_nombre(conexion, nombre):
    with conexion.cursor(dictionary=True) as cursor:
        consulta = "SELECT * FROM productos WHERE nombre = %s"
        cursor.execute(consulta, (nombre,))
        return cursor.fetchone()
    

def menu_actualizacion():
    print("\n¿Qué deseas actualizar?")
    print("1. Nombre")
    print("2. Descripción")
    print("3. Categoría")
    print("4. Precio")
    print("5. Todos los campos")
    print("0. Cancelar")
    opcion = input("Elige una opción: ")
    return opcion


def pedir_nuevo_valor(campo):
    valor = input(f"Ingrese el nuevo valor para {campo}: ").strip()
    return valor



### funciones auxiliares de eliminar  producto###

def confirmar_eliminacion(nombre):
    confirmacion = input(f"¿Estás seguro que deseas eliminar el producto '{nombre}'? (s/n): ").lower()
    return confirmacion == "s"