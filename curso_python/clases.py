class Carro:
    def __init__ (self, color, motor, marca):
        self.color= color
        self.motor= motor
        self.marca = marca
        

    def nuevo(self):
        return "El estado del auto es Nuevo."

    def usado(self):
        return "El estado del auto es Usado."
    
    def reacondicionado(self):
        return "El estado del auto es Reacondicionado."


carros = {
    "rx7": Carro("verde", "r4", "mazda"),
    "mk4": Carro("negro", "l6", "toyota"),
    "gtr34": Carro("azul", "v8", "nissan"),
    "corvette": Carro("rojo", "v12", "chevrolet")
}

registrar_modelo = str(input("Ingrese un modelo: "))
print("  CARACTERISTICAS  ")
registrar_color = str(input("¿De que color es?: "))
registrar_motor = str(input("¿Que motor integra?: "))
registrar_marca = str(input("¿De que marca es?: "))

registrar_nuevo = {registrar_modelo: Carro(registrar_color,registrar_motor,registrar_marca)}

carros.update(registrar_nuevo)


print()
busqueda = input("Qué modelo desea buscar: ")
if busqueda in carros:
        modelo = carros[busqueda]
        print(f"""
    Modelo: {busqueda.upper()}
            
El color del auto es: {modelo.color}
El auto integra un motor: {modelo.motor}
El la marca del auto es: {modelo.marca}
El estado del auto es: {modelo.nuevo()}
""")


       
else:
    print("No se encontraron resultados...")



input("...")