from lista import Lista
from random import randint

# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver 
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;[115]
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador 
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se 
# deberán mostrar los datos de ambos;

# lista_entrenadores = Lista()

# entrenadores = [{'name':'juan','torneos_ganados': 12, 'batallas_perdidas' : 5, 'batallas_ganadas': 32, 'pokemons': Lista()},
#                 {'name':'enzo','torneos_ganados': 2, 'batallas_perdidas' : 8, 'batallas_ganadas': 20, 'pokemons': Lista()},
#                 {'name':'maria','torneos_ganados': 4, 'batallas_perdidas' : 15, 'batallas_ganadas': 28, 'pokemons': Lista()},]

# pokemons = [{'name':'tyrantrum','nivel':12,'tipo':'fuego','subtipo':'planta','entrenador':'juan'},
#             {'name':'wingull','nivel':180,'tipo':'agua','subtipo':'volador','entrenador':'juan'},
#             {'name':'wolverine','nivel':3,'tipo':'fuego','subtipo':'terreno','entrenador':'enzo'},
#             {'name':'tyrantrum','nivel':12 ,'tipo':'fuego','subtipo':'planta','entrenador':'maria'},
#             {'name':'wingull','nivel':18,'tipo':'agua','subtipo':'volador','entrenador':'enzo' },
#             {'name':'tyrantrum','nivel':12 ,'tipo':'fuego','subtipo':'planta','entrenador':'maria' },
#             {'name':'gigante','nivel':21,'tipo':'agua','subtipo':'volador','entrenador':'juan' },
#             {'name':'rayo','nivel':3,'tipo':'fuego','subtipo':'terreno','entrenador':'enzo' },
#             {'name':'terrakion','nivel':21 ,'tipo':'roca','subtipo':'lucha','entrenador':'maria'}]

# def cargarEntrenadores(lista,entrenadores):
#     for entrenador in entrenadores:
#         lista.insertar(entrenador, 'name')
# cargarEntrenadores(lista_entrenadores,entrenadores)

# def cargarPokemon(lista,pokemons):
#     for pokemon in pokemons:
#         pos = lista.busqueda(pokemon['entrenador'], 'name')
#         if(pos > -1):
#             del pokemon['entrenador']
#             lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon, 'name')
# cargarPokemon(lista_entrenadores,pokemons)
# name='enzo'
# pos = lista_entrenadores.busqueda(name, 'name')
# if(pos != -1):
#     print('cantidad de pokemones de ', name,': ',lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())

# def mas3Trofeos(lista):
#     print ('entrenadores con mas de 3 trofeos:')
#     for i in range (lista.tamanio()):
#         aux=lista.obtener_elemento(i)
#         if (aux['torneos_ganados']>3):
#             print ('entrenador: ',aux['name'])
# mas3Trofeos(lista_entrenadores)

# def masTrofeos(lista):
#     maximo = 0
#     pos_maximo = -1
#     for i in range(lista.tamanio()):
#         if(lista.obtener_elemento(i)['torneos_ganados'] > maximo):
#             maximo = lista.obtener_elemento(i)['torneos_ganados'] 
#             pos_maximo = i
#     return pos_maximo
# posTrofeo=masTrofeos(lista_entrenadores)
# print('entrenador con mas trofeos: ',lista_entrenadores.obtener_elemento(posTrofeo)['name'])

