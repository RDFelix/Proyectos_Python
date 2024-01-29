from tkinter import *

raiz = Tk()
raiz.resizable(False,False)
raiz.config(bg="#5D6D7E")

frame1 = Frame(raiz)
frame1.pack()
frame1.config(bg="#5D6D7E")

#------->TAMAÑOS-------
size_font = 12
size_width = 5
#----------------------



#------->Variables------
numbers_display = StringVar()

#----------------------


#----------------->>>Pantalla
display = Entry(frame1, textvariable=numbers_display)
display.grid(row=1, column=1, columnspan=4)
display.config(bg="#5D6D7E", fg="white", font=(size_font),justify="right")

def agregar_valor(numero):
    
    numbers_display.set(numbers_display.get() + str(numero))



#----------------->>>FILA 1
button_7 = Button(frame1, text="7", width=str(size_width), font=(size_font), command=lambda:agregar_valor(7)).grid(row=2, column=1)
button_8 = Button(frame1, text="8", width=str(size_width), font=(size_font), command=lambda:agregar_valor(8)).grid(row=2, column=2)
button_9 = Button(frame1, text="9", width=str(size_width), font=(size_font), command=lambda:agregar_valor(9)).grid(row=2, column=3)
button_div = Button(frame1, text="/", width=str(size_width), font=(size_font)).grid(row=2, column=4)


#----------------->>>FILA 2
button_4 = Button(frame1, text="4", width=str(size_width), font=(size_font), command=lambda:agregar_valor(4)).grid(row=3, column=1)
button_5 = Button(frame1, text="5", width=str(size_width), font=(size_font), command=lambda:agregar_valor(5)).grid(row=3, column=2)
button_6 = Button(frame1, text="6", width=str(size_width), font=(size_font), command=lambda:agregar_valor(6)).grid(row=3, column=3)
button_mult = Button(frame1, text="x", width=str(size_width), font=(size_font)).grid(row=3, column=4)


#----------------->>>FILA 3
button_1 = Button(frame1, text="1", width=str(size_width), font=(size_font), command=lambda:agregar_valor(1)).grid(row=4, column=1)
button_2 = Button(frame1, text="2", width=str(size_width), font=(size_font), command=lambda:agregar_valor(2)).grid(row=4, column=2)
button_3 = Button(frame1, text="3", width=str(size_width), font=(size_font), command=lambda:agregar_valor(3)).grid(row=4, column=3)
button_rest = Button(frame1, text="-", width=str(size_width), font=(size_font)).grid(row=4, column=4)


#----------------->>>FILA 4
button_0 = Button(frame1, text="0", width=str(size_width), font=(size_font), command=lambda:agregar_valor(0)).grid(row=5, column=1)
button_coma = Button(frame1, text=",", width=str(size_width), font=(size_font), command=lambda:agregar_valor(",")).grid(row=5, column=2)
button_igual = Button(frame1, text="=", width=str(size_width), font=(size_font)).grid(row=5, column=3)
button_suma = Button(frame1, text="+", width=str(size_width), font=(size_font), command=lambda:agregar_valor("+")).grid(row=5, column=4)


raiz.mainloop()