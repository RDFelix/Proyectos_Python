from tkinter import *

raiz = Tk()
raiz.geometry("800x500")
raiz.config(bg="pink")


n = "14"


def sumar(numero):
    n += numero



bt_suma = Button(raiz)
bt_suma.config(width=10, height=10, text= "push", fg="grey", font=("Arial", 20), conmand=sumar("1"))
bt_suma.pack()

label = Label(raiz)
label.config(text=str(n))
label.pack()


raiz.mainloop()