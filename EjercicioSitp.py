#CONDICIONAL

# Leemos el tipo de tarjeta y el saldo actual
tipo_tarjeta = input("¿Es personalizada la tarjeta? (s/n): ")
saldo_actual = float(input("Ingrese el saldo actual en la tarjeta: "))
saldo_final=0

# Verificamos si el saldo es suficiente para pagar el pasaje
if saldo_actual >= 2750:
    pago=saldo_actual-2750
    print("Pago exitoso. \n Puede ingresar al bus!!!")
    saldo_final =pago
else:
    # Si la tarjeta es personalizada y no tiene suficiente saldo, se genera un préstamo
    if tipo_tarjeta == "s":
        prestamo = saldo_actual-2750
        
        print("Recargue su tarjeta antes de la siguiente subida" ,prestamo)
        saldo_final = prestamo
    else:
        print("Saldo insuficiente!!! \n No puede ingresar al bus.")
        pago=saldo_actual
        saldo_final = saldo_actual

# Imprimimos el saldo final de la tarjeta
print("Saldo final de la tarjeta:", saldo_final)
