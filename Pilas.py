class nodoPila(object):
    """clase nodo Pila"""
    info, sig = None, None

class Pila(object):
    """clase pila"""

    def __init__(self) -> None:
        """crea una pila vacia"""
        self.cima = None
        self.tamanio = 0
    
    def apilar(pila, dato):
        """apilar el dato sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.tamanio += 1

    def desapilar(pila):
        """desapila el elemento de la cima de la pila y lo devuelve"""
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x

    def pila_vacia(pila):
        """devuelve true si la pila esta vacia"""
        return pila.cima is None
    
    def en_cima(pila):
        """devuelve el valor almacenado en la cima de la pila"""
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
    
    def tamanio(pila):
        """devuelve el numero de elementos de la pila"""
        return pila.tamanio
    
    def barrido(pila):
        """muestra el contenido de la pila sin perder datos"""
        paux = Pila()
        while(not pila_vacia(pila)):
            dato = desapilar(pila)
            print (dato)
            apilar(paux, dato)
