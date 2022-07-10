from random import randint
from clases import Nodo, Ruta

class AlgoritmoTSP:
    __soluciones: list[Ruta]
    #constructor
    def __init__(self, grafo: list[Nodo], n: int, origen: Nodo):
        self.__grafo = grafo
        self.__n = n
        self.__origen = origen

    @property
    def todasLasRutas(self):
        result = ""
        for ruta in self.__soluciones:
            for nodo in ruta.nodos:
                result += nodo.nombre + "-"
            result += " " + str(ruta.distanciaTotal) + "\n"
        return result

    def caminar(self):
        self.__soluciones = []
        for i in range(self.__n):
            self.__soluciones.append(self.generarRuta())

    def siguienteNodo(self, actual: Nodo)->Nodo|None:
        siguienteIndice = randint(0, len(self.__grafo) - 2)
        return actual.caminos[siguienteIndice].nodo

    def generarRuta(self):
        solucion = Ruta()
        solucion.nodos.append(self.__origen)
        actual = self.__origen
        for i in range(len(self.__grafo) - 1):
            siguiente: Nodo = self.siguienteNodo(actual)
            while (siguiente in solucion.nodos):
                siguiente = self.siguienteNodo(actual)
            solucion.nodos.append(siguiente)
            solucion.distanciaTotal += actual.distanciaCamino(siguiente.nombre)
            actual = siguiente
        solucion.nodos.append(self.__origen)
        solucion.distanciaTotal += actual.distanciaCamino(self.__origen.nombre)
        return solucion