# def masNivel(lista,pos):
#     nivel_max = 0
#     posMax = -1
#     for i in range(lista.obtener_elemento(pos)['pokemons'].tamanio()):
#         if(lista.obtener_elemento(pos)['pokemons'].obtener_elemento(i)['nivel'] > nivel_max):
#             nivel_max = lista.obtener_elemento(pos)['pokemons'].obtener_elemento(i)['nivel']
#             posMax = i
#     return posMax
# posNivel=masNivel(lista_entrenadores,posTrofeo)
# print('su pokemon con mayor nivel es: ',lista_entrenadores.obtener_elemento(posTrofeo)['pokemons'].obtener_elemento(posNivel)['name'])
# print('entrenador:',lista_entrenadores.obtener_elemento(posTrofeo)['name'],',torneos ganados:', lista_entrenadores.obtener_elemento(posTrofeo)['torneos_ganados'],',batallas ganadas:', lista_entrenadores.obtener_elemento(posTrofeo)['batallas_ganadas'],',batallas perdidas:', lista_entrenadores.obtener_elemento(posTrofeo)['batallas_perdidas'])
# print('pokemons:')
# lista_entrenadores.obtener_elemento(posTrofeo)['pokemons'].barrido()

# def ganadas_porcentaje(listae,porcentaje):
#     print ('los entrenadores con mas del ',porcentaje,' porciento son:')
#     for i in range(listae.tamanio()):
#         lista=listae.obtener_elemento(i)
#         total = lista['batallas_ganadas']+lista['batallas_perdidas']
#         if ((lista['batallas_ganadas']*100/total)>porcentaje):
#             print (lista['name'])
# porcentaje=79
# ganadas_porcentaje(lista_entrenadores,porcentaje)

# def tipoysub(listae):
#     for j in range(listae.tamanio()):
#         lista=listae.obtener_elemento(j)
#         for i in range(lista['pokemons'].tamanio()):
#             poke=lista['pokemons'].obtener_elemento(i)
#             if ((poke['tipo'] =='fuego') and (poke['subtipo']=='planta')):
#                 print ('entrenador de tipo fuego, subtipo planta:',lista['name'])
#             if ((poke['tipo'] =='agua') and (poke['subtipo']=='volador')):
#                 print ('entrenador de tipo agua, subtipo volador:',lista['name'])
# tipoysub(lista_entrenadores)

# def promedio(listae):
#         pos=0
#         total=0
#         lista=listae.obtener_elemento(pos)
#         for i in range(lista['pokemons'].tamanio()):
#             total+= lista['pokemons'].obtener_elemento(i)['nivel']
#         print ('el promedio de nivel de ',lista['name'],' es: ',total/lista['pokemons'].tamanio())
# promedio(lista_entrenadores)

# def busquedaPokemon(lista,buscado):
#     print('los entrenadores con el pokeon ',buscado,' son:')
#     for i in range (lista.tamanio()):
#         if (lista.obtener_elemento(i)['pokemons'].busqueda(buscado,'name') > -1):
#             print(lista_entrenadores.obtener_elemento(i)['name'])
# buscado= 'wingull'
# busquedaPokemon(lista_entrenadores,buscado)

# def pokemonRepetidos(lista):
#     print ('los entrenadores con pokemones repetidos son:')
#     for j in range (lista.tamanio()):
#         for i in range (lista.obtener_elemento(j)['pokemons'].tamanio()-1):
#             if (lista.obtener_elemento(j)['pokemons'].obtener_elemento(i)['name']==lista.obtener_elemento(j)['pokemons'].obtener_elemento(i+1)['name']):
#                 print(lista.obtener_elemento(j)['name'])
# pokemonRepetidos(lista_entrenadores)
# busquedaPokemon(lista_entrenadores,'tyrantrum')
# busquedaPokemon(lista_entrenadores,'terrakion')
# busquedaPokemon(lista_entrenadores,'wingull')

