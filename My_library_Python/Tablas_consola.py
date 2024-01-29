#Elementos
nombres = [["felixxx","ruiz","52328673"],
           ["gabriel","duran","233"],
           ["h","po","2"]
          ]
titulos = ["Nombre", "Apellido","cobro"]


#Variables
n,a,b = len(titulos[0]), len(titulos[1]), len(titulos[2]) 
x,y,z = len(max(nombres[0])), len(max(nombres[1])), len(max(nombres[2]))
space_n,space_a,space_c = round(x/2)*2, round(y/2)*2, round(z/2)*2
t_n = titulos[0]
t_a = titulos[1]
t_c = titulos[2]
line_n,line_a,line_c= "═"*(x+2), "═"*(y+2), "═"*(z+2)
print(x,y,z)
print(max(nombres[1][0]))
print(max(nombres[1][1]))
print(max(nombres[1][2]))


#Agrega espacios
if space_n != x:#Primera columna
    titulos[0] = str((round(((x-n)+1)/2)*" ")+t_n+(round(((x-n)+1)/2)*" "))
else:
    titulos[0] = str((round(((x-n))/2)*" ")+t_n+(round(((x-n)+1)/2)*" "))
#----------------------------------------------------------------------------#
if space_a != y:#Segunda columna
    titulos[1] = str((round(((y-a)+1)/2)*" ")+t_a+(round(((y-a)+1)/2)*" "))
else:
    titulos[1] = str((round(((y-a))/2)*" ")+t_a+(round(((y-a)+1)/2)*" "))
#----------------------------------------------------------------------------#
if space_c != z:#Tercera columna
    titulos[2] = str((round(((z-b)+1)/2)*" ")+t_c+(round(((z-b)+1)/2)*" "))
else:
    titulos[2] = str((round(((z-b))/2)*" ")+t_c+(round(((z-b)+1)/2)*" "))

#Dibuja Tabla
print("""╔{}╦{}╦{}╗
║ {}║ {}║ {}║
╠{}╬{}╬{}╣""".format(line_n,line_a,line_c,titulos[0],titulos[1],titulos[2],line_n,line_a,line_c))

#Dibuja elementos de la tabla
for a in nombres:
    if x-len(a[0]) == 0:
        space_tb_n  = " "
    else:
        space_tb_n  = " "*round(x-len(a[0])+1)
    space_tb_a  = " "*((y-len(a[1])))
    space_tb_c  = " "*((z-len(a[1])))
    print("║ {}{}║ {}{} ║ {}{}║".format(a[0], space_tb_n, a[1], space_tb_a, a[2], space_tb_c))
print("╚{}╩{}╩{}╝".format(line_n,line_a,line_c))

input("...")