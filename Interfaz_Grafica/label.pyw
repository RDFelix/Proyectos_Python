from tkinter import *

root = Tk()
root.config(bg="#3498DB")


miFrame = Frame(root, width=402, height=293)

miFrame.pack()

miImagen = PhotoImage(file="image/image1.gif")

Label(miFrame, image=miImagen).place(x=100, y=200)


miFrame1 = Frame(root, width=402, height=293)

miFrame1.pack()

Label(miFrame1, text="Hello World", fg="blue", font=("Calibri", 20)).place(x=100, y=200)

root.mainloop()