import random
saldo_disponible = 4500
intentos = 4
 

while intentos > 0:
    celular = input("Ingresa tu número de celular: ")
    clave = input("Ingresa tu clave de 4 dígitos: ")
    if celular == "3112483372" and clave == "1234": 
        print("Bienvenido a Nequi!!")
        print("Tu saldo disponible es de:" ,saldo_disponible)
        break
    intentos -= 1
    print("¡Upps! Parece que tus datos de acceso no son correctos.")
    if intentos > 0:
        print("Tienes", intentos, "intentos más.")
    else:
        print("No tienes mas intentos. El sistema se bloqueara durante 1 hora!!")
        exit()
while True:
    print("\n¿Que operacion desea realizar?\n")
    print("1. saca \n")
    print("2. enviar \n")
    print("3. recargar \n")
    print("4. Servicios \n")
    print("5. salir \n")
    
    opcion = input("Ingresa el número de opción: ")
    if opcion == "1":
        print("\n¿Donde quiere hacer el retiro: ?\n")
        print("1. Cajero\n")
        print("2. punto fisico\n")
        retirar = input("Ingresa el numero de opcion: ")
        if saldo_disponible < 2000:
            print("No te alcanza para hacer el retiro.")
        else:
            monto = int(input("Ingrese la cantidad a retirar: "))
            if monto <=saldo_disponible:
                saldo_disponible -= monto
                codigo_retiro = random.randint(000000, 999999)
                print("Tu Codigo:" ,codigo_retiro,",Tienes 30 minutos para hacer el retiro!!!!")
                print ("Retiro exitoso. Tu nuevo saldo es de: ",saldo_disponible)
            else:
                print("No tienes suficiente saldo para hacer el retiro.")
                
    elif opcion == "2":
        celular_destino = input("Ingresa el número de celular al que deseas enviar dinero: ")
        monto = int(input("Ingresa el monto a enviar: "))
        if monto <= saldo_disponible:
            saldo_disponible -= monto
            print("Envío exitoso. Tu nuevo saldo es de: "  ,saldo_disponible)
        else:
            print("No tienes suficiente saldo para hacer el envío.")
            
    elif opcion == "3":
        monto = int(input("Ingresa el monto a recargar: "))
        recargar = input("¿Estás seguro que deseas hacer la recarga? (s/n): ")
        if recargar == "s":
            saldo_disponible += monto
            print("Recarga exitosa. Tu nuevo saldo es de:" ,saldo_disponible)
        else:
            print("Recarga cancelada.")
    elif opcion == "4":
        print("¿Que servicio desea pagar : \n 1.agua \n  2.luz \n  3.gas ? \n")
        servicios = input("Ingrese una opcion: " )
        pago = input("¿Estás seguro que deseas hacer el pago: ? (s/n): ")
        valor = int(input("Ingresa el valor a pagar: "))
        if valor <= saldo_disponible:
            saldo_disponible -= valor
            print("Pago de la Factura con Exito.!! Tu nuevo saldo es de: "  ,saldo_disponible)
        else:
            print("No tienes suficiente saldo para hacer el Pago.")
            
    elif opcion == "5":
        salir = input("¿Estás seguro que quieres salir de Nequi? (s/n): ")
        if salir == "s":
            print("Adiós.")
            exit()
        
    else:
        print("Opción no válida. Inténtalo de nuevo.")
    
 


