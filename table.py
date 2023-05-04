num=int(input("Ingrese el numero del uno al diez para obtener su tabla de multiplicar: \n"))
if num <1 or num>10:
    print("Error el numero debe estar entre el 1 y el 10")
else:
    print(f"tabla de multiplicar del {num} en orden inverso: ")
    for i in range (10, 0, -1):
        print(f"{num} x {i} = {num * i}")
    print(f"Tabla de multiplicar de {num} en orden correcto:")