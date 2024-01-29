nombre = str(input("Ingrese sus nombres: "))
renta = int(input("¿De cuanto es su declaracion de renta anual?"))
if nombre == "":
    print("-->>!Ingrese un nombre!<<--")
if renta == "" or renta == 0:
    print("-->>!Ingrese una cantidad valida!<<--")



if renta < 10000:
    print("Su impositivo de renta corresponde al 5%")
elif renta >= 10000 and renta < 20000:
    print("Su impositivo de renta corresponde al 15%")
elif renta >= 20000 and renta < 35000:
    print("Su impositivo de renta corresponde al 20%")
elif renta >= 35000 and renta < 60000:
    print("Su impositivo de renta corresponde al 30%")
elif renta >= 60000:
    print("Su impositivo de renta corresponde al 45%")

input("...")