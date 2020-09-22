import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as ctrl
assert config
from time import process_time
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# _________________
#  Ruta a los archivos
# _________________

DetailsSmall = "Movies/SmallMoviesDetailsCleaned.csv"
DetailsLarge = "Movies/AllMoviesDetailsCleaned.csv"
CastingSmall = "Movies/MoviesCastingRaw-small.csv"
CastingLarge = "Movies/AllMoviesCastingRaw.csv"
 
# _________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# _________________
# _________________
#  Menu principal
# _________________
def menu():
    print("\nBienvenido")
    print("1- Cargar información del catálogo")
    print("2- Descubrir productoras de cine")
    print("3- Descubrir trabajo de un director")
    print("4- Descubrir Actor")
    print("5- Descubrir género")
    print("6- Descubrir país")
    print("0- Salir de la aplicación")

cont = None
while True:
        menu()
        opcion = input('Selecciona una opción para continuar: ')
        if len(opcion[0]) > 0:
            if int(opcion[0]) == 1:
                print("Menú de opciones")
                print("1- Cargar archivos pequeños")
                print("2- Cargar archivos grandes")
                tamaño = int(input("Digita su selección para el tamaño de los archivos CSV: "))
                t1_start = process_time() #tiempo inicial
                if tamaño == 1:
                    cantidad = 2001
                    factor_de_carga = 0.5
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.crearCatalogo(cantidad,factor_de_carga)
                    print("Cargando información de los archivos .....")
                    ctrl.cargarDatos(cont,CastingSmall, DetailsSmall)
                    print('Películas (detalles) cargadas: ' + str(ctrl.moviesDetailsSize(cont)))
                    print('Películas (Casting) cargadas: ' + str(ctrl.moviesCastingSize(cont)))
                elif tamaño == 2:
                    cantidad = 329047
                    factor_de_carga = 3
                    print("Inicializando Catálogo ....")
                    # cont es el controlador que se usará de acá en adelante
                    cont = ctrl.crearCatalogo(cantidad,factor_de_carga)
                    print("Cargando información de los archivos .....")
                    ctrl.cargarDatos(cont,CastingLarge, DetailsLarge)
                    print('Películas (detalles) cargadas: ' + str(ctrl.moviesDetailsSize(cont)))
                    print('Películas (Casting) cargadas: ' + str(ctrl.moviesCastingSize(cont)))
                else:
                    print("Opción inválida.....")
                t1_stop = process_time() #tiempo final
                print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

            elif int(opcion[0]) == 2:
                if cont == None:
                    print("Debe cargar el archivo primero")
                else:
                    name = input('Digite el nombre de la compañía: ')
                    data = ctrl.descubrirProductorasDeCine(cont,name)
                    if data == -1:
                        print("Criterio equivocado")
                    else:
                        print('Nombres de peliculas para la compañia ',name,':')
                        for i in range(data[2]):
                            print(i+1,' - ',lt.getElement(data[0],i)['original_title'])
                        print('El promedio para las peliculas para la compañia ',name,' es de: ',round(data[1],2))
                        print('Para un total de ',data[2],' peliculas')
            elif int(opcion[0])==3:
                if cont==None:
                    print("Debe cargar el archivo primero")
                else:
                    director=input("Digite el nombre del director: ")
                    datos=ctrl.descubrir_director(cont,director)
                    if datos==None:
                        print("Criterio equivocado")
                    else:
                        print("Las películas del director "+str(director)+" son: ")
                        contar=0
                        while contar<datos[2]:
                            print(str(contar+1)+" - "+datos[0][contar])
                            contar+=1
                        print("Para un total de películas de: ",datos[2])
                        print("Para un promedio de: ",round(datos[1],2))
            elif int(opcion[0])==4:
                if cont==None:
                    print("Debe cargar el archivo primero")
                else:
                    actor=input("Digite el nombre del actor: ")
                    datos=ctrl.buscar_por_actor(cont,actor)
                    if datos==None:
                        print("Criterio equivocado")
                    else:
                        print("Las películas en las que ha participado el actor "+str(actor)+" son: ")
                        contador=0
                        while contador<datos[3]:
                            print(str(contador+1)+" - "+datos[0][contador])
                            contador+=1
                        print("El director con quién más ha participado es: "+datos[1])
                        print("Tiene un total de: ",datos[3]," películas")
                        print("Para un promedio de: ",round(datos[2],2))
            elif int(opcion[0])==5:
                if cont==None:
                    print("Debe cargar el archivo primero")
                else:
                    genero=input("Digite el nombre del género: ")
                    datos=ctrl.buscar_por_genero(cont,genero)
                    if datos==None:
                        print("Criterio equivocado")
                    else:
                        print('Nombres de peliculas por género '+genero+': ')
                        for i in range(datos[2]):
                            print(i+1,'. ',lt.getElement(datos[0],i)['original_title'])
                        print('El promedio  de votos para el género: '+genero+' es de: ',round(datos[1],2))
                        print('Para un total de ',datos[2],' peliculas')
            elif int(opcion[0])==6:
                if cont==None:
                    print("Debe cargar el archivo primero")
                else:
                    pais=input("Digite el nombre de un país: ")
                    datos=ctrl.buscar_por_pais(cont,pais)
                    if datos==None:
                        print("Criterio equivocado")
                    else:
                        print("Las películas producidas en el país "+pais+" son: ")
                        contador=0
                        while contador<len(datos[0]):
                            print(str(contador+1)+" - "+datos[0][contador])
                            print("Su fecha de salida fue o es el: "+datos[1][contador])
                            print("Su director es: "+datos[2][contador])
                            contador+=1
            else:
                sys.exit(0)