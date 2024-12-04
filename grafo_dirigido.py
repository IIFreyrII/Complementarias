class GrafoDirigido:
    def __init__(self):
        self.adyacencias = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = []

    def agregar_arista(self, origen, destino):
        self.adyacencias[origen].append(destino)

    def imprimir(self):
        for vertice, vecinos in self.adyacencias.items():
            print(f"{vertice} -> {vecinos}")

grafo = GrafoDirigido()
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.imprimir()
