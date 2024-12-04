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

def invertir_cadena(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida

# Prueba
print(invertir_cadena("Hola"))  # aloH
print(invertir_cadena("Python"))  # nohtyP
