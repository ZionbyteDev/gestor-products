from create import crear_producto
from read import ver_productos
from update import actualizar_producto
from delete import eliminar_producto

def mostrar_menu():
    print("\n====== GESTOR DE PRODUCTOS ======")
    print("1. Crear producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("============================================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Gracias por usar el Gestor de Productos. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()