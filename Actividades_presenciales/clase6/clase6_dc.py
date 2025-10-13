while True:
    espacio = int(input("Ingrese un número entero positivo: "))
    if espacio > 0:
        mochila = ["" for _ in range(espacio)]
        break
    else:
        print("Ingrese un número válido.")

while True:
    print("¡Opciones de la mochila!")
    print("1. Guardar objeto")
    print("2. Ver Mochila")
    print("3. Salir")
    opc = int(input("Ingrese una opción (nro correspondiente): "))
    try:
        if opc == 1:
            print("¡Guardar objeto en la mochila!")
        elif opc == 2:
            print("¡Ver Mochila!")
        elif opc == 3:
            break
    except ValueError:
        print("¡Ingrese una opción válida!")