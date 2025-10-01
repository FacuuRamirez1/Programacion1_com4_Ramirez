# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Ejercicio 1")
print("Números del 0 al 100: \n")

for i in range(0, 101):
    print(f'{i}')

print("\n\n")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
print("Ejercicio 2")
print("Contador de dígitos \n")

num_usuario = int(input("Ingrese un número entero: "))
digitos = 0

while True:
        cant_dig = num_usuario // 10
        digitos += 1
        if num_usuario == 0:
            break

print(f'El número {num_usuario} tiene {digitos} dígitos.')

print("\n\n")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
print("Ejercicio 3")
print("Suma de números entre dos valores \n")

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
suma = 0

for i in range(num1 + 1, num2):
    suma = suma + i
print(f"La suma de los números entre {num1} y {num2}, excluyendo a estos, es: {suma}")

print("\n\n")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("Ejercicio 4 \n")

suma = 0

while True:
    num_us = int(input("Ingrese un número entero (ingrese 0 si desea ver el resultado): "))
    if num_us != 0:
        suma = suma + num_us
    else:
        print(f'El total acumulado es: {suma}')
        break

print("\n\n")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("Ejercicio 5")
print("Adivina el número \n")

import random
num_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    num_jugador = int(input("Ingrese un número entero entre 0 y 9: "))
    if num_jugador != num_aleatorio:
        print("Incorrecto, intenta de nuevo!")
        intentos += 1
    else:
        intentos += 1
        print("Correcto, haz adivinado en número!")
        break

print(f'Has necesitado {intentos} intentos para adivinar el número {num_aleatorio}.')

print("\n\n")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("Ejercicio 6 \n")
print("Números pares del 100 al 0: \n")

for number in range(100, -1, -1):
    if number % 2 == 0:
        print(f'{number}')

print("\n\n")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
print("Ejercicio 7 \n")
print("Suma de números entre 0 y un número indicado \n")

num_indicado = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, num_indicado + 1):
    suma = suma + i

print(f'La suma de los números entre 0 y {num_indicado} es: {suma}')

print("\n\n")

# 8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
print("Ejercicio 8 \n")
print("Contador de números pares, impares, positivos y negativos \n")

numeros_usuario = []
pares = 0
impares = 0
positivo = 0
negativo = 0
for i in range(10): # CAMBIAR 10 POR 100
    num = int(input(f'Ingrese el número {i + 1} entero: '))
    if num % 2 == 0:
        pares += 1
    elif num == 0:
        pass
    else:
        impares += 1
    
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    numeros_usuario.append(num)

print(f'Has ingresado {pares} números pares, {impares} números impares, {positivo} números positivos y {negativo} números negativos.')

print("\n\n")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
print("Ejercicio 9 \n")
print("Cálculo de la media de números ingresados \n")

suma_usuario = 0

for i in range (10): # CAMBIAR 10 POR 100 
    nums = int(input(f'Ingrese el número {i + 1} entero: '))
    suma_usuario = suma_usuario + nums

media = suma_usuario / 10
print(f'La media de los números ingresados es: {media}')

print("\n\n")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("Ejercicio 10")
print("Inversor de números \n")

num_invertido = ""
num_elegido = input("Ingrese un número entero positivo: ")

for i in range(len(num_elegido) - 1, -1, -1):
    aux = num_elegido[i]
    num_invertido = num_invertido + aux

print(f'El número invertido es: {int(num_invertido)}')