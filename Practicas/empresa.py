usr_root = "adm14"
usr_pass = "root123"



admin = str(input("Ingrese usuario admin: "))
while admin != "adm14":
    print()
    print("-->>¡Ingrese un usuario admin valido!<<--")
    admin = str(input("Ingrese usuario admin: "))



if admin == "adm14":
    pass_admin = str(input("Ingrese contraseña: "))
while pass_admin != "root123":
    print()
    print("-->>¡Contraseña incorrecta!<<--")
    pass_admin = str(input("Ingrese contraseña: "))



print("_______________________________________________")
print("              B I E N B E N I D O              ")
print()
money = float(2400)
list = [["andres felipe",0.4,100.000],["gabriel duran",0.6,34353.000],["jose luis",0.0,10.000]]

names = str(input("Ingrese el nombre del empleado: "))
while names == "":
    print()
    print("¡Ingrese un nombre de empleado!")
    names = str(input("Ingrese el nombre del empleado: "))
print()
print("""
    Niveles        Puntuacion
    -------------------------
    Inaceptable    0.0
    Aceptable      0.4
    Meritorio      0.6 o mas
    -------------------------
      """)



points = float(input("""Ingrese la puntuarion respectiva para el
empleado {}
: """.format(names.upper())))
print()
print("""    Se ha establecido la puntuacion del empleado {}
en {}""".format(names.upper(),points))
print()

money_total = points*money

salary = str(input("El salario actual es de {}, ¿desea cambiarlo?    Y/N".format(money)))
if salary == "Y" or salary == "y":
    money = float(input("Ingrese el valor del nuevo salario: "))
    money_total = points*money
    list.append([names,points,money_total])
    print("El salario actual es de {}".format(money))

    while money < 0:
        print("Ingrese un valor valido")
        money = float(input("Ingrese el valor del nuevo salario: "))
        money_total = points*money

elif salary == "N" or salary == "n":
    print("No se realizaron cambios en el salario")
else:
    print("No se realizaron cambios en el salario")

money_total = points*money
list.append([names,points,money_total])




x = len(list)-1
print()
print("_______________________________________________")
print("      L I S T A   D E   E M P L E A D O S      ")
print("""
    Empleado       Puntuacion       Salario    """)

for x in list:
    y=x
    z=x
    print("{}   {}     {}".format(x[0],y[1],z[2]))
print("_______________________________________________")






input("...")