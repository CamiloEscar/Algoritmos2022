from grafo import Grafo
from pila import Pila

# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, 
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, 
# el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan 
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para 
# determinar cuántos metros de cable de red se necesitan para conectar el router con el 
# Smart Tv.

h = Grafo(dirigido=False)

h.insertar_vertice ('cocina')
h.insertar_vertice ('comedor')
h.insertar_vertice ('cochera')
h.insertar_vertice ('quincho')
h.insertar_vertice ('banio1')
h.insertar_vertice ('banio2')
h.insertar_vertice ('habitacion1')
h.insertar_vertice ('habitacion2')
h.insertar_vertice ('sala de estar')
h.insertar_vertice ('terraza')
h.insertar_vertice ('patio')

h.insertar_arista(3,'cocina','comedor')
h.insertar_arista(3,'cocina','patio')
h.insertar_arista(3,'cocina','habitacion2')
h.insertar_arista(3,'cocina','quincho')
h.insertar_arista(2,'cocina','habitacion1')
h.insertar_arista(4,'comedor','patio')
h.insertar_arista(5,'comedor','quincho')
h.insertar_arista(2,'comedor','habitacion2')
h.insertar_arista(3,'comedor','terraza')
h.insertar_arista(2,'comedor','sala de estar')
h.insertar_arista(3,'cochera','patio')
h.insertar_arista(2,'cochera','quincho')
h.insertar_arista(4,'cochera','cocina')
h.insertar_arista(3,'quincho','cocina')
h.insertar_arista(2,'quincho','habitacion')
h.insertar_arista(1,'quincho','patio')
h.insertar_arista(2,'banio1','habitacion1')
h.insertar_arista(3,'banio1','banio2')
h.insertar_arista(8,'banio1','terraza')
h.insertar_arista(7,'banio2','patio')
h.insertar_arista(6,'banio2','terraza')
h.insertar_arista(5,'banio2','habitacion1')
h.insertar_arista(4,'habitacion1','habitacion2')
h.insertar_arista(8,'habitacion1','sala de estar')
h.insertar_arista(7,'habitacion1','terraza')
h.insertar_arista(6,'habitacion2','terraza')
h.insertar_arista(3,'habitacion2','patio')
h.insertar_arista(2,'habitacion2','banio2')
h.insertar_arista(3,'sala de estar','banio1')
h.insertar_arista(9,'sala de estar','terraza')
h.insertar_arista(8,'sala de estar','patio')
h.insertar_arista(7,'terraza','patio')
h.insertar_arista(6,'terraza','quincho')
h.insertar_arista(5,'terraza','quincho')
h.insertar_arista(1,'patio','habitacion1')
h.insertar_arista(4,'patio','banio1')
h.insertar_arista(0,'patio','banio1')

arbol=h.kruskal_minimo()

for i in range(len(arbol)):
    arbol=h.kruskal_minimo()
    arbol = arbol[i].split('-')
    peso_total = 0
    for nodo in arbol:
        nodo = nodo.split(';')
        peso_total += int(nodo[2])
        print(f'{nodo[0]} - {nodo[1]} - {nodo[2]} ')
    print(f"La distancia total a recorrer: {peso_total} m ")
    print()

h.camino()

if h.existe_paso('habitacion1','sala de estar'):
    resultados = h.dijkstra('habitacion1')
    camino = h.camino(resultados,'habitacion1','sala de estar')
    print(f"La distancia total a recorrer: {camino} m ")
else:
    print('no puede llegar')

# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y 
# naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de 
# uno en las naturales) y tipo (natural o arquitectónica);

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar 
# la distancia que las separa;

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;

# e. determinar si algún país tiene más de una maravilla del mismo tipo;

# f. deberá utilizar un grafo no dirigido

g = Grafo(dirigido=False)

# ! maravillasnaturales
g.insertar_vertice('T', datos={'tipo': 'a', 'pais': 'egipto'})
g.insertar_vertice('Z', datos={'tipo': 'a', 'pais': 'francia'})
g.insertar_vertice('F', datos={'tipo': 'a', 'pais': 'china'})
g.insertar_vertice('X', datos={'tipo': 'a', 'pais': 'india'})
g.insertar_vertice('R', datos={'tipo': 'a', 'pais': 'eeuu'})
g.insertar_vertice('K', datos={'tipo': 'a', 'pais': 'brasil'})
# g.insertar_vertice('U')
#! maravillas arquitectonicas
g.insertar_vertice('L', datos={'tipo': 'n', 'pais': 'argentina-brasil-paragauy'})
g.insertar_vertice('J', datos={'tipo': 'n', 'pais': 'indonesia'})
g.insertar_vertice('I', datos={'tipo': 'n', 'pais': 'sudafrica'})
g.insertar_vertice('M', datos={'tipo': 'n', 'pais': 'india'})
g.insertar_vertice('S', datos={'tipo': 'n', 'pais': 'china'})
g.insertar_vertice('Y', datos={'tipo': 'n', 'pais': 'brasil'})

g.insertar_arista('L', 'J', 6)
g.insertar_arista('L', 'I', 3)
g.insertar_arista('I', 'M', 8)
g.insertar_arista('M', 'S', 2)
g.insertar_arista('M', 'Y', 2)
g.insertar_arista('Y', 'I', 9)

g.insertar_arista('T', 'X', 6)
g.insertar_arista('T', 'F', 3)
g.insertar_arista('T', 'R', 8)
g.insertar_arista('F', 'X', 2)
g.insertar_arista('F', 'R', 2)
g.insertar_arista('X', 'Z', 9)
g.insertar_arista('R', 'Z', 4)
g.insertar_arista('K', 'Z', 3)
g.insertar_arista('R', 'X', 5)

paises = g.contar_maravillas()
for pais in paises:
    print(pais, paises[pais])


arbol_min = g.kruskal()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el peso total es {peso_total}")

if g.existe_paso('T', 'Z'):
    resultados1 = g.dijkstra('T')
    camino = g.camino(resultados1, 'T', 'Z')
    print(camino)
else:
    print('no se puede llega de T a Z')
g.eliminar_arista('A', 'C')
g.eliminar_vertice('C')

g.barrido_profundidad('K')
print()
g.barrido_profundidad('T')
print('------------------------------------------')
g.barrido_profundidad('L')
print()
g.barrido_no_visitado()

g.adyacentes('A')

print(g.es_adyacente('A', 'F'))
print(g.es_adyacente('Z', 'A'))