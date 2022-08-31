# ENTRADAS =  VARIABLES = REFERENCIAS EN MEMEORIA
edad = int(input("Ingrese la edad"))

# PROCESO
if(edad < 0 and edad >= 101):
    # SALIDAS
    print(f'la edad {edad} es inválida ')
elif(edad >= 0 and edad <= 14) :
    # SALIDAS
    print(f'la edad {edad} corresponde a una persona niña')
elif(edad >= 15 and edad <= 28) :
    # SALIDAS
    print(f'la edad {edad} corresponde a una persona joven')
elif(edad >= 29 and edad <= 60) :
    # SALIDAS
    print(f'la edad {edad} corresponde a una persona adulta ')
elif(edad >= 61 and edad <= 100) :
    # SALIDAS
    print(f'la edad {edad} corresponde a una persona adulta mayor')
else:
    # SALIDAS
    print(f'la edad {edad} es inválida ')
