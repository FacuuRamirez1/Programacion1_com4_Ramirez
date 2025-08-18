# 1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
print("")
print("Imprimir Hola Mundo!")
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
print("")
print("")
print("Saludar al usuario!")
print("")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
print("")
print("")
print("Pedir información al usuario!")
print("")
nombre_apellido = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"{nombre_apellido} tiene {edad} años, actualmente recide en {lugar_de_residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
print("")
print("")
print("Calcular Área y perímetro!")
print("")
pi = 3.14159 #aproximación de PI

radio = int(input("Ingrese la longitud del radio en cm: "))
area = round(float(pi * (radio ** 2)), 3)
perimetro = round(float(2 * pi * radio), 3)
print(f"Para un círculo con un radio de {radio}cm.")
(print(f"El área es de {area}cm."))
(print(f"Y el perímetro es de {perimetro}cm."))

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
print("")
print("")
print("Pasar de segundos a hora!")
print("")
seg = int(input("Ingrese los segundos deseados: "))
convert_hora = round(seg / 3600, 3)
print(f"{seg} segundos son equivalentes a {convert_hora} hora/s.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
print("")
print("")
print("Tablas del número elegido!")
print("")
i = 0
x = int(input("Ingrese un número deseado: "))
while (i <= 10):
    res = x * i
    print(f"{x} * {i} = {res}")
    i = i + 1

# 7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("")
print("")
print("Operaciones de números elegidos!")
print("")
x = int(input("Ingrese el primer número (distinto de 0): "))
y = int(input("Ingrese el segundo número (distinto de 0): "))

res_sum = x + y
res_rest = x - y
res_mult = x * y
res_div = x / y

print("Los resultados de las operaciones son:")
print(f"Suma: {res_sum},   Resta: {res_rest},   Multiplicación: {res_mult},   División: {res_div}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("")
print("")
print("Calcular Indice de Masa Corporal!")
print("")
peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en mts: "))

imc = round(peso / altura ** 2, 2)

print(f"Su indice de masa corporal es de {imc}kg/m^2.")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("")
print("")
print("Pasar de grados Celsius a grados Fahrenheit!")
print("")
temp_c = int(input("Ingrese la temperatura en Celsius: "))
temp_f = round((9/5) * temp_c + 32, 2)

print(f"{temp_c}°C (Celsius) son equivalentes a {temp_f}°F (fahrenheit).")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("")
print("")
print("Calcular promedio de 3 números!")
print("")
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número:"))
z = int(input("Ingrese el tercer número:"))
promedio = round((x + y + z) / 3, 2)

print(f"El promedio de los números {x}, {y}, {z} es igual a {promedio}.")