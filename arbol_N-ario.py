class NodoNArio:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class ArbolNArio:
    def __init__(self, valor_raiz):
        self.raiz = NodoNArio(valor_raiz)

    def agregar_hijo(self, nodo_padre, valor_hijo):
        nodo_hijo = NodoNArio(valor_hijo)
        nodo_padre.hijos.append(nodo_hijo)
        return nodo_hijo

    def imprimir_preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            for hijo in nodo.hijos:
                self.imprimir_preorden(hijo)

arbol = ArbolNArio(1)
nodo2 = arbol.agregar_hijo(arbol.raiz, 2)
nodo3 = arbol.agregar_hijo(arbol.raiz, 3)
arbol.agregar_hijo(nodo2, 4)
arbol.agregar_hijo(nodo2, 5)
arbol.agregar_hijo(nodo3, 6)
arbol.imprimir_preorden(arbol.raiz)
