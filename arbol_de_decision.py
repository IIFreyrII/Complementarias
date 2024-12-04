class NodoDecision:
    def __init__(self, pregunta=None, valor=None):
        self.pregunta = pregunta
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolDecision:
    def __init__(self):
        self.raiz = None

    def construir_arbol(self):
        self.raiz = NodoDecision("¿Es mayor a 5?")
        self.raiz.izquierdo = NodoDecision(valor="Número pequeño")
        self.raiz.derecho = NodoDecision("¿Es par?")
        self.raiz.derecho.izquierdo = NodoDecision(valor="Número mayor e impar")
        self.raiz.derecho.derecho = NodoDecision(valor="Número mayor y par")

    def evaluar(self, nodo, entrada):
        if nodo.valor is not None:
            return nodo.valor
        if nodo.pregunta == "¿Es mayor a 5?":
            if entrada > 5:
                return self.evaluar(nodo.derecho, entrada)
            else:
                return self.evaluar(nodo.izquierdo, entrada)
        elif nodo.pregunta == "¿Es par?":
            if entrada % 2 == 0:
                return self.evaluar(nodo.derecho, entrada)
            else:
                return self.evaluar(nodo.izquierdo, entrada)

arbol = ArbolDecision()
arbol.construir_arbol()
entrada = 6
print(arbol.evaluar(arbol.raiz, entrada))
