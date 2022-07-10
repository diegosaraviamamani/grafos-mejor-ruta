from random import randint
from clases import Ruta, Ciudad, Conquista

class AlgoritmoTSP:
    __soluciones: list[Ruta]
    #constructor
    def __init__(self, grafo: list[Ciudad], n: int, origen: Ciudad):
        self.__grafo = grafo
        self.__n = n
        self.__origen = origen

    @property
    def todasLasRutas(self):
        str = ""
        for ruta in self.__soluciones:
            str += ruta.__str__() + "\n"
        return str

    def caminar(self):
        self.__soluciones = []
        for i in range(self.__n):
            self.__soluciones.append(self.generarRuta())

    def siguienteCiudad(self, actual: Ciudad)->Ciudad|None:
        siguienteIndice = randint(0, len(self.__grafo) - 2)
        return actual.conquistas[siguienteIndice].ciudad

    def generarRuta(self):
        solucion = Ruta()
        solucion.ciudades.append(self.__origen)
        actualCiudad = self.__origen
        for i in range(len(self.__grafo) - 1):
            #Buscar una ciudad que no haya sido visitada
            siguienteCiudad: Ciudad = self.siguienteCiudad(actualCiudad)
            while (siguienteCiudad in solucion.ciudades):
                siguienteCiudad = self.siguienteCiudad(actualCiudad)
            #buscamos la informacion de la conquista de la ciudad
            infoConquista: Conquista = actualCiudad.obtenerInfoConquista(siguienteCiudad.nombre)
            #agregamos la ciudad a la ruta
            solucion.agregarConquista(infoConquista)
            #Pasamos a la siguiente ciudad
            actualCiudad = siguienteCiudad
        #agregamos el regreso a la ciudad de origen
        solucion.ciudades.append(self.__origen)
        solucion.oro += actualCiudad.obtenerInfoConquista(self.__origen.nombre).costo
        return solucion

    def rutaMasEconomica(self):
        return min(self.__soluciones, key=lambda ruta: ruta.oro)

    def rutaMasSoldados(self):
        return min(self.__soluciones, key=lambda ruta: ruta.soldados)