class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izquierdo) - self._altura(nodo.derecho)

    def _rotacion_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho
        x.derecho = y
        y.izquierdo = T2
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))
        return x

    def _rotacion_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo
        y.izquierdo = x
        x.derecho = T2
        x.altura = 1 + max(self._altura(x.izquierdo), self._altura(x.derecho))
        y.altura = 1 + max(self._altura(y.izquierdo), self._altura(y.derecho))
        return y

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)
        else:
            nodo.derecho = self._insertar(nodo.derecho, valor)

        nodo.altura = 1 + max(self._altura(nodo.izquierdo), self._altura(nodo.derecho))
        balance = self._balance(nodo)

        if balance > 1 and valor < nodo.izquierdo.valor:
            return self._rotacion_derecha(nodo)
        if balance < -1 and valor > nodo.derecho.valor:
            return self._rotacion_izquierda(nodo)
        if balance > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self._rotacion_izquierda(nodo.izquierdo)
            return self._rotacion_derecha(nodo)
        if balance < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self._rotacion_derecha(nodo.derecho)
            return self._rotacion_izquierda(nodo)

        return nodo

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

avl = ArbolAVL()
avl.insertar(10)
avl.insertar(20)
avl.insertar(30)
