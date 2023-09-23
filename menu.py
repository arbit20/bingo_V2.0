from tkinter import *
import tkinter as tk
from tkinter import ttk
from como_jugador import iniciar_jugador
from como_maestro import iniciar_maestro


def seleccionar():
    cadena = ""
    if opcion.get() == 1:
        cadena = "Iniciaras como maestro"

    if opcion.get() == 2:
        cadena = "Iniciaras como jugador"

    monitor.config(text=cadena)


def iniciar():
    if opcion.get() == 1:
        iniciar_maestro()
        print("Maestro")

    if opcion.get() == 2:
        iniciar_jugador()
        print("iniciando")


# Crear una instancia de la clase Tk
ventana = Tk()
ventana.title("BINGO")
ventana.geometry("500x500")
ventana.resizable(False, False)
mensaje_bienvenida = ttk.Label(ventana, text="¡BIENVENIDO AL JUEGO DE BINGO!")
# Cargar imagen del disco.
image = tk.PhotoImage(file="bingo.png")
# Insertarla en una etiqueta.
imagen = ttk.Label(image=image)
mensaje_opciones = ttk.Label(ventana, text="Escoge algunas de las opciones")

opcion = IntVar()  # 1 si, 0 no

seleccion_maestro = Radiobutton(
    ventana, text="Maestro", variable=opcion, value=1, command=seleccionar
)
seleccion_jugador = Radiobutton(
    ventana, text="Jugador", variable=opcion, value=2, command=seleccionar
)
boton_inicio = Button(ventana, text="Iniciar", command=iniciar)

mensaje_bienvenida.pack()
imagen.pack()
mensaje_opciones.pack()
seleccion_maestro.pack()
seleccion_jugador.pack()
monitor = Label(ventana)
monitor.pack()
boton_inicio.pack()

# Mostrar la ventana
ventana.mainloop()
