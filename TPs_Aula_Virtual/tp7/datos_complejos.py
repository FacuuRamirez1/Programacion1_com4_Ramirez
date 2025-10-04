print("Ejercicio 1")
precios_frutas = {"Banana":1200, "Ananá":2500, "Melón":3000, "Uva":1450}
print(f'Lista inicial: {precios_frutas}')

precios_frutas.update("Naranja",1200)
precios_frutas.update("Manzana",1500)
precios_frutas.update("Pera",2300)
print(f'Lista nueva: {precios_frutas}')


print("\nEjercicio 2")
precios_frutas.update(Banana=1330)
precios_frutas.update(Manzana=1700)
precios_frutas.update(Melón=2800)
print(f'Lista actualizada: {precios_frutas}')


print("\nEjercicio 3")
lista_frutas = list(precios_frutas.keys())
print(f'Lista de frutas: {lista_frutas}')


print("\nEjercicio 4")
contactos = {}

for i in range(5):
    nombre = input(f'Ingrese el nombre del contacto {i+1}: ')
    telefono = input('Ingrese el número de teléfono: ')
    contactos[nombre] = telefono

busc_contacto = input('Ingrese el nombre del contacto a buscar: ')
if busc_contacto in contactos:
    print(f'El númeor de teléfono de {busc_contacto} es {contactos[busc_contacto]}')
else:
    print(f'{busc_contacto} no se encuentra en los contactos.')


print("\nEjercicio 5")
frase = input('Ingrese una frase: ')
palabras_unicas = set(frase.split())
recuento = {palabra: frase.count(palabra) for palabra in palabras_unicas}

print(f'Palabras únicas: {palabras_unicas}')
print(f'Recuento: {recuento}')


print("\nEjercicio 6")
a,b,c = input('Ingrese los nombres de los alumnos (separados por comas): ').split(',')
alumnos = {a:(), b:(), c:()}
for alumno in alumnos:
    notas = []
    for i in range(3):
        nota = float(input(f'Ingrese la nota {i+1} de {alumno}: '))
        notas.append(nota)
    alumnos[alumno] = tuple(notas)

    for i in range(3):
        promedio = sum(alumnos[alumno])/3
        print(f'El promedio de {alumno} es {promedio:.2f}')


print("\nEjercicio 7")
aprob_p1 = {"Perez","Ramirez","Godoy","Guardati","Vargas","Deseff","Fernandez","Martinez","Gonzales","Días","Mariño","Masi"}
aprob_p2 = {"Ramirez","Godoy","Guardati","Vargas","Deseff","Fernandez"}
print("Alumnos que aprobaron ambos parciales:")
for alumno in aprob_p1.intersection(aprob_p2):
    print(f'- {alumno}')

print("Alumnos que aprobaron uno de los parciales:")
for alumno in aprob_p1.symmetric_difference(aprob_p2):
    print(f'- {alumno}')

lista_aprob1 = aprob_p1.symmetric_difference(aprob_p2)
print("Lista de alumnos que aprobaron uno de los parciales:")
print(lista_aprob1)


print("\nEjercicio 8")
productos = {"Pizzas":10, "Hamburguesas":20, "Panchos":45, "Sanguchitos":15, "Papas":35}
print(f'productos: {list(productos.keys())}')

while True:
    print("1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar producto")
    print("4. Salir")
    opc = int(input("Elija una opción:"))

    if opc == 1:
        busc_p = input("Ingrese el nombre del producto: ")
        if busc_p in productos:
            print(f'Stock de {busc_p}: {productos[busc_p]}')
        else:
            print(f'El producto {busc_p} no se encuentra en el stock.')
    elif opc == 2:
        busc_p = input("Ingrese el nombre del producto: ")
        if busc_p in productos:
            cant = int(input("Ingrese la cantidad a agregar: "))
            productos[busc_p] += cant
            print(f'Producto {busc_p} - Nuevo stock: {productos[busc_p]}')
        else:
            print(f'El producto {busc_p} no se encuentra en el stock.')
    elif opc == 3:
        agregar_p = input("Ingrese el nombre del producto a agregar: ")
        if agregar_p in productos:
            print(f'El producto {agregar_p} ya se encuentra en el stock.')
        else:
            cant = int(input("Ingrese la cantidad a agregar: "))
            productos[agregar_p] = cant
            print(f'Producto {agregar_p} agregado con stock {cant}.')
    elif opc == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Error, ingrese una opción válida")


print("\nEjercicio 9")
agenda = {
    ("Lunes", "08:00"): "Programación 1",
    ("Lunes", "10:00"): "Sistemas Operativos",
    ("Martes", "08:00"): "Matemática",
    ("Martes", "10:00"): "Organización Empresarial",
    ("Miércoles", "08:00"): "Matemática",
    ("Jueves", "08:00"): "Programación 1",
}

print("¡Agenda de cursado presencial!")
dia, hora = input("Ingrese día y hora a consultar (en formato: Día, HH:MM): ").split(", ")
if (dia, hora) in agenda:
    print(f'Clase programada: {agenda[(dia, hora)]}')
else:
    print("No hay clases presenciales programadas en ese día y hora.")


print("\nEjercicio 10")
paises_capitales = {"Argentina":"CABA", "España":"Madrid", "Chile":"Santiago", "EEUU":"Washington DC", "Alemania":"Berlín", "Bélgica":"Bruselas", "Francia":"París", "Reino Unido":"Londres", "Portugal":"Lisboa"}
print(f'Países y capitales: {paises_capitales}')

capitales_paises = {}
for pais, capital in paises_capitales.keys():
    capitales_paises[capital] = pais
print(f'Capitales y países: {capitales_paises}')