class Razas:
    def __init__(self,raza,piel,altura,poder,poblacion,dios):
        self.raza = raza
        self.piel = piel
        self.altura = altura
        self.poder = poder
        self.poblacion = poblacion
        self.dios = dios


class Elfos(Razas):
    def __init__(self,raza,piel,altura,poder,poblacion,dios,nombre):
        super().__init__(raza,piel,altura,poder,poblacion,dios)
        self.raza = "Elfo"
        self.piel = "Blanca"
        self.altura = "Alto"
        self.poder = "Clase B"
        self.poblacion = "Baja"
        self.dios = "Naturaleza"
        self.nombre = nombre


    def nombres(self):
        input("Ingrese el nombre de un elfo: ")

Elfos.nombres()

input("...")