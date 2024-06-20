from nodo import Nodo

class ListaEnlazada():
    
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def get_primero(self):
        return self.primero
    def set_primero(self,nuevo_primero):
        self.primero=nuevo_primero

    def get_ultimo(self):
        return self.ultimo
    
    def set_ultimo(self,nuevo_ultimo):
        self.ultimo=nuevo_ultimo
        
    def insertarNodo(self, dato):
        nodoNuevo=Nodo(dato)
        if self.get_primero()==None:
            self.primero=nodoNuevo
            self.primero.set_siguiente(None)
            self.ultimo=self.primero
        else: 
            self.ultimo.set_siguiente(nodoNuevo)
            nodoNuevo.set_siguiente(None)
            self.ultimo=nodoNuevo
    def buscar_lista(self, numero):
        nodoActual = self.primero
        while nodoActual is not None:
            if nodoActual.get_dato().numero == numero:
                return nodoActual
            nodoActual = nodoActual.get_siguiente()
        return "Jugador no encontrado"
    def modificar_lista(self, numero, nuevo_nombre, nuevo_numero, nueva_posicion):
        nodoActual = self.buscar_lista(numero)
        if nodoActual is not None:
            nodoActual.get_dato().nombre = nuevo_nombre
            nodoActual.get_dato().numero = nuevo_numero
            nodoActual.get_dato().posicion = nueva_posicion
            return True
        return False
    def eliminar_nodo(self, numero):
        nodoActual = self.primero
        nodoAnterior = None
        while nodoActual is not None:
            if nodoActual.get_dato().numero == numero:
                if nodoAnterior is None:
                    self.primero = nodoActual.get_siguiente()
                else:
                    nodoAnterior.set_siguiente(nodoActual.get_siguiente())
                if nodoActual == self.ultimo:
                    self.ultimo = nodoAnterior
                return True
            nodoAnterior = nodoActual
            nodoActual = nodoActual.get_siguiente()
        return False
    def mostrarLista(self):
        nodoActual=self.primero
        listastring=""
        while nodoActual != None:
            listastring= listastring+str(nodoActual.get_dato())+"\n"
            nodoActual=nodoActual.get_siguiente()
        return listastring
            
    