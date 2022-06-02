def impresion(lista,num):
  if num==1:
    for renglon in lista:
        for config in renglon:
            numero=int(config[0])   
            caracter=config[1]
            print(numero*caracter,end="")
        print()


def impresion_avatar(lista):
  for rostro in lista:
    for renglon in rostro:
        for config in renglon:
            numero=int(config[0])   
            caracter=config[1]
            print(numero*caracter,end="")
        print()

def grabar_avatar_archivo(lista,nombre):

  file=open("texto.txt","a",encoding="utf-8")
  file.write("\n"+"INICIO USUARIO "+nombre)
  for rostro in lista:
    for renglon in rostro:
        file.write("\n")
        for config in renglon:
         numero=config[0]   
         caracter=config[1]
         file.write(numero)
         file.write("Q")
         file.write(caracter)
         file.write("Q")
  file.write("\n"+"FIN USUARIO "+nombre)
  file.close()

def leer_avatar_archivo(nombre):

  lista=[]
  file=open("texto.txt","r",encoding="utf-8")
  file.readline()
  datafile = file.readlines()
  for line in datafile:
    if "INICIO" in line and nombre in line:
      continue
    elif "FIN" in line:
      break
    else:
      config=[]
      dato=""
      for caracter in line:
        if "\n" in caracter or "Q" in caracter:
          config.append(dato)
          continue
       # elif "Q" in caracter:
       #   config.append(dato)
       #   continue 
        else: 
          if caracter.isdigit():
            dato += caracter
            continue
          else:
            dato = caracter
            continue
          #config.append(dato)
      lista.append(config)

  file.close()
