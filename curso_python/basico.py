#-------------------->Tipos de datos<--------------------
print("-------------------->Tipos de datos<--------------------")
#Enteros: Son un conjunto conformado por los numeros naturales; 1, -2, 454 o 0
entero = 4
print(">>",entero)
print("El tipo de dato es: ",type(entero))
print()

#Flotantes: Son numeros decimales compuestos por un punto o una coma
float = 0.043
print(">>",float)
print("El tipo de dato es: ",type(float))
print()

#Booleanos: Son valores logicos como verdadero o falso
boolean = True
print(">>",boolean)
print("El tipo de dato es: ",type(boolean))
print()

#Cadena de caracteres o String: Son un conjunto de valores identificado entre comillas
string = "Hello world"
print(">>",string)
print("El tipo de dato es: ",type(string))
print()




#-------------------->Operadores Arigmeticos<--------------------
print("-------------------->Operadores Arigmeticos<--------------------")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
print(f'----->>El primer valor es "{valor1}" y el segundo valor es "{valor2}"<<-----')
print()

#Realiza una suma de valores
print(f'-->La suma de los valores es: {valor1 + valor2}')
print(">>valor1 + valor2")
#Realiza una resta de valores
print(f'-->La resta de los valores es: {valor1 - valor2}')
print(">>valor1 - valor2")
print()

#Realiza una multiplicacion de valores
print(f'-->La multiplicacion de los valores es: {valor1 * valor2}')
print(">>valor1 * valor2")
#Realiza una divicion de valores
print(f'-->La divicion de los valores es: {valor1 / valor2}')
print(">>valor1 / valor2")
print()



#-------------------->Operadores de asignacion<--------------------
print("-------------------->Operadores de asignacion<--------------------")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
print(f'----->>El primer numero es "{n1}" y el segundo numero es "{n2}"<<-----')
print()

#Adiccion: Agrega, aumenta o suma un valor
n1 += 2
print(f'-->El primer numero aumento "{n1}"')
print(">>n1 +=2")
#Sustraccion: Elimina, disminuye o resta un valor
n1 -= 4
print(f'-->El primer numero disminuyo "{n1}"')
print(">>n1 -=4")
print()

#Multicacion: Multiplica por un valor
n2 *= 2
print(f'-->El segundo numero se multiplico por 2 "{n2}"')
print(">>n2 *=2")
#Sustraccion: Elimina, disminuye o resta un valor
n2 /= 4
print(f'-->El segundo numero se dividio entre 4 "{n2}"')
print(">>n2 /=4")
print()



#-------------------->Operadores relacionales<--------------------
print("-------------------->Operadores relacionales<--------------------")
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
print(f'----->>El primer valor es "{valor1}" y el segundo valor es "{valor2}"<<-----')
print()


print("------------->Igual o distinto que<-------------")
#Realiza una compracion: ¿Son iguales los valores?
print(f'    ¿El primer valor es igual al segundo valor? :{valor1 == valor2}')
print(">>valor1 == valor2")
#Realiza una compracion: ¿Son distintos los valores?
print(f'    ¿El primer valor es distinto al segundo valor? :{valor1 != valor2}')
print(">>valor1 != valor2")
print()


print("------------->Mayor, menor o igual que<-------------")
#Realiza una compracion: ¿El primer valor es mayor que el segundo valor?
print(f'    ¿El primer valor es igual al segundo valor? :{valor1 > valor2}')
print(">>valor1 > valor2")
#Realiza una compracion: ¿El primer valor es mayor o igual al segundo valor?
print(f'    ¿El primer valor es igual al segundo valor? :{valor1 >= valor2}')
print(">>valor1 >= valor2")
print()

#Realiza una compracion: ¿El primer valor es menor que el segundo valor?
print(f'    ¿El primer valor es igual al segundo valor? :{valor1 < valor2}')
print(">>valor1 < valor2")
#Realiza una compracion: ¿El primer valor es nenor o igual al segundo valor?
print(f'    ¿El primer valor es igual al segundo valor? :{valor1 <= valor2}')
print(">>valor1 <= valor2")
print()



#-------------------->Condicionales<--------------------
print("-------------------->Condicionales<--------------------")
print("Colores primarios: Solo se aceptaran colores primarios")
color = str(input("Ingrese un color: "))

#Solo si se cumple la condicion: El color tiene que ser azul, rojo o amarillo
#El comando "or" indica que se aceptaran mas de una posiblidad, es decir el color puede ser "azul o rojo o amarillo"
if color == "azul" or color == "rojo" or color == "amarillo" :
    if color == "azul":
        print(f'El {color} si es un color primario y es el color del cielo')
    if color == "rojo":
        print(f'El {color} si es un color primario y es el color del fuego')
    if color == "amarillo":
        print(f'El {color} si es un color primario y es el color del sol')
else:
    print(f'>>El "{color}" no es un color primario')

print()
print("Combinacion de colores: Solo se aceptaran los colores que conforman el color verde")
color1 = str(input("Ingrese el primer color: "))
color2 = str(input("Ingrese el segundo color: "))

#Solo si se cumple la condicion: Colores que conformen el color verde
#El comando "and" inidca que solo se aceptara si el primer y segundo valor son "azul y amarillo" sin importar el orden
#Tampoco se aceptaran colores repetidos, es decir, el primer color no debe ser igual al segundo color
if color1 != color2:
    if color1 == "azul" or color1 == "amarillo" and color2 == "azul" or color2 == "amarillo":
        print(f">>Es correcto; el verde esta conformado por {color1} y {color2}")
else:
    print(f'>>El color verde no esta conformado por {color1} y {color2}')
print()

#-------------------->Bucles For y While<--------------------
print("-------------------->Bucle For<--------------------")
#Repite una funcion las veces que se le indique
palabra = str(input("Ingrese una palabra: "))
veces = int(input("¿Cuantas veces se debe repetir?: "))
contador = 1
#Repite la variable "palabra" en el rango definido por la variable "veces" y aumenta un contador
for repetir in range(veces):
    print(f'{contador}. {palabra}')
    contador += 1
print()

print("-------------------->Bucle While<--------------------")
#Repite una funcion hasta que se cumpla una condicion
palabra = str(input("Ingrese una palabra: "))
veces = int(input("¿Cuantas veces se debe repetir?: "))
contador = 1

#Repite la variable "palabra" las veces que sea nesesario mientras se cumpla la condicion, puede ser infinito
while contador <= veces:
    print(f'{contador}. {palabra}')
    contador += 1
    #Comprueba que el contador llego a su fin y finaliza el bucle
    if contador > veces:
        print(">>Fin del bucle")
        break
print()

input("...")