from funciones import *

# =========================
#   LISTA DE HERRAMIENTAS
# =========================
Catalogo_herramientas = []

# ==================
#   MENÚ PRINCIPAL
# ==================

while True:
    print("======= MENÚ PRINCIPAL ======")
    print("1. Cargar herramienta")
    print("2. Mostrar herramientas")
    print("3. Modificar herramienta")
    print("4. Eliminar herramienta")
    print("5. Consultar disponibilidad")
    print("6. Listar productos sin stock")
    print("7. Salir")
    print("=============================")
    opc = int(input("Ingrese la opción correspondiente (número): "))

    try:
        if opc == 1:
            print("--- Cargar herramienta ---")

            nom = input("Ingrese el nombre de la herramienta: ")
            cant = int(input("Ingrese la cantidad de herramientas: "))
            precio = float(input("Ingrese el precio de cada herramienta: "))

            if len(nom) != 0:
                if cant >= 0:
                    if precio > 0:
                        new_product = Cargar_herramientas(nom, cant, precio)
                        Catalogo_herramientas.append(new_product)
                    else:
                        print("¡Error! El precio del producto debe ser mayor a cero")
                else:
                    print("¡Error! La cantidad debe ser un entero >= 0.")
            else: 
                print("¡Error! El nombre no debe estar vacío.")

        elif opc == 2:
            print("--- Mostrar herramientas ---")
            Mostrar_herramientas()

        elif opc == 3:
            print("--- Modificar herramientas ---")
            nom = input("Ingrese el nombre de la herramienta a modificar: ")
            if len(nom) != 0:
                if nom in Catalogo_herramientas:
                    print("")
                    # Modificar_herramientas(nom)
            else:
                print("¡Error! Ingrese el nombre de una herramienta.")
        elif opc == 4:
            print("--- Eliminar herramienta ---")
        elif opc == 5:
            print("--- Consultar disponibilidad ---")
        elif opc == 6:
            print("--- Listar productos sin stock ---")
        elif opc == 7:
            print("Finalizando el programa...")
            break
        else:
            print("¡Error! Ingrese una opción válida.")
    except ValueError as e:
        print(f'¡Error! {e}')
    except Exception as e:
        print(f'¡Error! {e}')