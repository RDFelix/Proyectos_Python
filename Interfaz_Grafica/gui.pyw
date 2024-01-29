from tkinter import *
raiz = Tk()


#Indica el titulo de la ventana
raiz.title("Interfaz Grafica")

#Inidica que el ancho puede ser modificado pero el alto no
raiz.resizable(True,False)# Width,Heigth

#Indica el icono de la ventana
raiz.iconbitmap("image\icono_ventana.ico")

#Indica el tamaño de la ventana al iniciar
raiz.geometry("800x500")# Width,Heigth

#Indica los parametros de configuracion de la ventana: 
#Indica el fondo de la ventana
raiz.config(bg="#3498DB")


barra = Frame()
barra.pack(fill="x")
#Configura el frame
barra.config(height=50, bg="#8E44AD")

#Crea un frame o elemento widget
bt_color = Frame()
bt_color.pack(side="left", anchor="n")
#Configura el frame
bt_color.config(width="200", height="100",#Tamaño del frame
                bg="#28B463",#Color de fondo del frame
                bd="5",relief="solid",#Tamaño del borde y el tipo de borde
                cursor="hand2",#Cambia al cursor al sobreponerse al frame
                )

      


#Repite, Actualiza, Mantiene abierta la ventana, siempre en ejecucion
raiz.mainloop()