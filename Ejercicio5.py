
tipoGasolina=input("Ingrese el tipo de gasolina a tanquear: corriente, diesel")
vtanquear=int(input("Ingrese el valor a tanquear: "))

if tipoGasolina=="corriente":
    corriente=10800
    galones=vtanquear/corriente
    print("los galones tanqueados"+galones)
elif tipoGasolina=="diesel":
    diesel=9800
    galones=vtanquear/diesel
    print("los galones tanqueados"+galones)
else:
    print("el tipo de gasolina no es valido")