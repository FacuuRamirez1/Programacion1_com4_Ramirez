import csv

# 2) Mostrar productos
#with open("productos.txt", "r") as archivo:
#    for linea in archivo:
#        nombre, precio, cantidad = linea.strip().split(",")
#        print(f'Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}')
#
# 3) Agregar producto
#with open("productos.txt", "a") as file:
#    new_producto = input('Ingrese los datos del producto en formato ("nombre, precio, cantidad"):').strip()
#    add_producto = new_producto.split(",")
#    writer = csv.writer(file)
#    writer.writerow(add_producto)
#    print("¡Producto agregado correctamente!")
#
# 4) Lista de diccionarios