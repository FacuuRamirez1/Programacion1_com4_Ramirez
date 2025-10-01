# ---------- Funciones ----------

# Función para elegir palabra
def elegir_p(palabras):
    n = random.randint(0, len(palabras))
    return n

# ---------- Programa Principal ----------
import random

palabras = ["JAVA", "JavaScript", "Python", "PHP", "SQL", "Ruby", "Swift", "Rust", "TypeScript", "Visual Basic"]
letras = []
intentos = 6

p_elegida = palabras[elegir_p(palabras)].upper()
print("BIENVENIDO AL AHORCADO!")

while True:
    if intentos != 0:
        for i in range(len(p_elegida)):
            print("_ ", end="")
        print("")
        ing_l = input("Ingrese una letra: ").upper()
        if ing_l in p_elegida:
            print(f'Haz adivinado la letra {ing_l}!')
            for i in range(len(p_elegida)):
                if i == ing_l:
                    print(f'{ing_l} ')
                else:
                    print("_ ")
        else:
            print("\nLa letra no se encuentra en la palabra!")
            intentos -= 1
            print(f'Intentos disponibles: {intentos}\n')
    else:
        print("Perdiste! :(")
        print("Se han acabado los intentos!")
        break