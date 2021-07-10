from tkinter import * #libreria de python de librerias


def inicial(api):

    ventana = Tk() #creacion de la ventana

    #Parametros iniciales:
    ventana.title("Shrek 2 Tweet Bot") #titulo

    ventana.resizable(1, 1) #que no se pueda redimensionar la ventana, metodo width-height

    ventana.iconbitmap("Shrekicon.ico") #esto sería para cambiar el icono, se necesita el .ico en el directorio

    ventana.geometry("650x650")

    ventana.config(bg="green")

    # ahora crearemos un frame
    frame1 = Frame(background="red")
    #esto es lo mismo que poner en config esto frame1.config(bg="red", width="200", height="250")

    # ahora lo empaquetamos en la ventana, queremos que quede con x mm de separacion del borde y que cubra todo
    frame1.pack(fill="both", expand=True, padx=40, pady=40)

    frame2 = Frame(width=100, height=100, background="blue") #este frame lo meteremos dentro del primero

    frame2.place(in_=frame1, anchor="c", relx=.5, rely=.5)

    ventana.mainloop() #para que la ventana se quede esuchando eventos debe estar en un bucle infinito

    return