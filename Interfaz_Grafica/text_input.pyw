from tkinter import *

raiz = Tk()
raiz.geometry("800x500")
raiz.config(bg="#3498DB")

frame1 = Frame(raiz, width=100, height=50)
frame1.pack(side="left", anchor="n")
frame1.config(bg="#3498DB")

mensaje = Text(frame1, width=40, height=10)
mensaje.grid(row=0, column=1, padx=5, pady=10)

scrollVert = Scrollbar(frame1, command=mensaje.yview)
scrollVert.grid(row=0, column=2, sticky="nsw", pady=10)
mensaje.config(yscrollcommand=scrollVert.set)



apellido = Label(frame1, bg="#3498DB",text="Apellido: ", font=("Calibri", 14)).grid(row=0,column=0,sticky="w", padx=5, pady=10)

raiz.mainloop()