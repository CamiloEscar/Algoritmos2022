'''# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
'''

romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50}

def romano_decimal(num_romano):
    if(len(num_romano) == 1):
        return romanos[num_romano]
    else:
        if(romanos[num_romano[0]] >= romanos[num_romano[1]]):
            return romanos[num_romano[0]] + romano_decimal(num_romano[1:])
        else:
            return - romanos[num_romano[0]] + romano_decimal(num_romano[1:])

# print(romano_decimal('XLVI'))

'''# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:

a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

c. Utilizar un vector para representar la mochila.
'''

from random import shuffle

def usar_la_fuerza (mochila, pos):
    if pos<len(mochila):
        if (mochila[pos] == 'sable de luz'):
            return pos
        else:
            return usar_la_fuerza (mochila,pos+1)
    else:
        return -1
#A
# mochila = ['sable de luz', 'comunicador', 'comida', 'armadura', 'casco']
# shuffle(mochila)

# n = usar_la_fuerza (mochila, 0)

# if (n >= 0):
#     print ('Encontro el sable de luz.')
#     print ('Para encontrarlo hizo falta sacar', n, 'elementos')
# else: #B 
#     print ('El sable de luz no se encuentra en la mochila')
# #C
# print ('en la mochila hay:')
# for cosas in mochila:
#     print (cosas)

'''# 23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

'''
def salida_del_laberinto (laberinto, x, y, salida = []):
    if (x >=0 and x <= len(laberinto)-1) and y>=0 and (y<= len(laberinto[0])-1):
        if x == len(laberinto)-1 and y == len(laberinto[0])-1: 
            salida.append([x, y])
            print ('Llegaste!, el camino para llegar al final fue:')            
            print (salida)

        elif (laberinto[x][y] == 1):
            laberinto[x][y] = '*'
            salida.append([x, y])
            salida_del_laberinto(laberinto, x, y+1,salida)
            salida_del_laberinto(laberinto, x, y-1,salida)
            salida_del_laberinto(laberinto, x+1, y,salida)
            salida_del_laberinto(laberinto, x-1, y,salida)
    
    if ([len(laberinto)-1, len(laberinto[0])-1]) not in salida:
        return False

laberinto =     [[1, 1, 1, 1, 0],
                 [0, 1, 0, 1, 0],
                 [1, 1, 1, 1, 1], 
                 [1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 1]]

# if salida_del_laberinto(laberinto, 0, 0) == False:
#     print ('El laberinto no tiene salida.')
# else:
#     salida_del_laberinto(laberinto, 0, 0)

 