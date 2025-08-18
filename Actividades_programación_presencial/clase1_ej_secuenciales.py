while (True) :
    monto_total = int(input("Ingrese el monto total: "))
    print("-------------------------------------\n")
    propina_10 = (monto_total * 0.10)
    monto_propina_10 = monto_total + propina_10
    propina_15 = (monto_total * 0.15)
    monto_propina_15 = monto_total + propina_15
    print(f'Propina sugerida (10%): {propina_10}')
    print(f'Total a pagar (10%): {monto_propina_10}')
    print("-------------------------------------\n")
    print(f'Propina sugerida (15%): {propina_15}')
    print(f'Total a pagar (15%): {monto_propina_15}')
    print('-------------------------------------\n')
    print("Elija una opción: \n1. Nuevo monto \n2. Salir \n")
    option = int(input("Ingrese el número correspondiente: "))
    print("-------------------------------------\n")
    
    if (option == 2):
        print("Gracias por su visita!")
        break