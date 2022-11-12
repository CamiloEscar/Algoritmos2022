def nodoArbol():
    nodo = {
        'info' : None,
        'der' : None,
        'izq' : None
    }
    return nodo

def insertar_nodo(arbol, dato):
    if arbol['info'] is None:
        arbol['info'] = dato
    elif dato < arbol['info']:
        if arbol['izq'] is None:
            arbol['izq'] = nodoArbol()
        insertar_nodo(arbol['izq'], dato)
    else:
        if arbol['der'] is None:
            arbol['der'] = nodoArbol()
        insertar_nodo(arbol['der'], dato)

def arbol_vacio():
    return arbol ['info'] is None

def preorden(arbol):
        if arbol is not None:
            print(arbol['info'])
            preorden(arbol['izq'])
            preorden(arbol['der'])

def inorden(arbol):
    if arbol is not None:
        inorden(arbol['izq'])
        print(arbol['info'])
        inorden(arbol['der'])

def postorden(arbol):
    if arbol is not None:
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])

def eliminar_nodo(arbol, clave):
    x = None
    if (arbol['info'] is not None):
        if clave < arbol['info']:
            x = eliminar_nodo(arbol['izq'],clave)
        elif clave > arbol['info']:
            x = eliminar_nodo(arbol['der'],clave)
        else:
            x = arbol['info']
            if arbol['izq'] is None and arbol['der'] is not None:
                arbol = arbol['der']
            elif arbol['der'] is None and arbol['izq'] is not None:
                arbol = arbol['izq']

    return x

#Funciones EJ Nº5  

def inorden_solo_villanos (self):
    """Realiza el barrido inorden del arbol mostrando solo a los villanos.
    Los elementos se listan en orden descendiente (menor a mayor)."""
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.inorden_solo_villanos()
        if (not self.datos['Bando']): 
            print (self.info)
        if (self.der is not None):
            self.der.inorden_solo_villanos()

def inorden_heroes_LetraC (self):
    """Realiza el barrido inorden del arbol mostrando solo a los heroes cuyo nombre comienza con C.
    Los elementos se listan en orden ascendente (menor a mayor)."""
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.inorden_heroes_LetraC() #ordeno de menor a mayor
        if (self.info[0]=='C'):#en el .info guardo la informacion del nodo.
            print (self.info)
        if (self.der is not None):
            self.der.inorden_heroes_LetraC()

def contar_nodos (self, categoria):#categoria= campo que le paso (true o false)
    """Cuenta la cantidad de nodos (villanos o heroes) en el arbol, dependiendo de la categoria dada (True para heroes, False para villanos)."""
    cantidad = 0
    if (self.info is not None):#si la raiz el 1er nodo del arbol no esa vacia.
        if (self.datos['Bando'] == categoria):
            cantidad += 1
        #recorro los nodos y llamo a la funcion. 
        if (self.izq is not None):
            cantidad += self.izq.contar_nodos(categoria)
        if (self.der is not None):
            cantidad += self.der.contar_nodos(categoria)
    return cantidad #retorna la cantidad total.

def postorden_heroes (self):
    """Realiza el barrido postorden del los superheroes en el arbol.
    Los elementos se listan en orden descendente (mayor a menor)."""
    if(self.info is not None):
        if(self.der is not None):
            self.der.postorden_heroes()
        if (self.datos['Bando']):
            print(self.info)
        if(self.izq is not None):
            self.izq.postorden_heroes()

def separar_arbol (self, arbol_aux, categoria):
    """Separa los elementos del arbol en base a la categoria dada (True para heroes, False para villanos)."""
    if(self.info is not None):
        if (self.datos['Bando'] == categoria):
            arbol_aux = arbol_aux.insertar_nodo(self.info, self.datos)#asigno el arbol_auxiliar al insertar nodo
        if(self.izq is not None):
            arbol_aux = self.izq.separar_arbol(arbol_aux, categoria)
        if(self.der is not None):
            arbol_aux = self.der.separar_arbol(arbol_aux, categoria)
    return arbol_aux




#Funciones EJ Nº 23

def barrido_derrotados_por(self):
    #Realiza el barrido inorden del arbol de criaturas mostrando la criatura y quien la capturo.
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.barrido_derrotados_por()
        if (self.datos['capturada'] != ''):
            print (self.info, ' fue derrotada por ', self.datos['capturada'])
        if (self.der is not None):
            self.der.barrido_derrotados_por()

def cargar_descripcion (self, criatura):
    """Carga una breve descripcion de la criatura si ésta existe en el arbol."""
    pos = self.busqueda(criatura)
    if (pos):
        desc = input('Ingrese una breve descricpion de la criatura: ')
        pos.datos['descripcion'] = desc
    else:
        print('No hay ninguna criatura con ese nombre en el arbol.')

def mostrar_informacion (self, criatura):
    pos = self.busqueda(criatura)
    if (pos):
        print(pos.info, '· Capturada por:' ,pos.datos['capturada'], '· Descripcion:' , pos.datos['descripcion'])
    else:
        print('No hay ninguna criatura con ese nombre.')

def contador_criaturas_derrotadas(self, dic):
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.contador_criaturas_derrotadas(dic)
        if (self.datos['capturada'] in dic and self.datos['capturada'] != ''):
            dic[self.datos['capturada']] += 1 #el dic tiene un solo campo, el nombre del heroe, al que se le asigna un valor numericoo (Cantidad de capturas)
        elif (self.datos['capturada'] != ''):
            dic[self.datos['capturada']] = 1
        if (self.der is not None):
            self.der.contador_criaturas_derrotadas(dic)

def criaturas_derrotadas (self, heroe):
    """Muestra las criaturas derrotadas por un heroe dado."""  
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.criaturas_derrotadas(heroe)
        if (self.datos['capturada'] == heroe):
            print (self.info)
        if (self.der is not None):
            self.der.criaturas_derrotadas(heroe)

def criaturas_no_derrotadas (self):
    """Muestra las criaturas que no han sido derrotadas."""  
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.criaturas_no_derrotadas()
        if (self.datos['capturada'] == ''):
            print (self.info)
        if (self.der is not None):
            self.der.criaturas_no_derrotadas()

def modificar_captura (self, criatura, heroe):
    """Modifica quien capturo a la criatura dada por el heroe dado."""
    pos = self.busqueda(criatura)
    if (pos):
        pos.datos['capturada'] = heroe
    else:
        print('No hay ninguna criatura con el nombre', criatura, 'en el arbol.')

def busqueda_por_coincidencia(self, clave):
    if(self.info is not None):
        if(self.izq is not None):
            self.izq.busqueda_por_coincidencia(clave)
        if(clave in self.info):
            print(self.info)
        if(self.der is not None):
            self.der.busqueda_por_coincidencia(clave)


arbol = nodoArbol()


insertar_nodo(arbol, 1)
insertar_nodo(arbol, 0)
insertar_nodo(arbol, 2)
insertar_nodo(arbol, 11)
insertar_nodo(arbol, 12)
insertar_nodo(arbol, 7)
insertar_nodo(arbol, 6)
insertar_nodo(arbol, 27)
insertar_nodo(arbol, 45)

value = eliminar_nodo(arbol,7)
print('valor eliminado',7)

print(arbol)
print('preorden')
preorden(arbol)
print('inorden')
inorden(arbol)
print('postorden')
postorden(arbol)

value = eliminar_nodo(arbol,7)
print('valor eliminado',7)

