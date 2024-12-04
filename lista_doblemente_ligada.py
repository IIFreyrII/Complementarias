class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def mostrar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def mostrar_atras(self):
        actual = self.cabeza
        if not actual:
            return
        while actual.siguiente:
            actual = actual.siguiente
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.anterior
        print("None")

lista_doble = ListaDoble()
lista_doble.agregar(1)
lista_doble.agregar(2)
lista_doble.agregar(3)
lista_doble.mostrar_adelante()
lista_doble.mostrar_atras()
