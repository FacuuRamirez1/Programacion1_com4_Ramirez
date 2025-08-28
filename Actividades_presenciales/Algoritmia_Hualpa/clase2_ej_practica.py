# Ejercicio 3 — Evaluación de crédito bancario

nombre_apellido = input("Ingrese su nombre y apellido: ")
cuit = (input("Ingrese su cuit/cuil (formato xx-xxxxxxxx-x): ").strip().split("-"))
ing_mensuales = float(input("Ingrese sus ingresos mensuales: "))
ant_laboral = int(input("Ingrese su antigüedad laboral (en años): "))
hist_crediticio = input("Ingrese su historial crediticio (bueno / regular / malo): ").lower()
opc_hist = ["bueno", "regular", "malo"]

# Validar CUIT
def validar_cuit (cuit):
    principio_valido = ["20", "23", "24", "27"]
    if len(cuit) != 3:
        return "CUIT inválido (formato incorrecto)"
    if cuit[0] not in principio_valido:
        return "CUIT inválido (primeros dígitos incorrectos)"
    if len(cuit[1]) != 8 or not cuit[1].isdigit():
        return "CUIT inválido (parte del medio incorrecta)"
    if len(cuit[2]) != 1 or not cuit[2].isdigit():
        return "CUIT inválido (último dígito incorrecto)"
    return f"{cuit[0]}-{cuit[1]}-{cuit[2]}"

# def conseguir préstamo
def calif_cliente (ingresos, antiguedad, historial):
    if historial not in opc_hist:
        return "Historial inválido"
    if ingresos < 200000 or hist_crediticio == "malo":
        return "rechazado"
    if ingresos >= 200000 and antiguedad >= 2:
        if historial == "bueno":
            return "$3.000.000"
        elif historial == "regular":
            return "$1.000.000"
        else:
            return "$500.000"
    else:
        return "$500.000"

print(f'✔ Cliente: {nombre_apellido}')
print(f'CUIT: {validar_cuit(cuit)}')
print(f'Ingresos: ${ing_mensuales}')
print(f'Antigüedad: {ant_laboral} años')
print(f'Historial: {hist_crediticio}')
print(f'Monto aprobado: {calif_cliente(ing_mensuales, ant_laboral, hist_crediticio)}')
