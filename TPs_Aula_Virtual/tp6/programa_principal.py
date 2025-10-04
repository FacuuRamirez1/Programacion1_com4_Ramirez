from funciones import *

print("==================================")
print("¡BIENVENIDO AL PROGRAMA PRINCIPAL!")
print("==================================\n")

print("\nEjercicio 1")
print(hola_mundo())

print("\nEjercicio 2")
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

print("\nEjercicio 3")
nom = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nom, apellido, edad, residencia)

print("\nEjercicio 4")
radio = int(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

print("\nEjercicio 5")
seg = float(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(seg)

print("\nEjercicio 6")
numero = int(input("Ingrese un número entero: "))
for i in range(11):
    tabla_multiplicar(numero, i)

print("\nEjercicio 7")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print("Los resultados de la suma, resta, multiplicación y división entre números son:")
print(f'Suma: {resultados[0]}')
print(f'Resta: {resultados[1]}')
print(f'Multiplicación: {resultados[2]}')
print(f'División: {resultados[3]}')

print("\nEjercicio 8")
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en mts: "))
calcular_imc(peso, altura)

print("\nEjercicio 9")
celsius = float(input("Ingrese los grados en Celsius: "))
celsius_a_fahrenheit(celsius)

print("\nEjercicio 10")
nota1 = float(input("Ingrese el primer número: "))
nota2 = float(input("Ingrese el segundo número: "))
nota3 = float(input("Ingrese el tercer número: "))
calcular_promedio(nota1, nota2, nota3)