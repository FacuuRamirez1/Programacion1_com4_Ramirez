# ---------- Ejercicio 1 - Bucle for ----------
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
corrimiento = int(input("Ingresel el número de corrimiento: "))
mensaje = ""
letra = ""
aux = ""
mensajes_finales = []

for oficial in range(1, 6):
    mensaje = input(f'Ingrese el mensaje para el oficial {oficial}: ').lower()
    mensaje_encript = ""
    for letra in mensaje:
        if letra in abecedario:
            aux =  abecedario.index(letra)
            n_aux = (aux + corrimiento) % len(abecedario)
            mensaje_encript += abecedario[n_aux]
        else:
            mensaje_encript += letra
    mensajes_finales.append(mensaje_encript)
            
for oficial in range(1, 6):
    print(f'Mensaje para el oficial {oficial}:')
    print(mensajes_finales[oficial - 1])


# ---------- Ejercicio 2 - Bucle while ----------

import random
print("Juguemos piedra, papel o tijeras!")
opciones = {1:"piedra", 2:"papel", 3:"tijeras"}
cont_jug = 0
cont_ia = 0

while True:
    print("Elija una de las opciones:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    print("4. Salir\n")
    opc_jug = int(input("Ingrese el número de la opción elegida: "))
    opc_ia = random.randint(1, 3)
    
    if (opc_jug == 4):
        print("\nJUEGO TERMINADO! \n")
        break
    elif (opc_jug not in [1, 2, 3]):
        print("Ingrese una opción válida.")
        continue

    print(f'Jugador: {opciones[opc_jug]}') if (opc_jug in opciones) else print("Juego terminado!")
    print(f'Máquina: {opciones[opc_ia]}\n')

    if opc_jug == opc_ia:
        print("Empate! \n")
    elif (opc_jug == 1 and opc_ia == 3) or (opc_jug == 2 and opc_ia == 1) or (opc_jug == 3 and opc_ia == 2):
        print("Ganaste! \n")
        cont_jug += 1
    else: 
        print("Perdiste! \n")
        cont_ia += 1
    
    print(f'Contador => jug:{cont_jug} - máquina:{cont_ia}\n')

