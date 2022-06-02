import cabellos as cab
import funciones as fun
import ojosorejas as ojor
#import Nariz as na
import boca as bo
##mport Cuello as cu

print("BIENVENIDO AL JUEGO. PARA CONTINUAR DEBES SELECCIONAR TU AVATAR\n\n")

print("SELECCIONE SU TIPO DE CABELLO: \n")
print("1.Gorro de Lana:\n")	
fun.impresion(cab.cabello_opcion1(),1)
print("\n2. Punkero:\n")
fun.impresion(cab.cabello_opcion2(),1)
print("\n3. Pluma Blanca:\n")
fun.impresion(cab.cabello_opcion3(),1)
print("\n4. Alemán:\n")
fun.impresion(cab.cabello_opcion4(),1)

opcion=int(input("Ingresa la opción"))
lista_tempo=[]
if opcion == 1:
    lista_tempo.append(cab.cabello_opcion1())
elif opcion == 2:
    lista_tempo.append(cab.cabello_opcion2())
elif opcion == 3:
    lista_tempo.append(cab.cabello_opcion3())
else:
    lista_tempo.append(cab.cabello_opcion4())


print("SELECCIONE SU TIPO DE OJOS: \n")
print("1.Gorro de Lana:\n")	
fun.impresion(ojor.ojo_opcion1(),1)
print("\n2. Punkero:\n")
fun.impresion(ojor.ojo_opcion2(),1)
print("\n3. Pluma Blanca:\n")
fun.impresion(ojor.ojo_opcion3(),1)
print("\n4. Alemán:\n")
fun.impresion(ojor.ojo_opcion4(),1)

opcion=int(input("Ingresa la opción"))
print()
if opcion == 1:
    lista_tempo.append(ojor.ojo_opcion1())
elif opcion == 2:
    lista_tempo.append(ojor.ojo_opcion2())
elif opcion == 3:
    lista_tempo.append(ojor.ojo_opcion3())
else:
    lista_tempo.append(ojor.ojo_opcion4())

print("---------------------------")
print("ASI VA TU MUÑECO")
print(fun.impresion_avatar(lista_tempo))

nombre=input("\nAhora elije un nombre para tu hermosa criaturita!: ")

fun.grabar_avatar_archivo(lista_tempo,nombre)

nombre=input("--Ingresa tu nombre de jugador---")
fun.leer_avatar_archivo(nombre)
