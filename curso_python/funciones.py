"""n = str(input("Cual es tu nombre?: "))
a = str(input("Cual es tu apellido?: "))

def nombres(nombre = "", apellido = ""):
    if nombre == "" or apellido == "":
        print("Ingrese un nombre y un apellido")
        return
    return (nombre + " " + apellido).upper()

print(f"Tu nombre es {nombres(n,a)}")



print("---------->Escriba 'fin' para terminar<----------")
nombres_estudiantes = []
x = 0
while x != True:
    estudiantes = str(input(">>Ingrese los estudiantes: "))
    if estudiantes == "fin":
        break
    else:
        nombres_estudiantes.append(estudiantes)
longitud = len(nombres_estudiantes)

def registro (*n):
    y = 0
    for i in range(longitud):     
        print(f"{y+1}. {n[0][y]}")
        y += 1

registro(nombres_estudiantes)


print("---------->Escriba 'fin' para terminar<----------")

diccionario = []

z = 0
while z != True:
    print()
    word = str(input("Ingrese una palabra: "))
    print("----------------------------------")
    print("¿Cual es la descriocion?")
    description = str(input(f"{word}: "))
    ingresar = str(input("¿Desea ingresar otro dato? y/n: "))
    if ingresar == "n":
        break
    else:
        diccionario.append(palabra(z)+word+": "+description)
"""


dtb = ({
    "nombre": "felix",
    "apellido": "ruiz",
    "edad": 17
    },
    {
    "nombre": "daniela",
    "apellido": "sarmiento",
    "edad": 17
    }
)


for i in dtb:
    print(i.items()[0][0])
input("...")