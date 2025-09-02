# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Ejercicio 1 \n")

for i in range(0, 101):
    print(f'{i}\n')

print("\n\n")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
print("Ejercicio 2 \n")

while True:
    num_usuario = int(input("Ingrese un número entero: "))
    if num_usuario != int:
        print("Error, ingresó un valor inválido.") # Si el número no es entero se termina el bucle (en la consigna no hay condición para que se termine, esto genera un bucle infinito).
        break
    else:
        num_usuario = str(num_usuario)
        print(f'El número {num_usuario} tiene {len(num_usuario)} dígitos.')

print("\n\n")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
print("Ejercicio 3 \n")

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 or num2 != int:
    print("Error, ingresó un valor inválido.")
elif num1 > num2:
    print("Error, el primer número debe ser menor que el segundo.")
else:
    suma = 0
    for i in range(num1 + 1, num2):
        suma += i

print(f"La suma de los números entre {num1} y {num2}, excluyendo a estos, es: {suma}")

print("\n\n")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
print("Ejercicio 4 \n")

while True:
    num_us = int(input("Ingrese un número entero (ingrese 0 si desea ver el resultado): "))
    if num_us != 0:
        suma = 0
        suma += num_us
    else:
        print(f'El total acumulado es: {suma}')
        break

print("\n\n")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("Ejercicio 5 \n")

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


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.


# 8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.