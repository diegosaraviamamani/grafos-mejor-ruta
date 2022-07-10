from AlgoritmoTSP import AlgoritmoTSP
from clases import Camino, Nodo

nodoA = Nodo("A")
nodoB = Nodo("B")
nodoC = Nodo("C")
nodoD = Nodo("D")

nodoA.caminos.append(Camino(nodoB, 9))
nodoA.caminos.append(Camino(nodoC, 7))
nodoA.caminos.append(Camino(nodoD, 8))

nodoB.caminos.append(Camino(nodoA, 9))
nodoB.caminos.append(Camino(nodoC, 10))
nodoB.caminos.append(Camino(nodoD, 15))

nodoC.caminos.append(Camino(nodoA, 7))
nodoC.caminos.append(Camino(nodoB, 10))
nodoC.caminos.append(Camino(nodoD, 4))

nodoD.caminos.append(Camino(nodoA, 8))
nodoD.caminos.append(Camino(nodoB, 15))
nodoD.caminos.append(Camino(nodoC, 4))

grafo = [nodoA, nodoB, nodoC, nodoD]

tsp = AlgoritmoTSP(grafo, 10, nodoB)
tsp.caminar()
print(tsp.todasLasRutas)