# def entrenadorXpokemonY(lista, entrenadorX, pokemonY ):
#     posEntrenador = lista.busqueda(entrenadorX, 'name')
#     if posEntrenador > -1:
#         posPokemon = lista.obtener_elemento(posEntrenador)['pokemons'].busqueda(pokemonY, 'name')
#         if posPokemon > -1:
#             print('El entrenador ', entrenadorX, ' tiene al pokemon ',pokemonY)
#             mostrarX=lista.obtener_elemento(posEntrenador)
#             print('entrenador: ',mostrarX['name'],' torneos_ganados: ',mostrarX['torneos_ganados'],' batallas ganadas: ',mostrarX['batallas_ganadas'],' batallas perdidas: ',mostrarX['batallas_perdidas'])
#             mostrarY = lista.obtener_elemento(posEntrenador)['pokemons'].obtener_elemento(posPokemon)
#             print('pokemon: ',mostrarY['name'],' nivel: ',mostrarY['nivel'],' tipo: ',mostrarY['tipo'],' subtipo: ',mostrarY['subtipo'])
#         else:
#             print('El Entrenador ', entrenadorX, ' no tiene a ',pokemonY)
#     else:
#         print('El Entrenador ', entrenadorX, ' no esta en la lista')
# entrenadorx = input('nombre del entrenador: ')
# pokemony = input('nombre del pokemon: ')
# entrenadorXpokemonY(lista_entrenadores,entrenadorx,pokemony)




# 21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos: 
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–;[118]
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una 
# lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

lista_peliculas = Lista()

peliculas = [{'name':'forest','valoracion': 8, 'anio' : 1994, 'recaudacion': 1000000},
                {'name':'el aeropuerto','valoracion': 9, 'anio' : 2004, 'recaudacion': 3000000},
                {'name':'el naufrago','valoracion': 10, 'anio' : 2000, 'recaudacion': 7000000},]



# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–

dato = lista_peliculas.busqueda('1994'.title(), 'anio')
if dato:
    print(f'el superheroe {dato.info.name} aparecieo en {dato.info.anio}')
else:
    print('el superheroe no esta en la lista')
# b. mostrar los datos de la película que más recaudo;

def masRecaudacion(peliculas):
    maximo = 0
    pos_maximo = -1
    for i in range(lista_peliculas.tamanio()):
        if(lista_peliculas.obtener_elemento(i)['recaudacion'] > maximo):
            maximo = lista_peliculas.obtener_elemento(i)['recaudacion'] 
            pos_maximo = i
    return pos_maximo
posReca=masRecaudacion(lista_peliculas)
print('con mayor recaudacion: ',lista_peliculas.obtener_elemento(posReca)['name'])

# c. indicar las películas con mayor valoración del público, puede ser más de una;

def masValoracion(peliculas):
    maximo = 0
    pos_maximo = -1
    for i in range(lista_peliculas.tamanio()):
        if(lista_peliculas.obtener_elemento(i)['valoracion'] > maximo):
            maximo = lista_peliculas.obtener_elemento(i)['valoracion'] 
            pos_maximo = i
    return pos_maximo
posReca=masValoracion(lista_peliculas)
print('con mayor valoracion: ',lista_peliculas.obtener_elemento(posReca)['name'])

# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, 
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las 
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron."""

# class Jedi:

#     def __init__(self, nombre, especie, maestro, sable_luz):
#         self.nombre = nombre
#         self.especie = especie
#         self.maestro = maestro
#         self.sable_luz = sable_luz

#     def __str__(self):
#         return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"

# # a. listado ordenado por nombre y por especie;

# lista_jedi = Lista()
# lista_jedi2 = Lista()

# file = open('jedis.txt')
# lineas = file.readlines()

# lista = []

# lineas.pop(0)  # quitar cabecera
# for linea in lineas:
#     datos = linea.split(';')
#     datos.pop(-1)
#     # print(datos[4].split('/'))
#     lista_jedi.insertar(Jedi(datos[0],
#                              datos[2],
#                              datos[3].split('/'),
#                              datos[4].split('/')),
#                         campo='nombre')
#     lista_jedi2.insertar(Jedi(datos[0],
#                               datos[2],
#                               datos[3],
#                               datos[4].split('/')),
#                          campo='especie')
#     lista.append(Jedi(datos[0],
#                       datos[2],
#                       datos[3].split('/'),
#                       datos[4].split('/')))
# # !


# for Jedi in Jedi:
#     lista_jedi.insertar(Jedi, 'name')

# for i in range(0, lista_jedi.tamanio()):
#     lista_jedi.obtener_elemento(i)['especie'] = lista_jedi[i]

# def barridoJedis(lista):
#     for i in range (0,lista.tamanio()):
#         elemento=lista.obtener_elemento(i)
#         print ('nombre: ',elemento['name'])
#         print ('maestros: ',elemento['maestro'])
#         print ('sables: ',elemento['sables'])
#         print ('especie: ',elemento['especie'])
#         print ()

# lista_jedi.ordenar('especie')
# barridoJedis(lista_jedi)
# lista_jedi.ordenar('name')
# barridoJedis(lista_jedi)

# def barridoBusqueda(lista,pos):
#     elemento=lista.obtener_elemento(pos)
#     print ('nombre: ',elemento['name'])
#     print ('maestros: ',elemento['maestro'])
#     print ('sables: ',elemento['sables'])
#     print ('especie: ',elemento['especie'])
#     print ()

# # lista_jedi2.barrido()

# # b. mostrar toda la información de Ahsoka Tano y Kit Fisto;

# pos = lista_jedi.busqueda('Ahsoka Tano','name')
# if (pos != -1):
#     barridoBusqueda(lista_jedi,pos)

# dato = lista_jedi.busqueda('kit fisto', 'nombre')
# if dato:
#     print(f'el Jedi {dato.info}')
# else:
#     print('el Jedi no esta en la lista')

# # c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;

# def PadawansDeMaestros(lista, maestro):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if (jedi['maestro'] == maestro):
#             print(jedi['name'])

# print ('padawans de luke Skywalker')
# PadawansDeMaestros(lista_jedi,'Luke Skywalker')
# print ('padawans de Yoda')
# PadawansDeMaestros(lista_jedi,'Yoda')

# print()
# lista_jedi.barrido_jedi_master()

# # d. mostrar los Jedi de especie humana y twi'lek;

# def mostrarEspecies(lista, especie):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if jedi['especie'] == especie:
#             print(jedi['name'])
# print ('especie humana:')
# mostrarEspecies(lista_jedi,'Humana')
# print ('especie twi´lek:')
# mostrarEspecies(lista_jedi,'Twi´lek')

# # e. listar todos los Jedi que comienzan con A;

# def JedisInicial(lista, letra):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if (letra == jedi['name'].upper()[0]):
#             print(jedi['name'])
# JedisInicial(lista_jedi,'A')

# # print()
# # lista_jedi.barrido_comienza_con(['a'])

# # def citerio(item):
# #     return item.nombre + item.especie


# # lista.sort(key=citerio)

# # for jedi in lista:
# #     print(jedi)


# # f. mostrar los Jedi que usaron sable de luz de más de un color;


# def Jedis_Sables(lista):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if len(jedi['sables']) > 1:
#             if (jedi['sables'][0]!=jedi['sables'][3]):
#                 print (jedi['name'])
# Jedis_Sables(lista_jedi)


# # g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# def JedisColorDeSable(lista, color):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         for j in range(0, len(jedi['sables'])):
#             if (jedi['sables'][j] == color) :
#                 print (jedi['name'])

# print ('jedis con sables color amarillo:')
# JedisColorDeSable(lista_jedi,'amarillo')
# print ('jedis con sables color violeta:')
# JedisColorDeSable(lista_jedi,'violeta')


# # h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

# print ('los padawans de Qui-Gon Jin: ')
# PadawansDeMaestros (lista_jedi,'Qui-Gon Jin')
# print ('los padawansk de Mace Windu: ')
# PadawansDeMaestros (lista_jedi,'Mace Windu')


# Jedis = [
#         {'name' : 'Bo Keevil', 'maestro' : 'Mace Windu', 'sables' : [], 'especie' : 'Humana'},
#         {'name' : 'Bossk', 'maestro' : 'Yoda' , 'sables' : [], 'especie' : 'Humana'},
#         {'name' : 'Boba Fett', 'maestro' : 'Luke Skywalker', 'sables' : [], 'especie' : 'Twi´lek'},
#         {'name' : 'Kit Fisto', 'maestro' : 'Qui-Gon Jin' , 'sables' : [], 'especie' : 'Nautolano'},
#         {'name' : 'Baby Yoda', 'maestro' : 'Yoda' , 'sables' : [], 'especie' : 'desconocida'},
#         {'name' : 'Ahsoka Tano', 'maestro' : 'Luke Skywalker', 'sables' : [], 'especie' : 'Togruta'},
#         ]

# sables= [['rojo', 'azul'],
#         ['rojo'],
#         ['blanco', 'violeta'],
#         ['violeta', 'amarillo'],
#         ['verde', 'verde'],
#         ['azul']
#         ]

# listaJedis = Lista()

# for Jedi in Jedis:
#     listaJedis.insertar(Jedi, 'name')

# for i in range(0, listaJedis.tamanio()):
#     listaJedis.obtener_elemento(i)['sables'] = sables[i]

# def barridoJedis(lista):
#     for i in range (0,lista.tamanio()):
#         elemento=lista.obtener_elemento(i)
#         print ('nombre: ',elemento['name'])
#         print ('maestros: ',elemento['maestro'])
#         print ('sables: ',elemento['sables'])
#         print ('especie: ',elemento['especie'])
#         print ()

# listaJedis.ordenar('especie')
# barridoJedis(listaJedis)
# listaJedis.ordenar('name')
# barridoJedis(listaJedis)

# def barridoBusqueda(lista,pos):
#     elemento=lista.obtener_elemento(pos)
#     print ('nombre: ',elemento['name'])
#     print ('maestros: ',elemento['maestro'])
#     print ('sables: ',elemento['sables'])
#     print ('especie: ',elemento['especie'])
#     print ()

# pos = listaJedis.busqueda('Ahsoka Tano','name')
# if (pos != -1):
#     barridoBusqueda(listaJedis,pos)

# pos = listaJedis.busqueda('Kit Fisto','name')
# if (pos != -1):
#     barridoBusqueda(listaJedis,pos)

# def PadawansDeMaestros(lista, maestro):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if (jedi['maestro'] == maestro):
#             print(jedi['name'])

# print ('padawans de luke Skywalker')
# PadawansDeMaestros(listaJedis,'Luke Skywalker')
# print ('padawans de Yoda')
# PadawansDeMaestros(listaJedis,'Yoda')

# def mostrarEspecies(lista, especie):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if jedi['especie'] == especie:
#             print(jedi['name'])
# print ('especie humana:')
# mostrarEspecies(listaJedis,'Humana')
# print ('especie twi´lek:')
# mostrarEspecies(listaJedis,'Twi´lek')

# def JedisInicial(lista, letra):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if (letra == jedi['name'].upper()[0]):
#             print(jedi['name'])
# JedisInicial(listaJedis,'A')

# def JedisCon2Sables(lista):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         if len(jedi['sables']) > 1:
#             if (jedi['sables'][0]!=jedi['sables'][1]):
#                 print (jedi['name'])
# JedisCon2Sables(listaJedis)

# def JedisColorDeSable(lista, color):
#     for i in range(0, lista.tamanio()):
#         jedi = lista.obtener_elemento(i)
#         for j in range(0, len(jedi['sables'])):
#             if (jedi['sables'][j] == color) :
#                 print (jedi['name'])

# print ('jedis con sables color amarillo:')
# JedisColorDeSable(listaJedis,'amarillo')
# print ('jedis con sables color violeta:')
# JedisColorDeSable(listaJedis,'violeta')

# print ('los padawans de Qui-Gon Jin: ')
# PadawansDeMaestros (listaJedis,'Qui-Gon Jin')
# print ('los padawansk de Mace Windu: ')
# PadawansDeMaestros (listaJedis,'Mace Windu')