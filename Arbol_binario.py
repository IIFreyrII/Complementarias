class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo:
                self._agregar_recursivo(nodo.izquierdo, valor)
            else:
                nodo.izquierdo = Nodo(valor)
        else:
            if nodo.derecho:
                self._agregar_recursivo(nodo.derecho, valor)
            else:
                nodo.derecho = Nodo(valor)

    def imprimir_preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.imprimir_preorden(nodo.izquierdo)
            self.imprimir_preorden(nodo.derecho)

arbol = ArbolBinario()
arbol.agregar(10)
arbol.agregar(5)
arbol.agregar(15)
arbol.imprimir_preorden(arbol.raiz)
