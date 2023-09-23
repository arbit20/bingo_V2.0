import tkinter
import tkinter as tk
from tkinter import *
from numeros_aleatorios import elegir_azar




def iniciar_maestro():
    def mostrar_numero():
        a.set(elegir_azar())
    ventana_secundaria = tkinter.Toplevel()
    ventana_secundaria.title("BINGO (Mestro)")
    ventana_secundaria.geometry("100x400")
    ventana_secundaria.resizable(False, False)
    a = StringVar()
    Label(ventana_secundaria, textvariable=a).pack()
    boton = tk.Button(ventana_secundaria, text="Generar numero", command=mostrar_numero)
    boton.pack()
    ventana_secundaria.mainloop()
