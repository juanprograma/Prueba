import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
assert config
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog(cantidad,factor_de_carga):
    catalog = {'moviesDetails': None,
                'moviesCasting': None,
                'moviesIdsDetails': None,
                'moviesIdsCasting': None,
                'directors': None,
                'actors': None,
                'productionCompanies': None,
                'genres': None,
                'countries': None}

    catalog['moviesDetails'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesCasting'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['moviesIdsDetails'] = mp.newMap(cantidad,
                                maptype='CHAINING',
                                loadfactor=factor_de_carga,
                                comparefunction=compareMapMoviesIds)
    catalog['moviesIdsCasting'] = mp.newMap(cantidad,
                                   maptype='CHAINING',
                                   loadfactor=factor_de_carga,
                                   comparefunction=compareMapMoviesIds)
    catalog['directors'] = mp.newMap(cantidad,
                                   maptype='CHAINING',
                                   loadfactor=factor_de_carga,
                                   comparefunction=compareDirectorsByName)
    catalog['actors'] = mp.newMap(cantidad,
                                  maptype='CHAINING',
                                  loadfactor=factor_de_carga,
                                  comparefunction=compareActorsByName)
    catalog['productionCompanies'] = mp.newMap(cantidad,
                                 maptype='CHAINING',
                                 loadfactor=factor_de_carga,
                                 comparefunction=compareProductionCompany)
    catalog['genres'] = mp.newMap(cantidad,
                                 maptype='CHAINING',
                                 loadfactor=factor_de_carga,
                                 comparefunction=compareGenres)
    catalog['countries'] = mp.newMap(cantidad,
                                 maptype='CHAINING',
                                 loadfactor=factor_de_carga,
                                 comparefunction=compareCountry)
    return catalog
#______________________________________________
# Funciones para agregar informacion al catalogo
#______________________________________________
def addMovieDetails(catalog, movie):
    lt.addLast(catalog['moviesDetails'], movie)
    mp.put(catalog['moviesIdsDetails'], movie['id'], movie)
def addMovieCasting(catalog, movie):
    lt.addLast(catalog['moviesCasting'], movie)
    mp.put(catalog['moviesIdsCasting'], movie['id'], movie)
def addMovieByDirector(catalog,directorName,movie):
    directors = catalog['directors']
    existdirector = mp.contains(directors,directorName)
    if existdirector:
        entry = mp.get(directors, directorName)
        director = me.getValue(entry)
    else:
        director = NewDirector(directorName)
        mp.put(directors, directorName, director)
    lt.addLast(director['movies'], movie)
    direcavg = director['vote_average']
    movieavg = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_average']
    direcount = director['vote_count']
    moviecount = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_count']
    if (direcavg[0] == 0.0):
        director['vote_average'][0] = float(movieavg)
        director['vote_average'][1] = float(movieavg)
        director['vote_average'][2] = 1
    else:
        director['vote_average'][1] = direcavg[1] + float(movieavg)
        director['vote_average'][2] += 1
        director['vote_average'][0] =  director['vote_average'][1]/ director['vote_average'][2]
    if (direcount[0] == 0):
        director['vote_count'][0] = int(moviecount)
        director['vote_count'][1] = int(moviecount)
        director['vote_count'][2] = 1
    else:
        director['vote_count'][1] = direcount[1] + int(moviecount)
        director['vote_count'][2] += 1
        director['vote_count'][0] =  director['vote_count'][1]/ director['vote_count'][2]
def addMovieByCountry(catalog,countryName,movie):
    countries = catalog['countries']
    existcountry = mp.contains(countries,countryName)
    if existcountry:
        entry = mp.get(countries, countryName)
        country = me.getValue(entry)
    else:
        country = NewCountry(countryName)
        mp.put(countries, countryName, country)
    lt.addLast(country['movies'], movie)
    countryavg = country['vote_average']
    movieavg = movie['vote_average']
    countrycount = country['vote_count']
    moviecount = movie['vote_count']
    if (countryavg[0] == 0.0):
        country['vote_average'][0] = float(movieavg)
        country['vote_average'][1] = float(movieavg)
        country['vote_average'][2] = 1
    else:
        country['vote_average'][1] = countryavg[1] + float(movieavg)
        country['vote_average'][2] += 1
        country['vote_average'][0] =  country['vote_average'][1]/ country['vote_average'][2]
    if (countrycount[0] == 0):
        country['vote_count'][0] = int(moviecount)
        country['vote_count'][1] = int(moviecount)
        country['vote_count'][2] = 1
    else:
        country['vote_count'][1] = countrycount[1] + int(moviecount)
        country['vote_count'][2] += 1
        country['vote_count'][0] =  country['vote_count'][1]/ country['vote_count'][2]
