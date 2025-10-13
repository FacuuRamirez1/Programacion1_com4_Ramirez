import csv

# ====== Función mostrar productos ======
def mostrar_productos():
    print("\n====== Productos Catálogo ======")
    try:
        with open("productos.csv", "r", newline="") as archivo:
            lector = csv.DictReader(archivo, fieldnames=["Producto","Precio"])
            for linea in lector:
                print(f'- {linea['Producto']}: ${linea['Precio']}')
    except FileNotFoundError as e:
        print(f'\nHa ocurrido un error: {e}\n')
    print()

# ====== Función Agregar Producto ======
def agregar_producto():
    print("\n====== Agregar produto ======")
    producto = input("Ingrese el nuevo producto: ")
    precio = input("Ingrese el precio del producto: ")
    try:
        with open('productos.csv', "a", newline="") as archivo:
            colum = ["Producto","Precio"]
            escritor = csv.DictWriter(archivo, delimiter=",", fieldnames=colum)
            escritor.writeheader()

            for linea in archivo:
                escritor.writerow(linea)
    except TypeError as e:
        print(f'\nHa ocurrido un error: {e}\n')
    print()


# ====== Función Eliminar Producto ======
def eliminar_producto():
    print("\n====== Eliminar producto ======")
    producto = input("Ingrese el nombre del producto: ")
    try:
        with open('productos.csv', "w", newline=""):
            escritor = csv.DictWriter.writerow("")
    except TypeError as e:
        print(f'\nHa ocurrido un error: {e}\n')
    print()