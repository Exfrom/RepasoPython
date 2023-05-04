presupuesto=100000
num_gastos=0
total_gastos=0

while num_gastos<3:
    accion=input("¿Desea restistar un gasto (1): o desea capturar un valor (2): ?:\n   ")
    num_gastos += 1
    if accion =="1":
        gasto = float(input("¿ingrese el valor del gasto: "))
        total_gastos += gasto
        presupuesto -= gasto
        print("Usted ha gastado" ,gasto, "su presupuesto actual es de" ,presupuesto)
    elif accion == "2":
        valor = float(input("Ingrese el valor a capturar: "))
        presupuesto += valor
        print("Su presupuesto actual es de:" ,presupuesto)
    else:
        print("Opción inválida, por favor intente de nuevo.")
    print("Usted ha gastado un total de" ,total_gastos, "Su presupuesto final es de: " ,presupuesto)