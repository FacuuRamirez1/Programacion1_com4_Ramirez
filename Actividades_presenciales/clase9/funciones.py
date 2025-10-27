import csv

# =============
#   FUNCIONES
# =============

# Cargar herramientas al csv
def Cargar_herramientas(nom, cant, prec):
    with open("herramientas.csv", "a", encoding="utf-8") as catalogo:
        new_product = {
            "nombre" : {nom},
            "cantidad" : {cant},
            "precio" : {prec}
        }

        writer = csv.DictWriter(catalogo)
        writer.writerow(new_product)
        print("¡Producto agregado correctamente!")
        return (
            new_product
        )

# Mostrar herramientas del csv
def Mostrar_herramientas():
    with open("herramientas.csv", "r", encoding="utf-8") as catalogo:
        if len(catalogo) != 0:
            print(" === Catálogo de Herramientas ===")
            for linea in catalogo:
                cosas = linea.split(",")
                print(f'- {cosas[0], cosas[1], cosas[2] }')
        else:
            print("!Error¡ El catálogo está vacío.")

# Modificar herramienta existente
#def Modificar_herramientas(nom):
