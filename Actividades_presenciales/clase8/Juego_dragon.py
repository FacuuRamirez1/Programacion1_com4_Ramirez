laberinto = [
    ["🐉", "🧱", "", "", ""],
    ["", "🧱", "", "🧱",""],
    ["", "", "", "🧱", ""],
    ["🧱", "🧱", "", "", ""],
    ["🧱","","","","🧱","🧱"]
    ["🧱", "", "🧱", "🧱", "🧱"]
    ["🧱", "", "", "", "🏁"]
]

print("==================")
print(" JUEGO DEL DRAGON ")
print("==================")


def buscar_salida(laberinto, fila, columna):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[fila])):
            print(laberinto[fila][columna])
    print("---------------")
    print("~ Derecha (D)")
    print("~ Izquierda (A)")
    print("~ Arriba (W)")
    print("~ Abajo (S)")

    opc = input("\nIngrese la opción elegida: ").upper()
    pos_fila, pos_columna = fila, columna
    if opc == "D":
        pos_columna += 1
    elif opc == "A":
        pos_columna -= 1
    elif opc == "W":
        pos_fila += 1
    elif opc == "S":
        pos_fila -= 1
    else:
        print("¡Error! Ingrese una opción válida...")
    
    