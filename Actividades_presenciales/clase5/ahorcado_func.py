# ---------- Funciones ----------

# Función para elegir palabra
def elegir_p(palabras):
    n = random.randit(0, len(palabras))
    return n

# ---------- Programa Principal ----------
import random

palabras = ["JAVA", "JavaScript", "Python", "PHP", "SQL", "Ruby", "Swift", "Rust", "TypeScript", "Visual Basic"]
letras = []
intentos = 6

p_elegida = palabras[elegir_p(palabras)]
while True:

    ing_l = input("Ingrese una letra: ").lower()