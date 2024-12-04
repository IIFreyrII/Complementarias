class BST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierdo:
                self.izquierdo.insertar(valor)
            else:
                self.izquierdo = BST(valor)
        else:
            if self.derecho:
                self.derecho.insertar(valor)
            else:
                self.derecho = BST(valor)

    def buscar(self, valor):
        if valor == self.valor:
            return True
        elif valor < self.valor and self.izquierdo:
            return self.izquierdo.buscar(valor)
        elif valor > self.valor and self.derecho:
            return self.derecho.buscar(valor)
        return False

raiz = BST(10)
raiz.insertar(5)
raiz.insertar(15)
print(raiz.buscar(5))  # True
print(raiz.buscar(20)) # False