def addMovieByProductionCompany(catalog,companyName,movie):
    companies = catalog['productionCompanies']
    existcompany = mp.contains(companies,companyName)
    if existcompany:
        entry = mp.get(companies, companyName)
        company = me.getValue(entry)
    else:
        company = NewProductionCompany(companyName)
        mp.put(companies, companyName, company)
    lt.addLast(company['movies'], movie)
    companyavg = company['vote_average']
    movieavg = movie['vote_average']
    companycount = company['vote_count']
    moviecount = movie['vote_count']
    if (companyavg[0] == 0.0):
        company['vote_average'][0] = float(movieavg)
        company['vote_average'][1] = float(movieavg)
        company['vote_average'][2] = 1
    else:
        company['vote_average'][1] = companyavg[1] + float(movieavg)
        company['vote_average'][2] += 1
        company['vote_average'][0] =  company['vote_average'][1]/ company['vote_average'][2]
    if (companycount[0] == 0):
        company['vote_count'][0] = int(moviecount)
        company['vote_count'][1] = int(moviecount)
        company['vote_count'][2] = 1
    else:
        company['vote_count'][1] = companycount[1] + int(moviecount)
        company['vote_count'][2] += 1
        company['vote_count'][0] =  company['vote_count'][1]/ company['vote_count'][2]
def addMovieByGenre(catalog,genreName,movie):
    genres = catalog['genres']
    existgenre = mp.contains(genres,genreName)
    if existgenre:
        entry = mp.get(genres, genreName)
        genre = me.getValue(entry)
    else:
        genre = NewGenre(genreName)
        mp.put(genres, genreName, genre)
    lt.addLast(genre['movies'], movie)
    genreavg = genre['vote_average']
    movieavg = movie['vote_average']
    genrecount = genre['vote_count']
    moviecount = movie['vote_count']
    if (genreavg[0] == 0.0):
        genre['vote_average'][0] = float(movieavg)
        genre['vote_average'][1] = float(movieavg)
        genre['vote_average'][2] = 1
    else:
        genre['vote_average'][1] = genreavg[1] + float(movieavg)
        genre['vote_average'][2] += 1
        genre['vote_average'][0] =  genre['vote_average'][1]/ genre['vote_average'][2]
    if (genrecount[0] == 0):
        genre['vote_count'][0] = int(moviecount)
        genre['vote_count'][1] = int(moviecount)
        genre['vote_count'][2] = 1
    else:
        genre['vote_count'][1] = genrecount[1] + int(moviecount)
        genre['vote_count'][2] += 1
        genre['vote_count'][0] =  genre['vote_count'][1]/ genre['vote_count'][2]
def addMovieByActor(catalog,actorName,movie):
    actors = catalog['actors']
    existactor = mp.contains(actors,actorName)
    if existactor:
        entry = mp.get(actors, actorName)
        actor = me.getValue(entry)
    else:
        actor = NewActor(actorName)
        mp.put(actors, actorName, actor)
    lt.addLast(actor['movies'], movie)
    actoravg = actor['vote_average']
    movieavg = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_average']
    actorcount = actor['vote_count']
    moviecount = me.getValue(mp.get(catalog['moviesIdsDetails'],movie['id']))['vote_count']
    if (actoravg[0] == 0.0):
        actor['vote_average'][0] = float(movieavg)
        actor['vote_average'][1] = float(movieavg)
        actor['vote_average'][2] = 1
    else:
        actor['vote_average'][1] = actoravg[1] + float(movieavg)
        actor['vote_average'][2] += 1
        actor['vote_average'][0] =  actor['vote_average'][1]/ actor['vote_average'][2]
    if (actorcount[0] == 0):
        actor['vote_count'][0] = int(moviecount)
        actor['vote_count'][1] = int(moviecount)
        actor['vote_count'][2] = 1
    else:
        actor['vote_count'][1] = actorcount[1] + int(moviecount)
        actor['vote_count'][2] += 1
        actor['vote_count'][0] =  actor['vote_count'][1]/ actor['vote_count'][2]
