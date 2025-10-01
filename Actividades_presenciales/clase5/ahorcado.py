# ---------- Funciones ----------

# Función para elegir palabra
def elegir_p(palabras):
    n = random.randint(0, len(palabras))
    return n

# ---------- Programa Principal ----------
import random

palabras = ["JAVA", "JavaScript", "Python", "PHP", "SQL", "Ruby", "Swift", "Rust", "TypeScript", "Visual Basic"]
letras = []
letras_adiv = []
intentos = 6

p_elegida = palabras[elegir_p(palabras) - 1].upper()
print("BIENVENIDO AL AHORCADO!")
for i in range(len(p_elegida)):
    print("_ ", end="")
print("")

while True:
    if intentos != 0:
        ing_l = input("\n\nIngrese una letra: ").upper()
        if ing_l in p_elegida:
            print(f'Haz adivinado la letra {ing_l}!')
            letras_adiv.append(ing_l)
            letras.append(ing_l)
            for i in range(len(p_elegida)):
                if i == ing_l:
                    print(f'{ing_l} ',end="")
                else:
                    print("_ ", end="")
            print("")
        else:
            print("\nLa letra no se encuentra en la palabra!")
            intentos -= 1
            letras_adiv.append(ing_l)
            letras.append(ing_l)
            print(f'Intentos disponibles: {intentos}\n')
            print(f'Letras ya ingresadas:')
            for i in range(len(letras)):
                print(f'{letras[i]} ', end="")
            print(f'\nLetras adivinadas: ')
            for i in range(len(letras_adiv)):
                print(f'{letras_adiv[i]} ', end="")
    else:
        print("Perdiste! :(")
        print("Se han acabado los intentos!")
        break