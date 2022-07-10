class Ciudad:
    #constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.conquistas: list[Conquista] = []
    def obtenerInfoConquista(self, nombre:str):
        findByName = lambda conquista: conquista.ciudad.nombre == nombre
        return list(filter(findByName, self.conquistas))[0]

class Conquista:
    def __init__(self, nodo: Ciudad, costo: int, porcentaje: int):
        self.ciudad = nodo
        self.costo = costo
        self.porcentajeMuertes = porcentaje

class Ruta:
    def __init__(self):
        self.ciudades: list[Ciudad] = []
        self.oro = 20000
        self.soldados = 1000
    def agregarConquista(self, conquista: Conquista):
        self.ciudades.append(conquista.ciudad)
        self.oro -= conquista.costo
        self.soldados -= int(self.soldados*conquista.porcentajeMuertes/100)
    def __str__(self) -> str:
        result = "\nRUTA: "
        for ciudad in self.ciudades:
            result += ciudad.nombre
            if(ciudad != self.ciudades[-1]):
                result += " => "
        result += "\nORO RESTANTE: " + str(self.oro)
        result += "\nSOLDADOS RESTANTES: " + str(self.soldados)
        return result