# =====================
#      FUNCIONES
# =====================

import random
palabras = ["JAVA", "JavaScript", "Python", "PHP", "SQL", "Ruby", "Swift", "Rust", "TypeScript", "Visual Basic"]

# Función para mostrar el dibujo del ahorcado
def mostrar_ahorcado(intentos):
    dibujos = [
        r"""
            -----
            |   |
            O   |
           /|\  |
           / \  |
        =========
        """,
        r"""
            -----
            |   |
            O   |
           /|\  |
           /    |
        =========
        """,
        r"""
            -----
            |   |
            O   |
           /|\  |
                |
        =========
        """,
        r"""
            -----
            |   |
            O   |
           /|   |
                |
        =========
        """,
        r"""
            -----
            |   |
            O   |
            |   |
                |
        =========
        """,
        r"""
            -----
            |   |
            O   |
                |
                |
        =========
        """,
        r"""
            -----
            |   |
                |
                |
                |
        =========
        """,
    ]
    print(dibujos[intentos])

# Función para elegir palabra
def elegir_p(palabras):
    n = random.choice(palabras)
    return n

# Función para mostrar las letras adivinadas
def mostrar_p(palabra, letras_adiv):
    mostrada = ""
    for letra in palabra:
        if letra in letras_adiv:
            mostrada += letra.upper() + " "
        else:
            mostrada += "_ "
    print(f'Palabra: {mostrada.strip()}')

# Función para ingresar y validar letra
def ingresar_letra(letras_us):
    while True:
        letra = input("Ingrese una letra: ").upper()
        if len(letra) != 1:
            print("Por favor, ingrese una sola letra")
        elif letra in letras_us:
            print("Letra ya usada, prueba otra")
        else:
            return letra