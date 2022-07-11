'''# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, 
desarrollar las funciones necesarias para resolver las siguientes actividades:
'''
# class Pelicula():
#     Peliculas, estudio, anio_estreno = None, None, None

# dic = {'Peliculas': 'callou', 'estudio': 'warner', 'anio_estreno': '2014'}

# dic['Peliculas']


# Peliculas =['callou', 'el renacido', 'batman']
# estudio =['warner','holiwud','Marvel Studios']
# anio_estreno =[2012,2013,2014,2015,2016,2017,2018,2019,2020]

# from random import choice

# for i in range(len(Peliculas)):
#     dato = Pelicula()
#     dato.Peliculas = Peliculas[i]
#     #dato.Peliculas = choice(Peliculas)
#     dato.estudio = estudio[i]
#     #dato.estudio = choice(estudio)
#     dato.anio_estreno = choice(anio_estreno)
#     dic = {'Peliculas': Peliculas[i], 'estudio': estudio[i], 'anio': choice(anio_estreno)}
#     print(dato.Peliculas, dato.estudio, dato.anio_estreno)
#     pila1.apilar(dato)

# '''a. mostrar los nombre películas estrenadas en el año 2014;
# '''
# print()
# #anio_estreno = input('ingrese la pelicula estrenada en el año 2014 ')
# insertar = True
# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     if(dato.anio_estreno == 2014):
#         print('Punto A.     la pelicula estrenada en el 2014 es ', dato.Peliculas)
    
#     '''b. indicar cuántas películas se estrenaron en el año 2018'''
#     contador = 0
#     if(dato.anio_estreno == 2018):
#         print()
#         print('Punto B.     la pelicula estrenada en el 2018 es ', dato.Peliculas)
#         contador += 1
#         print('             cantidad de peliculas estrenadas en ', contador)

#     '''c. mostrar las películas de Marvel Studios estrenadas en el año 2016.'''

#     if(dato.estudio == 'Marvel Studios' and dato.anio_estreno == 2016):
#         print()
#         print('Punto C.     la pelicula estrenada en el 2016 de Marvel Studios es ', dato.Peliculas)
#         contador += 1
#         print('             cantidad de peliculas estrenadas en ', contador)



'''# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:

a.determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.'''

# class Personaje (object):

#     def __init__(self, nombre, cant_peliculas):
#         self.nombre = nombre
#         self.cant_peliculas = cant_peliculas

#     def __str__(self):
#         return self.nombre + ' - ' + str(self.cant_peliculas) + ' peliculas'

# pila_MCU = Pila ()
# pila_aux = Pila ()
# pila_5 = Pila()
# pila_CDG = Pila()

# personajes = [('Iron Man', 11),('Captain America', 11),('Groot', 4),('Black Widow', 10),('Thor', 8),
#             ('Hulk', 8),('Hawkeye', 5),('Bucky Barnes', 7),('Wanda Maximoff', 5),('Captain Marvel', 2),
#             ('Star-Lord', 4),('Rocket Raccoon', 4),('Gamora', 4),('Black Panther', 4)]

# for (a,b)  in personajes:
#     personaje = Personaje(a,b)
#     pila_MCU.apilar(personaje)

# while not pila_MCU.pila_vacia():
#     x = pila_MCU.desapilar()
#     pila_aux.apilar(x)
#     if x.nombre == 'Rocket Raccoon' or x.nombre == 'Groot':
#         print (x.nombre, 'se encuentra en la posicion', pila_aux.tamanio()) 
#     if x.cant_peliculas > 5:
#         pila_5.apilar(x)
#     if x.nombre == 'Black Widow':
#         print ('Black Widow aparecio en', x.cant_peliculas, 'peliculas.')
#     if x.nombre[0] == 'C' or x.nombre[0] == 'D' or x.nombre[0] == 'G': 
#         pila_CDG.apilar(x)

# print()
# print ('Personajes que aparecieron en mas de 5 películas:')
# while not pila_5.pila_vacia():
#     print (pila_5.desapilar())

# print()
# print ('Personajes cuyo nombre empieza con C, D o G:')
# while not pila_CDG.pila_vacia():
#     print (pila_CDG.desapilar().nombre)
