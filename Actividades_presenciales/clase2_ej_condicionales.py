# Separar fecha en tres variables ()
fecha = input("Ingrese la fecha de la siguiente manera dia, DD/MM: ")
partes = fecha.split(",")
if len(partes) != 2:
    print("ERROR, respetar formato de fecha pedido.")
dia = partes[0].strip().lower()

fecha_num = partes[1].strip()
partes_fecha = fecha_num.split("/")
if len(partes_fecha) != 2:
    print("ERROR, respete el formato pedido.")

semana = ["lunes","martes","miércoles","jueves","viernes"] # Lista con los días de la semana

dd = int(partes_fecha[0])
mm = int(partes_fecha[1])

if (dia not in semana or (dd < 1 or dd > 31) or (mm < 1 or mm > 12)): # Si los valores ingresados no son válidos
    print ("Ha ocurrido un error.")
elif (dia == semana[0] or dia == semana[1] or dia == semana[2]): # Condición para exámenes
    if (dia == semana[0]): # Condición para nivel inicial
        print("\nNivel Inicial! \n")
        aprobados = int(input("Ingrese el número de aprobados: "))
        desaprobados = int(input("Ingrese el número de desaprobados: "))
        porcentaje_aprob = (aprobados * 100) / (aprobados + desaprobados)
        print(f'El porcentaje de aprobados en el nivel inicial es del: {round(porcentaje_aprob, 2)}%')
    elif (dia == semana[1]): # Condición para nivel intermedio
        print("\nNivel Intermedio! \n")
        aprobados = int(input("Ingrese el número de aprobados: "))
        desaprobados = int(input("Ingrese el número de desaprobados: "))
        porcentaje_aprob = (aprobados * 100) / (aprobados + desaprobados)
        print(f'El porcentaje de aprobados en el nivel inicial es del: {round(porcentaje_aprob, 2)}%')
    elif (dia == semana[2]): # Condición para nivel avanzado
        print("\nNivel Avanzado! \n")
        aprobados = int(input("Ingrese el número de aprobados: "))
        desaprobados = int(input("Ingrese el número de desaprobados: "))
        porcentaje_aprob = (aprobados * 100) / (aprobados + desaprobados)
        print(f'El porcentaje de aprobados en el nivel inicial es del: {round(porcentaje_aprob, 2)}%')
    else: pass
elif (dia == semana[3]): # Condición de práctica hablada
    print("\nPráctica hablada! \n")
    asistencia = input("Ingrese el porcentaje de asistencia: ")
    asistencia = float(asistencia.split("%")[0])
    if (asistencia > 50):
        print("Asistió a la mayoría")
    elif (asistencia <= 50):
        print("No asistió a la mayoría")
elif (dia == semana[4]): # Condición de inglés para viajeros
    print("\nInglés para viajeros! \n")
    if ((dd == 1 and mm == 1) or (dd == 1 and mm == 7)):
        print("Comienzo de nuevo ciclo!")
        alumnos_inscriptos = int(input("Ingrese la cantidad de alumnos: "))
        arancel = int(input("Ingrese el monto del arancel: "))
        monto_total = alumnos_inscriptos * arancel
        print(f'El ingreso total es de ${monto_total}')
    else: pass