# ENTRADAS =  VARIABLES = REFERENCIAS EN MEMEORIA
nivelAgua = int(input("Digite el nivel de agua: "))

# PROCESO
if(nivelAgua >= 0 and nivelAgua < 20 ):
    # SALIDAS
    print(f'El nivel de agua es {nivelAgua} y este es bajo')    
elif(nivelAgua >= 20 and nivelAgua < 400):
    # SALIDAS
    print(f'El nivel de agua es {nivelAgua} operando normalmente')  
elif(nivelAgua >= 400):
    # SALIDAS
    print(f'El nivel de agua es {nivelAgua} Alerta! arriba de 400 metros')
else:
    # SALIDAS
    print(f'El nivel de agua no es válido...')
