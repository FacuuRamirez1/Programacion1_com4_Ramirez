# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
print("Ejercicio 1\n")

lista_1_a_100 = []

for i in range(1, 101):
    if i % 4 == 0:
        i = str(i)
        lista_1_a_100.append(i)

l = len(lista_1_a_100)
for i in range(l):
    print(lista_1_a_100[i])

print("\n\n")

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
print("Ejercicio 2\n")

lista1 = [1,2,3,4,5]

print("Forma tradicional:")
print(f'Penúltimo número: {lista1[3]}')

print("\nUsando índice negativo:")
print(f'Penúltimo número: {lista1[-2]}')

print("\n\n")
# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
print("Ejercicio 3\n")

lista_3_palabras = []

for i in range(3):
    p = input("Ingrese una palabra: ")
    lista_3_palabras.append(p)

print("\n")

for lista_3_palabras in lista_3_palabras:

    print(lista_3_palabras, end = " ")

print("\n\n")
# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
print("Ejercicio 4\n")

print("Lista original")
animales = ["perro","gato","conejo","pez"]
print(animales)

animales[1] = "loro"
animales[2] = "oso"

print("")
print("Lista modificada")
print(animales)


print("\n\n")

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print("Ejercicio 5")

numeros = [8, 15, 3, 22, 7] # Lista inicial
numeros.remove(max(numeros)) # Se elimina el elemento de mayor valor 
print(numeros) # Finalmente se imprime [8, 15, 3, 7]

print("\n\n")

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
print("Ejercicio 6\n")

lista = [10, 15, 20, 25, 30]
print(f'Lista: {lista}')
print(f'Primer elemento: {lista[0]}')
print(f'Segundo número: {lista[1]}')

print("\n\n")

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera
print("Ejercicio 7\n")
autos = ["sedan", "palio", "suran", "gol"]

print(f'Lista original: {autos}')

autos[1] = "punto"
autos[2] = "ka"

print(f'Lista modificada: {autos}')

print("\n\n")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
print("Ejercicio 8\n")

dobles = []

for i in range(5, 16, 5):
    dobles.append(2*i)

print(dobles)
print("\n\n")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    # c) Eliminar "pan" de la lista del primer cliente.
    # d) Imprimir la lista resultante por pantalla
print("Ejercicio 9\n")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(f'Lista original: {compras}')
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove(compras[0][0])

print(f'Lista modificada: {compras}')
print("\n\n")

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    # Posición lista_anidada[0]: 15
    # Posición lista_anidada[1]: True
    # Posición lista_anidada[2][0]: 25.5
    # Posición lista_anidada[2][1]: 57.9
    # Posición lista_anidada[2][2]: 30.6
    # Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.
print("Ejercicios 10\n")

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)