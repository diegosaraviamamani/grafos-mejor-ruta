from clases import Ciudad

getInfo = lambda costo, porcentaje: [costo, porcentaje]

infoCampaña = [
  [None,getInfo(1600,6),getInfo(1200,7),getInfo(1900,9),getInfo(1050,1),getInfo(900,13),getInfo(950,14)],
  [getInfo(1600,0),None,getInfo(1000,2),getInfo(1050,3),getInfo(1100,8),getInfo(1600,1),getInfo(800,3)],
  [getInfo(1200,0),getInfo(1000,2),None,getInfo(1900,11),getInfo(1000,12),getInfo(1800,2),getInfo(1300,4)],
  [getInfo(1900,0),getInfo(1050,3),getInfo(1900,11),None,getInfo(500,7),getInfo(700,6),getInfo(1200,3)],
  [getInfo(1050,0),getInfo(1100,8),getInfo(1000,12),getInfo(500,7),None,getInfo(300,5),getInfo(1100,2)],
  [getInfo(900,0),getInfo(1600,1),getInfo(1800,2),getInfo(700,6),getInfo(300,5),None,getInfo(200,15)],
  [getInfo(950,0),getInfo(800,3),getInfo(1300,4),getInfo(1200,3),getInfo(1100,2),getInfo(200,15),None]
]

grafo = [
  Ciudad("Desembarco"),
  Ciudad("Volanis"),
  Ciudad("Bravos"),
  Ciudad("Qarth"),
  Ciudad("Asshai"),
  Ciudad("Meereen"),
  Ciudad("Pentos"),
]