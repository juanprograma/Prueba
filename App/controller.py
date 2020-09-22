import config as cf
from App import model
import csv
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
# _________________
#  Inicializacion del catalogo
# _________________
def crearCatalogo(cantidad,factor_de_carga):
    catalog=model.newCatalog(cantidad,factor_de_carga)
    return catalog
# _________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# _________________
def cargarDatos(catalog,moviesCastingFile,moviesDetailsFile):
    cargarDetalles(catalog,moviesDetailsFile)
    cargarCasting(catalog,moviesCastingFile)
def cargarCasting(catalog,moviesfile):
    moviesfile = cf.data_dir + moviesfile
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file= csv.DictReader(open(moviesfile, encoding='utf-8-sig'),dialect=dialect)
    for movie in input_file:
        model.addMovieCasting(catalog,movie)
        actors1 = movie['actor1_name'].split(",")
        actors2 = movie['actor2_name'].split(",")
        actors3 = movie['actor3_name'].split(",")
        actors4 = movie['actor4_name'].split(",")
        actors5 = movie['actor5_name'].split(",")
        directors = movie['director_name'].split(",")
        for autor in actors1:
            model.addMovieByActor(catalog, autor.strip(), movie)
        for autor in actors2:
            model.addMovieByActor(catalog, autor.strip(), movie)
        for autor in actors3:
            model.addMovieByActor(catalog, autor.strip(), movie)
        for autor in actors4:
            model.addMovieByActor(catalog, autor.strip(), movie)
        for autor in actors5:
            model.addMovieByActor(catalog, autor.strip(), movie)
        for director in directors:
            model.addMovieByDirector(catalog, director.strip(), movie)       
def cargarDetalles(catalog,moviesfile):
    moviesfile = cf.data_dir + moviesfile
    dialect = csv.excel()
    dialect.delimiter=";"
    input_file = csv.DictReader(open(moviesfile,encoding='utf-8-sig'),dialect=dialect)
    for movie in input_file:
        model.addMovieDetails(catalog,movie)
        companies = movie['production_companies'].split(",")
        genres = movie['genres'].split(",")
        countries = movie['production_countries'].split(",")
        for company in companies:
            model.addMovieByProductionCompany(catalog, company.strip(), movie)
        for genre in genres:
            model.addMovieByGenre(catalog, genre.strip(), movie)
        for country in countries:
            model.addMovieByCountry(catalog, country.strip(), movie)
# _________________
#  Funciones para consultas
# _________________
"""TAMAÑO DETALLES"""
def moviesDetailsSize(catalog):
    return model.moviesDetailsSize(catalog)
"""TAMAÑO CASTING"""
def moviesCastingSize(catalog):
    return model.moviesCastingSize(catalog)
"""TAMAÑO ID"""
def moviesIdsSize(catalog):
    return model.MoviesIdsSize(catalog)
"""TAMAÑO ACTORES"""
def actorsSize(catalog):
    return model.actorsSize(catalog)
"""TAMAÑO GÉNERO"""
def genresSize(catalog):
    return model.genresSize(catalog)
"""TAMAÑO COMPAÑÍAS"""
def productionCompaniesSize(catalog):
    return model.productionCompaniesSize(catalog)
"""TAMAÑO PAISES"""
def countriesSize(catalog):
    return model.countriesSize(catalog)
"""TAMAÑO VOTOS PROMEDIO"""
def voteAverageSize(catalog):
    return model.voteAverageSize(catalog)
"""TAMAÑO CONTEO VOTOS"""
def voteCountSize(catalog):
    return model.voteCountSize(catalog)
"""PELÍCULAS-DIRECTOR"""
def getMoviesByDirector(catalog):
    return model.moviesByDirector(catalog)
"""PELÍCULAS-ACTOR"""
def getMoviesByActor(catalog):
    return model.moviesByActor(catalog)
"""PELÍCULAS-COMPAÑÍAS"""
def getMoviesByProductionCompanies(catalog):
    return model.moviesByProductionCompany(catalog)
"""PELÍCULAS-PAÍS"""
def getMoviesByCountry(catalog):
    return model.moviesByCountry(catalog)
"""PELÍCULAS-GÉNERO"""
def getMoviesByGenre(catalog):
    return model.moviesByGenre(catalog)
"""REQUERMIENTO 1"""
def descubrirProductorasDeCine(catalog, nameCompany):
    return model.descubrirProductorasDeCine(catalog, nameCompany)
"""REQUERIMIENTO 2"""
#CORREGIR
def descubrir_director(catalog,directorname):
    return model.descubrir_drirector(catalog,directorname)
"""REQUERIMIENTO 3"""
#TERMINAR
def buscar_por_actor(catalog,actorname):
    return model.buscar_por_actor(catalog,actorname)
"""REQUERMIENTO 4"""
def buscar_por_genero(catalog,genrename):
    return model.buscar_por_genero(catalog,genrename)
"""REQUERIMIENTO 5"""
def buscar_por_pais(catalog,countryname):
    return model.buscar_por_pais(catalog,countryname)
