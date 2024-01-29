from tkinter import *

raiz = Tk()
raiz.geometry("800x500")
raiz.config(bg="#3498DB")

nombres = StringVar()

def color():
    raiz.config(bg="green")

def nombre():
    nombres.set("Felix Gabriel")


input_nombre = Entry(raiz, textvariable=nombres)
input_nombre.pack()

button_color = Button(raiz, text="Azul", command=color)
button_color.pack()

button_nombre = Button(raiz, text="Mi nombre", command=nombre)
button_nombre.pack()

raiz.mainloop()