class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaLigada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.mostrar()