# ==============================
# Funciones de consulta
# ==============================
def getmoviesByDirector(catalog, directorname):
    director = mp.get(catalog['directors'], directorname)
    if director:
        return me.getValue(director)
    return None
def getmoviesByActor(catalog, actorname):
    actor = mp.get(catalog['actors'], actorname)
    if actor:
        return me.getValue(actor)
    return None
def getmoviesByProductionCompany(catalog, companyname):
    company = mp.get(catalog['productionCompanies'], companyname)
    if company:
        return me.getValue(company)
    return None
def getmoviesByGenres(catalog, genrename):
    genre = mp.get(catalog['genres'], genrename)
    if genre:
        return me.getValue(genre)
    return None
def getmoviesByCountry(catalog,countryname):
    country = mp.get(catalog['countries'], countryname)
    if country:
        return me.getValue(country)
    return None
def getMoviesbyname(catalog,idname):
    ids=mp.get(catalog["moviesIdsDetails"],idname)
    if ids:
        return me.getValue(ids)
def getMovies_director(catalog,idname):
    ids=mp.get(catalog["moviesIdsCasting"],idname)
    if ids:
        return me.getValue(ids)
# ==============================
# Funciones de Filtrado
# ==============================  
def NewDirector(directorName):
    director = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0], 'vote_count': [0,0,0]}
    director['name'] = directorName
    director['movies'] = lt.newList('ARRAY_LIST', compareDirectorsByName)
    return director
def NewCountry(countryName):
    country = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0], 'vote_count': [0,0,0]}
    country['name'] = countryName
    country['movies'] = lt.newList('ARRAY_LIST', compareCountry)

    return country

def NewProductionCompany(companyName):
    company = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0], 'vote_count': [0,0,0]}
    company['name'] = companyName
    company['movies'] = lt.newList('ARRAY_LIST', compareProductionCompany)
    return company
def NewGenre(genreName):
    genre = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0], 'vote_count': [0,0,0]}
    genre['name'] = genreName
    genre['movies'] = lt.newList('ARRAY_LIST', compareGenres)
    return genre
def NewActor(actorName):
    actor = {'name': "", "movies": None, 'vote_average': [0.0,0.0,0], 'vote_count': [0,0,0]}
    actor['name'] = actorName
    actor['movies'] = lt.newList('ARRAY_LIST', compareActorsByName)
    return actor
# ==============================
# Funciones de Comparacion
# ==============================
def compareMoviesIds(id1, id2):
    if (int(id1) == int(id2)):
        return 0
    elif int(id1) > int(id2):
        return 1
    else:
        return -1
def compareVotesCount(vote, entry):
    voteEntry = me.getKey(entry)
    if (int(vote) == int(voteEntry)):
        return 0
    elif int(vote) > int(voteEntry):
        return 1
    else:
        return -1
def compareMapMoviesIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
def compareDirectorsByName(director, entry):
    directorentry = me.getKey(entry)
    if (director == directorentry):
        return 0
    elif (director > directorentry):
        return 1
    else:
        return -1

def compareVotesAverage(avr,entry):
    avrentry = me.getKey(entry)
    if (int(avr) == int(avrentry)):
        return 0
    elif (int(avr) > int(avrentry)):
        return 1
    else:
        return -1

def compareActorsByName(name, entry):
    nameentry = me.getKey(entry)
    if (name == nameentry):
        return 0
    elif (name > nameentry):
        return 1
    else:
        return -1

def compareProductionCompany(company, entry):
    companyentry = me.getKey(entry)
    if (company == companyentry):
        return 0
    elif (company > companyentry):
        return 1
    else:
        return 0

