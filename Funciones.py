def impresion(lista,num):
  if num==1:
    for renglon in lista:
        for config in renglon:
            numero=int(config[0])   
            caracter=config[1]
            print(numero*caracter,end="")
        print()