from cola import Cola
from heap import HeapMax


'''16- Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:'''

cola_prioridad = HeapMax()

# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
cola_prioridad.arribo('DocumentoEmpleado1', 1)
cola_prioridad.arribo('DocumentoEmpleado2', 1)
cola_prioridad.arribo('DocumentoEmpleado3', 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print(cola_prioridad.atencion()[1])
print()

# c. cargue dos documentos del staff de TI.
cola_prioridad.arribo('DocumentoTI1', 2)
cola_prioridad.arribo('DocumentoTI2', 2)

# d. cargue un documento del gerente.
cola_prioridad.arribo('DocumentoGerente1', 3)

# e. imprima los dos primeros documentos de la cola.
print(cola_prioridad.atencion()[1])
print(cola_prioridad.atencion()[1])
print()

# f. cargue dos documentos de empleados y uno de gerente.
cola_prioridad.arribo('DocumentoEmpleado4', 1)
cola_prioridad.arribo('DocumentoEmpleado5', 1)
cola_prioridad.arribo('DocumentoGerente2', 3)

# g. imprima todos los documentos de la cola de impresión.
while (not cola_prioridad.vacio()):
    print(cola_prioridad.atencion()[1])

print()


'''18. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
tiene mayor cantidad.
d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
mayor que 506.
'''
cola0 = Cola()
cola1 = Cola()
cola2 = Cola()
from random import randint, choice

def codigo_turno ():
    letras = ['A','B','C','D','E','F']
    turno = choice(letras)+ str(randint(0,9))+ str(randint(0,9))+ str(randint(0,9))
    return turno

#A
for i in range(20):
    turno= codigo_turno()
    #print(turno)
    cola0.arribo(turno)

#B
print()
while not cola0.cola_vacia():
    turno = cola0.atencion()
    if (turno[0] == 'A' or turno[0] == 'C' or turno[0] == 'F'):
        cola1.arribo(cola0)
        #cola1 = turno
        print(turno)
#    if (turno[0] == 'B' or turno[0] == 'D' or turno[0] == 'E'):
    else:
        cola2.arribo(cola0)
        print(turno)   

#C

print()
if cola1.tamanio() > cola2.tamanio():
    print('cola1 hay ',cola1.tamanio())
    cont1=0
    cont2=0
    cont3=0
    if (turno[0] == 'A'):
        #cola1.arribo(turno)
        cont1+=1
    if (turno[0] == 'C'):
        #cola1.arribo(turno)
        cont2+=1        
    if (turno[0] == 'E'):
        #cola1.arribo(turno)
        cont3+=1
      
else:
    print('cola2 hay ',cola2.tamanio())
    cont4=0
    cont5=0
    cont6=0
    if (turno[0] == 'B'):
        #cola2.arribo(turno)
        cont4+=1 
    if (turno[0] == 'D'):
        #cola2.arribo(turno)
        cont5+=1
    if (turno[0] == 'F'):
        #cola2.arribo(turno)
        cont6+=1

while cola1.tamanio() > cola2.tamanio():

    if (cont1 > cont2 and cont1 > cont3):
        print('LETRA A  ')
    if (cont2 > cont1 and cont2 > cont3):
        print('LETRA C  ',cont2)
    if (cont3 > cont2 and cont3 > cont1):
        print('LETRA E  ',cont3)
else:
        
    if (cont4 > cont5 and cont4 > cont6):
        print(' LETRA B',cont4)
    if (cont5 > cont4 and cont5 > cont6):
        print(' LETRA D', cont5)
    if (cont6 > cont5 and cont6 > cont4):
        print(' LETRA F',cont6)


print()

#_____________________________________

from cola import Cola
from random import randint, choice


c = Cola()
cola_1 = Cola()
cola_2 = Cola()
cola_aux1 = Cola()
cola_aux2 = Cola()
c1_turno = 0
c2_turno = 0
CA = 0
CB = 0
CC = 0
CD = 0 
CE = 0
CF = 0

def generar_turno():

    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    turno = choice(letras)+ str(randint(0,9))+ str(randint(0,9))+ str(randint(0,9))
    return turno

#!Punto A
for i in range(0,1000):
    turno = generar_turno()
    print(turno)
    c.arribo(turno)


#!Punto B
while not c.cola_vacia():
    turno = c.atencion()
    if (turno[0] == 'A' or turno[0] == 'C' or turno[0] == 'F'):
        cola_1.arribo (turno)
        print('Turnos con A, C y F', turno)
    else:
        cola_2.arribo (turno)
        print('Turnos con B, D y E', turno)


#!Punto C
if(cola_1.tamanio () > cola_2.tamanio()):
    print('la cola 1 tiene mayor cantidad de turno', cola_1.tamanio())
else:
    print('la cola 2 tiene mayor cantidad de turnos', cola_2.tamanio())

while(not cola_1.cola_vacia()):
    turno = cola_1.atencion()
    print(turno)
    c1_turno += 1
    if(turno[1] > '506'):
        cola_aux1.arribo(turno)
    if(turno[0] == 'A'):
        CA += 1
    else:
        if(turno[0] == 'C'):
            CC += 1
        else:
            CF += 1


while(not cola_2.cola_vacia()):
    turno = cola_2.atencion()
    print(turno)
    c2_turno += 1
    if(turno[1] > '506'):
        cola_aux2.arribo(turno)
    if(turno[0] == 'B'):
        CB += 1
    else:
        if(turno[0] == 'D'):
            CD += 1
        else:
            CE += 1

    
if(c1_turno > c2_turno):
    print('La cola con mas turnos es la 1')
    if(CA > CC and CA > CF):
        print('La letra que predomina en los turnos es la A')
    else:
        if(CC > CA and CC > CF):
            print('La letra que predomina en los turnos es la C')
        else:
            print('La letra que predomina en los turnos es la F')
else:
    print('La cola con mas turnos es la 2')
    if(CB > CD and CB > CE):
        print('La letra que predomina en los turnos es la B')
    else:
        if(CD > CB and CD > CE):
            print('La letra que predomina en los turnos es la D')
        else:
            print('La letra que predomina en los turnos es la E')


# #!Punto D
if(c1_turno < c2_turno):
    
    while(not cola_aux1.cola_vacia()):
        turno = cola_aux1.atencion()
        print()
        print('La cola con menos turnos cuyo numero es mayor que 506 es la 1 ',  turno)
else:
    while(not cola_aux2.cola_vacia()):
        turno = cola_aux2.atencion()
        print()
        print('La cola con menos turnos cuyo numero es mayor que 506 es la 2 ',   turno)



'''22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes.'''

class Personaje (object):

    def __init__(self, nombre, alter_ego, genero):
        self.nombre = nombre
        self.alter_ego = alter_ego
        self.genero = genero

    def __str__(self):
        return self.nombre + ' - ' + self.alter_ego + ' - ' + self.genero

cola_personajes = Cola()
cola_F = Cola()
cola_M = Cola()
cola_S = Cola()

personajes = [ ('Tony Stark','Iron Man','M'),('Steve Rogers','Captain America','M'),('Natasha Romanoff','Black Widow','F'),
            ('Wanda Maximoff','Scarlet Witch','F'),('Clint Barton','Hawkeye','M'),('Bruce Banner','Hulk','M'),
            ('Carol Danvers','Captain Marvel','F'),('Hope Van Dyne','The Wasp','F'),('Scott Lang','Ant-Man','M'),
            ('Thor Odinson','Thor','M'),("T'challa",'Black Panther','M'),('Pepper Potts','Rescue','F'),
            ('Peter Parker','Spider-Man','M'),('Gamora','Gamora','F')]


for (a,b,c) in personajes:
    personaje = Personaje(a, b, c)
    cola_personajes.arribo(personaje)

while not cola_personajes.cola_vacia():
    x = cola_personajes.atencion()
    if (x.alter_ego == 'Captain Marvel'):
        print ('El nombre de', x.alter_ego, 'es', x.nombre)
    if (x.nombre == 'Scott Lang'):
        print ('El nombre de superhéroe de', x.nombre, 'es', x.alter_ego)
    if (x.nombre == 'Carol Danvers'):
        print (x.nombre, 'se encuentra en la cola y su nombre de superhéroe es', x.alter_ego)
    if (x.nombre[0]=='S' or x.alter_ego[0]=='S'):
        cola_S.arribo(x)
    if (x.genero == 'F'):
        cola_F.arribo(x)
    else:
        cola_M.arribo(x) 

print()
print ('Nombres de los superhéroes femeninos:')
while (not cola_F.cola_vacia()):
    print (cola_F.atencion().alter_ego)

print()

print ('Nombres de los personajes masculinos:')
while (not cola_M.cola_vacia()):
    print (cola_M.atencion().nombre)

print()

print ('Personajes cuyos nombres empiezan con S:')
while (not cola_S.cola_vacia()):
    print (cola_S.atencion())