def compareGenres(genre, entry):
    genreentry = me.getKey(entry)
    if (genre == genreentry):
        return 0
    elif (genre > genreentry):
        return 1
    else:
        return 0 

def compareCountry(country, entry):
    countryentry = me.getKey(entry)
    if (country == countryentry):
        return 0
    elif (country > countryentry):
        return 1
    else:
        return 0 
# ==============================
# Funciones de Comparacion
# ==============================
def moviesDetailsSize(catalog):
    return lt.size(catalog['moviesDetails'])
def moviesCastingSize(catalog):
    return lt.size(catalog['moviesCasting'])
def MoviesIdsSize(catalog):
    return mp.size(catalog['moviesIds'])
def actorsSize(catalog):
    return mp.size(catalog['actors'])
def genresSize(catalog):
    return mp.size(catalog['genres'])
def productionCompaniesSize(catalog):
    return mp.size(catalog['productionCompanies'])
def countriesSize(catalog):
    return mp.size(catalog['countries'])
def voteAverageSize(catalog):
    return mp.size(catalog['voteAverage'])
def voteCountSize(catalog):
    return mp.size(catalog['voteCount'])   
# ==============================
# Funciones de los Requerimientos
# ==============================
"""REQUERMIENTO 1"""
def descubrirProductorasDeCine(catalog, nameCompany):
    try:
        companies = getmoviesByProductionCompany(catalog, nameCompany)
        movies_names = companies['movies']
        movies_avr = companies['vote_average'][0]
        return (movies_names,movies_avr,lt.size(movies_names))
    except:
        return -1
"""REQUERIMIENTO 2"""
def descubrir_drirector(catalog,directorname):
    try:
        director=getmoviesByDirector(catalog,directorname)
        nombres_peliculas= director["movies"]
        average= director["vote_average"][0]
        ids=nombres_peliculas["elements"]
        cont=0
        a=[]
        while cont<len(ids) and cont!=len(ids):
            movies=getMoviesbyname(catalog,ids[cont]["id"])
            cont+=1
            a.append(movies)
        nombres_movies=[]
        for i in a:
            nombres_movies.append(i["original_title"])
        return (nombres_movies,average,len(nombres_movies))
    except:
        return None
"""REQUERIMIENTO 3"""
#TERMINAR
def buscar_por_actor(catalog,actorname):
    try:
        actor=getmoviesByActor(catalog,actorname)
        nombres_peliculas=actor["movies"]
        average=actor["vote_average"][0]
        general=nombres_peliculas["elements"]
        contador=0
        directores=[]
        peli=[]
        while contador<len(general) and contador!=len(general):
            movies=getMoviesbyname(catalog,general[contador]["id"])
            director=general[contador]["director_name"]
            peli.append(movies)
            directores.append(director)
            contador+=1
        nombres_peli=[]
        for i in peli:
            nombres_peli.append(i["original_title"])
        director_mas=(max(set(directores), key=directores.count))
        return (nombres_peli,director_mas,average,len(nombres_peli))
    except:
        return None
"""REQUERMIENTO 4"""
def buscar_por_genero(catalog,genrename):
    try:
        género=getmoviesByGenres(catalog,genrename)
        nombres_peliculas=género["movies"]
        count=género["vote_count"][0]
        return (nombres_peliculas,count,lt.size(nombres_peliculas))
    except:
        return None
"""REQUERIMIENTO 5"""
def buscar_por_pais(catalog,countryname):
    pais=getmoviesByCountry(catalog,countryname)
    nombres_peliculas=pais["movies"]
    general=nombres_peliculas["elements"]
    cont=0
    directores=[]
    peli=[]
    fechas=[]
    while cont<len(general) and cont!=len(general):
        direct=getMovies_director(catalog,general[cont]["id"])
        nombres_peliculas=general[cont]["original_title"]
        fechas_peli=general[cont]["release_date"]
        peli.append(nombres_peliculas)
        fechas.append(fechas_peli)
        directores.append(direct)
        cont+=1
    nombres_directores=[]
    for i in directores:
        nombres_directores.append(i["director_name"])
    return (peli,fechas,nombres_directores)

    
