## BINGO de 5x5 con números aleatorios entre 1 y 50, sin repetirse.
#
#import random
#from random import choice
#
## variables y listas
#num = random.sample(range(1,51), 25)
#carton = [num[i*5:(i+1)*5] for i in range(5)]
#carton_lleno = False
#
## Mostrar cartón usuario
#print("Tu cartón es el siguiente:")
#for i in range(5):
#    print(carton[i])
#
#while not carton_lleno:
#    num_rand = random.randint(1,51)
#    print(f'Salió el número: {num_rand}!')
#
#    while True:
#        encontrado = False
#        for i in range(5):
#            for j in range(5):
#                if carton[i][j] == num_rand:
#                    carton[i][j] = 0
#                    encontrado = True
#
#        if encontrado:
#            print(f'El número {num_rand} está en tu cartón!')
#        else:
#            print("No tienens este número")
#
#        print("Cartón actualizado:")
#        for i in range(5):
#            for j in range(5):
#                if j != 0:
#                    print(f'{j:2}', end=" ")
#                else:
#                    print(" 0", end=" ")
#            print()
#        print()
#    
#        for i in carton:
#            if i.count(0) == 5:
#                print("Línea!\n")
#                break
#        
#        carton_lleno = True
#        for i in carton:
#            for j in i:
#                if j != 0:
#                    carton_lleno = False
#
#print("BINGO! Felicitaciones, has ganado!")

import random


num = random.sample(range(1, 51), 25)
carton = []
carton = [num[i*5:(i+1)*5] for i in range(5)]
numeros_sorteados = []
carton_lleno = False

print("Bienvenido al BINGO!\n")

# Mostrar el cartón del usuario
print("Cartón actual:")
for i in range(5):
    print(carton[i])
    

while not carton_lleno:
    while True:
        num_sort = random.randint(1, 50)
        if num_sort not in numeros_sorteados:
            numeros_sorteados.append(num_sort)
            break

    print(f"\nSalió el número: {num_sort}\n")

    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == num_sort:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print("¡El número está en tu cartón!\n")
    else:
        print("No tienes este número.\n")

    print("Cartón actual:")
    for i in range(5):
        print(carton[i])

    for i in carton:
        if i.count(0) == 5: # count() sirve para ver cuantas veces está un número en una lista
            print("¡Línea!\n")
            break

    carton_lleno = True
    for i in carton:
        for j in i:
            if j != 0:
                carton_lleno = False

print("¡Bingo! ¡Felicidades, has ganado!")