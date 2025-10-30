import os

productos = []

if os.path.exists("productos.txt") and os.path.getsize("productos.txt") > 0:
    with open("productos.txt", "r", encoding="utf-8") as catalogo:
        next(catalogo)
        for producto in catalogo:
            producto = producto.strip()
            if len(producto) == 0:
                continue
            producto = producto.split(",")
            cargar_p = {
                "nombre":producto[0],
                "precio":float(producto[1]),
                "cantidad":int(producto[2])
            }
            productos.append(cargar_p)

while True:
    print("")
    print("=========================")
    print("  CATÁLOGO DE PRODUCTOS  ")
    print("=========================")

    print("1. Escribir nueva lista")
    print("2. Agregar producto")
    print("3. Ver catálogo")
    print("4. Buscar producto")
    print("5. Salir")
    opc = int(input("Elija una opción: "))

    try:
        if opc == 1:
            print("\n  Escribir nueva lista  ")
            print("------------------------")
            n = int(input("¿Cuántos productos desea agregar? "))
            try:
                productos.clear()
                with open("productos.txt", "w", encoding="utf-8") as catalogo:
                    catalogo.write("nombre,precio,cantidad\n")
                    for i in range(n):
                        producto = input('Ingrese el producto en formato "nombre,precio,cantidad": ').strip().split(",")
                        if len(producto) == 3:
                            catalogo.write(f'{producto[0]},{producto[1]},{producto[2]}\n')
                            new_p = {
                                "nombre":producto[0],
                                "precio":float(producto[1]),
                                "cantidad":int(producto[2])
                            }
                            productos.append(new_p)
                            print("✅¡Productos agregados correctamente!")
                        else:
                            print("❌¡Error! Ingrese el producto con el formato correcto")
                    
            except ValueError:
                print("❌¡Error! Debe ingresar un número.")
            except Exception as e:
                print(f'❌¡Error inesperado! {e}')

        elif opc == 2:
            print("\n  Agregar un producto  ")
            print("-----------------------")
            try:
                if os.path.exists("productos.txt") and os.path.getsize("productos.txt") == 0:
                    with open("productos.txt", "a", encoding="utf-8") as catalogo:
                        producto = input('Ingrese el nuevo producto en formato "nombre,precio,cantidad": ').strip().split(",")
                        if len(producto) == 3:
                            new_p = {
                                "nombre":producto[0],
                                "precio":float(producto[1]),
                                "cantidad":int(producto[2])
                            }
                            productos.append(new_p)
                            catalogo.write("nombre,precio,cantidad\n")
                            catalogo.write(f'{producto[0]},{producto[1]},{producto[2]}\n')
                        else:
                            print("❌¡Error! Ingrese el producto con el formato correcto")
                else:
                    with open("productos.txt", "a", encoding="utf-8") as catalogo:
                        producto = input('Ingrese el nuevo producto en formato "nombre,precio,cantidad": ').strip().split(",")
                        if len(producto) == 3:
                            new_p = {
                                "nombre":producto[0],
                                "precio":float(producto[1]),
                                "cantidad":int(producto[2])
                            }
                            productos.append(new_p)
                            catalogo.write(f'{producto[0]},{producto[1]:.2f},{producto[2]}\n')
                        else:
                            print("❌¡Error! Ingrese el producto con el formato correcto")

            except FileNotFoundError:
                print("❌¡Error! El archivo no existe")
            except Exception as e:
                print(f'❌¡Error inesperado! {e}')

        elif opc == 3:
            if os.path.getsize("productos.txt") == 0:
                print("❌¡Error! El archivo se encuentra vacío")
            else:
                try:
                    print("\n  Ver catálogo  ")
                    print("----------------")

                    with open("productos.txt", "r", encoding="utf-8") as catalogo:
                        for producto in catalogo:
                            producto = producto.strip().split(",")
                            print(f'{producto[0]} | {producto[1]:.2f} | {producto[2]}')

                except FileNotFoundError:
                    print("❌¡Error! Ocurrió un error al abrir el archivo")
                except Exception as e:
                    print(f'❌¡Error inesperado! {e}')
            
        elif opc == 4:
            if os.path.getsize("productos.txt") == 0:
                print("❌¡Error! El archivo se encuentra vacío")
            else:
                try:
                    print("\n  Buscar producto  ")
                    print("-------------------")

                    busc_p = input("Ingrese el nombre del producto: ").upper()
                    p_encontrado = False
                    for i in productos:
                        if i["nombre"].upper() == busc_p:
                            print("\n  Información del producto  ")
                            print("----------------------------")
                            print(f'- Nombre: {i["nombre"]}')
                            print(f'- Precio: ${i["precio"]:.2f}')
                            print(f'- Cantidad: ${i["cantidad"]}')
                            p_encontrado = True
                    
                    if not p_encontrado:
                        print("❌¡Error! Producto no encontrado")
            
                except FileNotFoundError:
                    print("❌¡Error! No se pudo abrir el archivo")
                except Exception as e:
                    print(f'❌¡Error inesperado! {e}')

        elif opc == 5:
            print("\nSaliendo del programa...")
            break

        else:
            print("❌¡Error! Ingrese una opción válida.")
    
    except ValueError:
        print("❌¡Error! Debe ingresar un número.")
    except Exception as e:
        print(f'❌¡Error inesperado! {e}')