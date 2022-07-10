class Nodo:
    #constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.caminos: list[Camino] = []
    def distanciaCamino(self, nombre:str):
        findByName = lambda camino: camino.nodo.nombre == nombre
        return list(filter(findByName, self.caminos))[0].distancia
    #metodo para mostrar la información que se va a imprimir
    def __str__(self):
        str="NODO: " + self.nombre + " - "
        str+="CAMINOS:\n"
        for camino in self.caminos:
            str+="\t"+camino.__str__()+"\n"
        return str

class Camino:
    def __init__(self, nodo: Nodo, distancia: int):
        self.nodo = nodo
        self.distancia = distancia
    def __str__(self):
        return "Camino: " + self.nodo.nombre + " - " + str(self.distancia)

class Ruta:
    def __init__(self):
        self.nodos: list[Nodo] = []
        self.distanciaTotal = 0
    def __str__(self):
        str = "Ruta:\n"
        for nodo in self.nodos:
            str += "\t" + nodo.__str__() + "\n"
        str += "Distancia total: " + self.distanciaTotal.__str__()
        return str