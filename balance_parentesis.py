class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
    
    def esta_vacia(self):
        return len(self.items) == 0

def esta_balanceada(secuencia):
    pila = Pila()
    for caracter in secuencia:
        if caracter == '(':
            pila.apilar(caracter)
        elif caracter == ')':
            if pila.esta_vacia():
                return False
            pila.desapilar()
    return pila.esta_vacia()

# Prueba
print(esta_balanceada("(())"))  # True
print(esta_balanceada("(()"))   # False
