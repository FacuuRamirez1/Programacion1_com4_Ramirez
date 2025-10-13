from funciones import *

while True:
    print("==========================")
    print("      Menú Principal      \n")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    print("\n==========================")

    opc = int(input("Ingrese una opción: "))
    try:
        if opc == 1:
            mostrar_productos()
        elif opc == 2:
            agregar_producto()
        elif opc == 3:
            eliminar_producto()
        elif opc == 4:
            print("\nSaliendo del programa...")
            break
        else:
            print("Por favor ingrese una opción válida")

    except FileNotFoundError:
        print("¡Error! No existe el archivo")

    except TypeError:
        print("Ingrese un número entero positivo.")