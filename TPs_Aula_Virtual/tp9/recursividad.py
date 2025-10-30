# 1) Calcular factorial de un número y los que se encuentran dentro:
print("===============")
print("  Ejercicio 1  ")
print("===============")

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Ingrese un número entero positivo: "))
for i in range(1, num + 1): 
    print(f'El factorial de {i} es: {factorial(i)}')

# 2)
print("\n===============")
print("  Ejercicio 2  ")
print("===============")

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
num = int(input("Ingrese un número entero positivo: "))
for i in range(num):
    print(f'Fibonacci({i}) = {fibonacci(i)}')

# 3)
print("\n===============")
print("  Ejercicio 3  ")
print("===============")

def potencia(num, e):
    if e == 0:
        return 1
    else:
        return num * potencia(num, e-1)
    
num = int(input("Ingrese un número entero positivo: "))
e = int(input(f'¿A qué número desea elevar a {num}? '))
potencia(num,e)

# 4)
print("\n===============")
print("  Ejercicio 4  ")
print("===============")

def pasar_a_bin(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return pasar_a_bin(num // 2) + str(num % 2)

num = int(input("Ingrese un númmero decimal, entero, positivo: "))
print(f'El número {num} en binario es: {pasar_a_bin(num)}')


# 5)
print("\n===============")
print("  Ejercicio 5  ")
print("===============")

def es_palindromo(palabra):
    if len(palabra) == 1:
        return True
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Por favor ingrese una palabra(sin espacios ni tildes): ").split("")
es_palindromo(palabra)


# 6)
print("\n===============")
print("  Ejercicio 6  ")
print("===============")

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (num % 10) + suma_digitos(num//10)

numero = int(input("Ingrese un número entero positivo: "))
print(f'La suma de los dígitos de {numero} es: {suma_digitos(numero)}')


# 7)
print("\n===============")
print("  Ejercicio 7  ")
print("===============")

def contar_bloques(n):
    if n == 0:
        return n
    else:
        return n + contar_bloques(n-1)
    
num = int(input("Ingrese un número entero positivo: "))
print(f'({contar_bloques(num)})')


# 8)
print("\n===============")
print("  Ejercicio 8  ")
print("===============")

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    
    ultimo = numero % 10
    
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else: 
        return 0 + contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito entre 0 y 9: "))
print(f'El número {numero} tienen {contar_digito(numero,digito)} dígitos.')