# ENTRADAS =  VARIABLES = REFERENCIAS EN MEMEORIA
mesDigitado = input("Ingrese el mes del año")
mes = mesDigitado.lower()
# PROCESO
if(mes == "enero"  or  mes == "febrero" or mes == "marzo"):
    # SALIDAS
    print(f'La estación en la que se encuentra el mes {mes} es Invierno')
elif(mes == "abril"  or  mes == "mayo" or mes == "junio"):
    # SALIDAS
    print(f'La estación en la que se encuentra el mes {mes} es primavera')
elif(mes == "julio"  or  mes == "agosto" or mes == "septiembre"):
    # SALIDAS
    print(f'La estación en la que se encuentra el mes {mes} es verano')
elif(mes == "octubre"  or  mes == "noviembre" or mes == "diciembre"):  
    # SALIDAS
    print(f'La estación en la que se encuentra el mes {mes} es otoño')
else:
   # SALIDAS
    print(f'El mes no es válido...')