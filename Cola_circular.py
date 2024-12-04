class ColaCircular:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.items = [None] * tamaño
        self.frente = -1
        self.final = -1

    def encolar(self, item):
        if (self.final + 1) % self.tamaño == self.frente:
            print("La cola está llena.")
        else:
            if self.frente == -1:
                self.frente = 0
            self.final = (self.final + 1) % self.tamaño
            self.items[self.final] = item

    def desencolar(self):
        if self.frente == -1:
            print("La cola está vacía.")
        else:
            elemento = self.items[self.frente]
            if self.frente == self.final:
                self.frente = -1
                self.final = -1
            else:
                self.frente = (self.frente + 1) % self.tamaño
            return elemento

def prueba_cola_circular():
    cola = ColaCircular(3)
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    cola.encolar(4)  
    print(cola.desencolar())
    cola.encolar(4) 
    print(cola.desencolar())  

prueba_cola_circular()
