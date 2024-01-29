from tkinter import *

raiz = Tk()
raiz.geometry("800x500")
raiz.config(bg="#3498DB")

frame1 = Frame(raiz, width=100, height=50)
frame1.pack(side="left", anchor="n")
frame1.config(bg="#3498DB")

titulo = Label(frame1, bg="#3498DB",text="DATOS DE USUARIO", font=("Calibri", 14)).grid(row=0,column=0, sticky="s")

input_nombre = Entry(frame1)
input_nombre.grid(row=1, column=1)#Row:Fila - Column: Columna    -  Comienza desde row y column 0, es decir, 0,0
nombre = Label(frame1, bg="#3498DB",text="Nombre: ", font=("Calibri", 14)).grid(row=1,column=0,sticky="w", padx=5, pady=10)

input_apellido = Entry(frame1)
input_apellido.grid(row=2, column=1)#Row:Fila - Column: Columna    -  Comienza desde row y column 0, es decir, 0,0
apellido = Label(frame1, bg="#3498DB",text="Apellido: ", font=("Calibri", 14)).grid(row=2,column=0,sticky="w", padx=5, pady=10)
raiz.mainloop()