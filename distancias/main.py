from AlgoritmoTSP import AlgoritmoTSP
from clases import Camino, Nodo

# matriz de distancias
matriz = [
    [0, 9, 7, 8],
    [9, 0, 10, 15],
    [7, 10, 0, 4],
    [8, 15, 4, 0]
]
grafo = [Nodo("A"), Nodo("B"), Nodo("C"), Nodo("D")]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] != 0:
            grafo[i].caminos.append(Camino(grafo[j], matriz[i][j]))

tsp = AlgoritmoTSP(grafo, 10, grafo[3])
tsp.caminar()
print(tsp.todasLasRutas)