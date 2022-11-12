from arbol_binario import Arbol
from sys import getsizeof
from cola import Cola
# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel 
# Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo 
# booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por 
# proximidad para encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes 
# y otro a los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
arbol_superheroes = Arbol()
arbol_villanos = Arbol()
arbol_personajes = Arbol()

personajes = [{'nombre': 'Iron man', 'heroe': True},
                {'nombre': 'Doctor Octopus', 'heroe': False},
                {'nombre': 'Calavera', 'heroe': True},
                {'nombre': 'Thanos', 'heroe': False},
                {'nombre': 'Spider man', 'heroe': True},
                {'nombre': 'Doctor Strnge', 'heroe': False},
                {'nombre': 'Capitan America', 'heroe': True},
                {'nombre': 'Hulk', 'heroe': True},
                {'nombre': 'Capitana Marvel', 'heroe': True,}]

for personaje in personajes:
    arbol_personajes = arbol_personajes.insertar_nodo(personaje['nombre'],personaje)

arbol_personajes.inorden()

# b. listar los villanos ordenados alfabéticamente;
print("Listado en orden alfabetico de villanos")
arbol_personajes.inordenClave('heroe',False)

# c. mostrar todos los superhéroes que empiezan con C;
print("Héroes que empiezan con C: ") 
arbol_personajes.busqueda_proximidad('C')

# d. determinar cuántos superhéroes hay el árbol;
print('la cantidad de heroes en el arbol son:',arbol_personajes.contadorClave('heroe',True))

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
print ('modificar Doctor Strange')
arbol_personajes.busqueda_proximidad('D')
dato = input('ingrese el nombre a modificar: ')
modificado =input('ingrese el nombre modificado: ')

def modificar(arbol,clave,indice,modificado):
    pos = arbol.busqueda(indice)
    if (pos is not None):
        info, datos = arbol.eliminar_nodo(indice)
        if (info==datos[clave]):
            info=modificado
        datos[clave]=modificado
        arbol.insertar_nodo(info,datos)
        print (info,datos)
    else:print ('no se encontro',indice)

modificar(arbol_personajes,'nombre',dato,modificado)

# f. listar los superhéroes ordenados de manera descendente;
print("Barrido de manera descendente de los heroes: ")
arbol_personajes.postordenClave('heroe',True)

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes
# y otro a los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
def bosque(arbol, arbol1,clave,respuesta):
    if(arbol.info is not None):
        if(arbol.datos[clave] == respuesta):
            arbol1 = arbol1.insertar_nodo(arbol.info, arbol.datos)
        if(arbol.izq is not None):
            arbol1 = bosque(arbol.izq, arbol1, clave,respuesta)
        if(arbol.der is not None):
            arbol1 = bosque(arbol.der, arbol1, clave,respuesta)
    return arbol1

print(arbol_personajes.contador_nodos())
bosque(arbol_personajes,arbol_superheroes,'heroe',True)
bosque(arbol_personajes,arbol_villanos,'heroe',False)
print("Cantidad de nodos del arbol de villanos: ",arbol_villanos.contador_nodos())
print("Barrido del arbol de villanos:")
arbol_villanos.inorden()
print("Cantidad de nodos del arbol de heroes: ",arbol_superheroes.contador_nodos())
print("Barrido del arbol de heroes")
arbol_superheroes.inorden()



# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente 
# tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe 
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí 
# de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

arbolCriaturas=Arbol()

