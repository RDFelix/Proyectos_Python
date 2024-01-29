class User:
    def __init__ (self, id, sexo, fecha_nacimiento, edad, nombre, apellido):
        self.__id = id
        self._genero = sexo
        self._fecha = fecha_nacimiento
        self.años = edad

        self.nombre = nombre
        self.apellido = apellido

    def adulto(self):
        return "Mayor de edad."

    def joven(self):
        return "Menor de edad."


persona1 = User(1119391637,"Masculino","13/08/2005",22,"felix gabriel","ruiz duran")

edad = int(persona1.años)
estado = ""
if edad >= 18:
    estado = str(persona1.adulto())
else:
    estado = str(persona1.joven())

print(f"""
    Nombre: {(persona1.apellido.upper())} {(persona1.nombre).upper()}
    N°: {persona1._User__id}

    Genero: {persona1._genero}     Fecha de nacimiento: {persona1._fecha}
    Estado: {estado}
""")


input("...")