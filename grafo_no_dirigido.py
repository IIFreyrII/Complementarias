class GrafoNoDirigido:
    def __init__(self):
        self.adyacencias = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        self.adyacencias[vertice1].append(vertice2)
        self.adyacencias[vertice2].append(vertice1)

    def imprimir(self):
        for vertice, vecinos in self.adyacencias.items():
            print(f"{vertice}: {vecinos}")

grafo = GrafoNoDirigido()
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.imprimir()
