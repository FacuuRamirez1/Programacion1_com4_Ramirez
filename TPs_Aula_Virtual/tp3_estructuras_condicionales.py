#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
print("Ejercicio 1:")
edad = int(input("Ingrese su edad: "))
if (edad > 18): 
    print("Es mayor de edad")
else:
    print("No es mayot de edad")

print("\n\n")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
print("Ejercicio 2:")
nota = float(input("Ingrese su nota: "))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

print("\n\n")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
print("Ejercicio 3:")
numero_par = int(input("Ingrese un número par: "))
if (numero_par % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingresar un número par")

print("\n\n")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.
print("Ejercicio 4:")
edad_persona = int(input("Ingrese su edad: "))
if (edad_persona < 12):
    print("Ustede pertenece a la categoría: Niño/a")

elif (edad_persona >= 12 or edad_persona < 18):
    print("Usted pertenece a la categoría: Adolecente")

elif (edad_persona >= 18 or edad_persona < 30):
    print("Usted pertenece a la categoría: Adulto/a joven")

else:
    print("Usted pertenece a la categoría: Adulto/a")

print("\n\n")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
print("Ejercicio 5:")
contraseña = input("Ingrese su contraseña: ")
if (len(contraseña) >= 8 and len(contraseña) <= 14):
    print("Ha ingresado una contraseña correccta")
else:
    print("Por favor ingrese una contraseña que contenga entre 8 y 14 caracteres")

print("\n\n")


# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
print("Ejercicio 6:")
import random
from statistics import mode, median, mean
nums_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f'Números aleatorios: {nums_aleatorios}')

if (mean(nums_aleatorios) > median(nums_aleatorios) and median(nums_aleatorios) > mode(nums_aleatorios)):
    print("El sesgo es positivo")

elif (mean(nums_aleatorios) < median(nums_aleatorios) and median(nums_aleatorios) < mode(nums_aleatorios)):
    print("El sesgo es negativo")

elif (mean(nums_aleatorios) == median(nums_aleatorios) and median(nums_aleatorios) == mode(nums_aleatorios)):
    print("No hay sesgo")

else:
    pass

print("\n\n")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
print("Ejercicio 7:")
frase_usuario = input("Ingrese una frase: ")


if (frase_usuario and frase_usuario[-1].lower() in 'aeiou'):
    print(f'{frase_usuario}!')

else:
    print(frase_usuario)

print("\n\n")


# 8)  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula.
print("Ejercicio 8:")
nombre = input("Ingrese su nombre: ")
n = len(nombre)
print("Elija una de las siguientes opciones:")
print("1. Si quiere su nombre en mayúsculas. \n2. Si quiere su nombre en minúsculas. \n3. Si quiere su nombre con la primer letra en mayúscula.")
optn = int(input("Ingrese el número correspodiente a la opción deseada: "))

print("")
if(optn == 1): 
    print(nombre.upper())

elif(optn == 2):
    print(nombre.lower())

elif(optn == 3):
    print(f"{nombre[0,1].upper()}{nombre[1:n + 1]}")

else: 
    pass

print("\n\n")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#   ● Menor que 3: "Muy leve" (imperceptible).
#   ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#   ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#   ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#   ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#   ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Ejercicio 9:")
mag_ter = float(input("Ingrese la magnitud del terremoto:"))

if (mag_ter < 3):
    print("Categoría del terremoto: muy leve (imperceptible)")

elif (mag_ter >= 3 and mag_ter < 4):
    print("Categoría del terremoto: leve (ligeramente perceptible)")

elif (mag_ter >= 4 and mag_ter < 5):
    print("Categoría del terremoto: Moderado (sentido por personas, pero sin causar daños)")

elif (mag_ter >= 5 and mag_ter < 6):
    print("Categoría del terremoto: Fuerte (puede causar daños en estructuras débiles)")

elif (mag_ter >= 6 and mag_ter < 7):
    print("Categoría del terremoto: Muy fuerte (puede causar daños significativos)")

elif (mag_ter >= 7):
    print("Categorpia del terremoto: Extremo (puede causar graves daños a gran escala)")

else: pass

print("\n\n")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
print("Ejercicio 10:")
from datetime import date
hemisferio = input("¿En qué hemisferio se encuentra? \nIngrese N si está en el hemisferio Norte \nIngrese S si está en el hemisferio Sur \nRespuesta: ").upper()
print("")
mes = int(input("Ingrese el mes del año en el que se encuentra (número):"))
dia = int(input("Ingrese el día (número): "))
fecha_usuario = date(2000, mes, dia)

print("")
if (hemisferio == "N"):
    if (fecha_usuario >= date(2000, 12, 21) and fecha_usuario <= date(2000, 3, 20)):
        print("Usted se encuentra en Invierno.")

    elif (fecha_usuario >= date(2000, 3, 21) and fecha_usuario <= date(2000, 6, 21)):
        print("Usted se encuentra en Primavera.")

    elif (fecha_usuario >= date(2000, 6, 21) and fecha_usuario <= date(2000, 9, 20)):
        print("Usted se encuentra en Verano.")

    elif (fecha_usuario >= date(2000, 9, 21) and fecha_usuario <= date(2000, 12, 20)):
        print("Usted se encuentra en Otoño.")

elif (hemisferio == "S"):
    if (fecha_usuario >= date(2000, 12, 21) and fecha_usuario <= date(2000, 3, 20)):
        print("Usted se encuentra en Verano.")

    elif (fecha_usuario >= date(2000, 3, 21) and fecha_usuario <= date(2000, 6, 21)):
        print("Usted se encuentra en Otoño.")

    elif (fecha_usuario >= date(2000, 6, 21) and fecha_usuario <= date(2000, 9, 20)):
        print("Usted se encuentra en Invierno.")

    elif (fecha_usuario >= date(2000, 9, 21) and fecha_usuario <= date(2000, 12, 20)):
        print("Usted se encuentra en Primavera.")

else: pass

print("\n\n")