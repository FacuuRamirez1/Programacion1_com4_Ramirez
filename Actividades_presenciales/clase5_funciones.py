# ---------- Funciones ----------

# Función para sumar los dígitos de un número ingresado por un usuario
def sum_digitos(num):
    sum = 0
    num1 = num
    while num1 != 0:
        digito = num1 % 10
        sum += digito
        num1 //= 10
        
    return print(f'La suma de los dígitos de {num} es: {sum}\n')

# Función para sumar números ingresados por el usuario
def sum_numeros(nums_guardados: list): 
    n = len(nums_guardados)
    sum = 0
    for i in range(n):
        sum += nums_guardados[i]
    return sum

# ---------- Programa principal ----------
nums_guardados = []

while True:
    num = int(input("Ingrese un número entero positivo (0 para terminar): "))
    if num == 0:
        print(f'\nLa suma de los números ingresados es: {sum_final}')
        break
    else:
        sum_digitos(num)
        nums_guardados.append(num)
        sum_final = sum_numeros(nums_guardados)