class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

def simulacion_cola():
    cola = Cola()
    cola.encolar("Persona 1")
    cola.encolar("Persona 2")
    cola.encolar("Persona 3")
    print("Atendiendo a:", cola.desencolar())  
    print("Atendiendo a:", cola.desencolar()) 

simulacion_cola()
