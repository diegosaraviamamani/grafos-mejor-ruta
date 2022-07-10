from AlgoritmoTSP import AlgoritmoTSP
from clases import  Conquista
from data import infoCampaña, grafo

for i in range(len(infoCampaña)):
    for j in range(len(infoCampaña[i])):
        if infoCampaña[i][j] != None:
            costo, porcentajeMuertes = infoCampaña[i][j]
            grafo[i].conquistas.append(Conquista(grafo[j], costo, porcentajeMuertes))

tsp = AlgoritmoTSP(grafo, 10, grafo[0])
tsp.caminar()
print(tsp.todasLasRutas)
print(tsp.rutaMasEconomica())
print(tsp.rutaMasSoldados())