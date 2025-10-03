# ====================================
#          PROGRAMA PRINCIPAL
# ====================================
from funciones_ahorcado import *

palabra = elegir_p(palabras).upper()
letras_us = set()
letras_adiv = set()
intentos = 6

print("BIENVENIDO AL AHORCADO!")
while intentos != 0 and set(palabra) != letras_adiv:
    mostrar_ahorcado(intentos)
    mostrar_p(palabra, letras_adiv)
    print(f'')
    letra = ingresar_letra(letras_us)
    letras_us.add(letra)

    if letra in palabra:
        letras_adiv.add(letra)
        print("Has adivinado una letra!")
    else:
        intentos -= 1
        print(f'Incorrecto! Te quedan {intentos} intentos.')
mostrar_ahorcado(intentos)
mostrar_p(palabra, letras_adiv)
if set(palabra) == letras_adiv:
    print("\nGanaste!")
    print(f'Has adivinado la palabra: {palabra}')    

else:
    print("\nPerdiste!")
    print(f'La palabra era: {palabra}')