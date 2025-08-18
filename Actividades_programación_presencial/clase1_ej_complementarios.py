# 1)
print("Ejercicio 1 \n")
numero1 = 10
print(f'numero1 = {numero1}')
print("\n\n")

# 2)
print("Ejercicio 2 \n")
numero2 = 12.5
print(f'numero2 = {numero2}')
print("\n\n")

# 3)
print("Ejercicio 3 \n")
suma = numero1 + numero2
print(f'Suma de numero1 y numero2 = {suma}')
print("\n\n")

# 4)
print("Ejercicio 4 \n")
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f'Resta: {resta} \nMultiplicación: {multiplicacion} \nDivisión: {division}')
print("\n\n")
# 5)
print("Ejercicio 5 \n")
nombre = "Facundo"
print(f'nombre = {nombre}')
print("\n\n")

# 6)
print("Ejercicio 6 \n")
precio = 20000
print(f'precio = {precio}')
print("\n\n")

# 7)
print("Ejercico 7 \n")
descuento = 0.15
print(f'descuento = {descuento}')
print("\n\n")

# 8)
print("Ejercicio 8 \n")
precio_final = precio - (precio * descuento)
print(f'precio_final = {precio_final}')
print("\n\n")

# 9)
print("Ejercicio 9 \n")
cadena = "Gracias por su compra"
print(f'cadena = {cadena}')
print("\n\n")

# 10)
print("Ejercicio 10 \n")
longitud = len(cadena)
print(f'longitud = {longitud}')
print("\n\n")

# 11)
print("Ejercicio 11 \n")
precio = int(25.3)
print(f'precio = {precio}')
print("\n\n")

# 12)
print("Ejercicio 12 \n")
nombre = "Facundo"
apellido = "Ramirez"
nombre_completo = (f'{nombre} {apellido}')
print(f'Nombre: {nombre} \nApellido: {apellido} \nNombre Completo: {nombre_completo}')
print("\n\n")

# 13)
print("Ejercicio 13\n")
edad = 20
calc = edad + 5 - 10
print(f'edad = {edad}')
print(f'calc = {calc}')
print("\n\n")

# 14)
print("Ejercicio 14\n")
altura = float(1.75)
calc_alt = round((altura * 4) / 3, 2)
print(f'altura = {altura}')
print(f'calc_alt = {calc_alt}')
print("\n\n")

# 15)
print("Ejercicio 15\n")
nombre_mayusculas = "FACUNDO"
nombre_minusculas = nombre_mayusculas.lower() #Pasar nombre a minúscula

# Primer letra mayúscula
n = len(nombre_mayusculas)
mayuscula_primer_letra = nombre_mayusculas[0:1] + nombre_mayusculas[1:(n+1)].lower()

print(f'Nombre: {nombre_mayusculas}')
print(f'Nombre en minúscula: {nombre_minusculas}')
print(f'Primer letra en mayúscula: {mayuscula_primer_letra}')