criaturas= [{'nombre': 'Ceto', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Tifon', 'derrotado_por': 'Zeus','descripcion':None,'capturada_por': None},
            {'nombre': 'Equidna', 'derrotado_por': 'Argos Panoptes','descripcion':None,'capturada_por': None},
            {'nombre': 'Dino', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Pefredo', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Enio', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Escila', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Caribdis', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Euriale', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Esteno', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Medusa', 'derrotado_por': 'Perseo','descripcion':None,'capturada_por': None},
            {'nombre': 'Ladon', 'derrotado_por': 'Heracles','descripcion':None,'capturada_por': None},
            {'nombre': 'Aguila del Caucaso', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Quimera', 'derrotado_por': 'Belerofonte','descripcion':None,'capturada_por': None},
            {'nombre': 'Hidra de Lerna', 'derrotado_por': 'Heracles','descripcion':None,'capturada_por': None},
            {'nombre': 'Leon de Nemea', 'derrotado_por': 'Heracles','descripcion':None,'capturada_por': None},
            {'nombre': 'Esfinge', 'derrotado_por': 'Edipo','descripcion':None,'capturada_por': None},
            {'nombre': 'Dragon de la Colquida', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Cerbero', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Cerda de Cromion', 'derrotado_por': 'Teseo','descripcion':None,'capturada_por': None},
            {'nombre': 'Ortro', 'derrotado_por': 'Heracles','descripcion':None,'capturada_por': None},
            {'nombre': 'Toro de Creta', 'derrotado_por': 'Teseo','descripcion':None,'capturada_por': None},
            {'nombre': 'Jabali de Calidon', 'derrotado_por': 'Atalanta','descripcion':None,'capturada_por': None},
            {'nombre': 'Carcinos', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Gerion', 'derrotado_por': 'Heracles','descripcion':None,'capturada_por': None},
            {'nombre': 'Cloto', 'derrotado_por': 'Zeus','descripcion':None,'capturada_por': None},
            {'nombre': 'Laquesis', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Atropos', 'derrotado_por':None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Minotauro de Creta', 'derrotado_por': 'Teseo','descripcion':None,'capturada_por': None},
            {'nombre': 'Harpias', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Argos Panoptes', 'derrotado_por': 'Hermes','descripcion':None,'capturada_por': None},
            {'nombre': 'Aves del Estinfalo', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Talos', 'derrotado_por': 'Medea','descripcion':None,'capturada_por': None},
            {'nombre': 'Sirenas', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Piton', 'derrotado_por': 'Apolo','descripcion':None,'capturada_por': None},
            {'nombre': 'Cierva de Cerinea', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Basilisco', 'derrotado_por': None,'descripcion':None,'capturada_por': None},
            {'nombre': 'Jabali de Erimanto', 'derrotado_por': None,'descripcion':None,'capturada_por': None}]

for criatura in criaturas:
    arbolCriaturas = arbolCriaturas.insertar_nodo(criatura['nombre'],criatura)

dic={}

# A
arbolCriaturas.inorden()

# B
# buscado =input ('ingrese el nombre de la criatura a la que desea agregarle descripcion ')
# descripcion = input ('ingrese la descripcion: ')
# modificar(arbolCriaturas,'descripcion',buscado,descripcion)

# c
arbolCriaturas.busqueda_proximidad('Talos')

# d
arbolCriaturas.contador_criaturas_derrotadas(dic)
def ordenar(item):
    return item[1]
lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)
print(lista[:3])

# e
arbolCriaturas.inordenClave('derrotado_por', 'Heracles')

# f
arbolCriaturas.inordenClave('derrotado_por', None)

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí 
# de Erimanto indicando que Heracles las atrapó;

modificar(arbolCriaturas,'capturada_por','Cerbero','Heracles')
modificar(arbolCriaturas,'capturada_por','Toro de Creta','Heracles')
modificar(arbolCriaturas,'capturada_por','Cierva de Cerinea','Heracles')
modificar(arbolCriaturas,'capturada_por','Jabali de Erimanto','Heracles')

# i. se debe permitir búsquedas por coincidencia;
print ('busqeuda por coincidencia')
arbolCriaturas.busqueda_proximidad('G')

# j. eliminar al Basilisco y a las Sirenas;
arbolCriaturas.eliminar_nodo('Basilisco')
# arbolCriaturas.eliminar_nodo('Sirenas')

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
modificar(arbolCriaturas,'derrotado_por','Aves del Estinfalo', 'Heracles')

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
modificar(arbolCriaturas,'nombre','Ladon', 'Dragon Ladon')

# m. realizar un listado por nivel del árbol;
arbolCriaturas.barrido_por_nivel()

# n. muestre las criaturas capturadas por Heracles.
arbolCriaturas.inordenClave('capturada_por', 'Heracles')