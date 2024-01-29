import tkinter as tk


#-->VENTANA
wn = tk.Tk()
wn.geometry("600x400+735+300")
wn.resizable(0, 0)
wn.title("Programa")

#-->DEFINICIONES
def verde():
    etiqueta["text"] = "Verde"
    etiqueta["bg"] = "green"

def azul():
    etiqueta["text"] = "Azul"
    etiqueta["bg"] = "blue"

#-->BOTONES Y ETIQUETAS
boton1 = tk.Button(wn, text="Verde", command=verde, borderwidth=0, background="#ABB2B9",fg="black", height=10, width=10, font="Calibri", activebackground="#2C3E50")
boton1.pack(side=tk.RIGHT)
boton2 = tk.Button(wn, text="Azul", command=azul, borderwidth=0, background="#ABB2B9",fg="black", height=10, width=10, font="Calibri", activebackground="#2C3E50")
boton2.pack(side=tk.LEFT)
etiqueta = tk.Label(wn)
etiqueta.pack()

#-->LOOP
wn.mainloop()