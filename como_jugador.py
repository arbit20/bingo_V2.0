import tkinter as tk
from numeros_carton import devolver_25


def iniciar_jugador():
    # Definir una lista de valores
    valores = devolver_25()
    diccionario = {}
    # Recorrer la lista de valores y agregarlos al diccionario
    for i, valor in enumerate(valores):
        clave = "clave" + str(i + 1)
        diccionario[clave] = valor
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("BINGO")
    ventana_secundaria.geometry("500x400")
    ventana_secundaria.resizable(False, False)
    casilla_n1 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave1"]
    )
    casilla_n1.grid(padx=40, pady=20, row=1, column=1)
    casilla_n2 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave2"]
    )
    casilla_n2.grid(padx=20, pady=20, row=2, column=1)
    casilla_n3 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave3"]
    )
    casilla_n3.grid(padx=20, pady=20, row=3, column=1)
    casilla_n4 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave4"]
    )
    casilla_n4.grid(padx=20, pady=20, row=4, column=1)
    casilla_n5 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave5"]
    )
    casilla_n5.grid(padx=20, pady=20, row=5, column=1)

    casilla_n6 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave6"]
    )
    casilla_n6.grid(padx=40, pady=20, row=1, column=2)
    casilla_n7 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave7"]
    )
    casilla_n7.grid(padx=20, pady=20, row=2, column=2)
    casilla_n8 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave8"]
    )
    casilla_n8.grid(padx=20, pady=20, row=3, column=2)
    casilla_n9 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave9"]
    )
    casilla_n9.grid(padx=20, pady=20, row=4, column=2)
    casilla_n10 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave10"]
    )
    casilla_n10.grid(padx=20, pady=20, row=5, column=2)

    casilla_n11 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave11"]
    )
    casilla_n11.grid(padx=40, pady=20, row=1, column=3)
    casilla_n12 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave12"]
    )
    casilla_n12.grid(padx=20, pady=20, row=2, column=3)
    casilla_n13 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave13"]
    )
    casilla_n13.grid(padx=20, pady=20, row=3, column=3)
    casilla_n14 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave14"]
    )
    casilla_n14.grid(padx=20, pady=20, row=4, column=3)
    casilla_n15 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave15"]
    )
    casilla_n15.grid(padx=20, pady=20, row=5, column=3)

    casilla_n16 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave16"]
    )
    casilla_n16.grid(padx=40, pady=20, row=1, column=4)
    casilla_n17 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave17"]
    )
    casilla_n17.grid(padx=20, pady=20, row=2, column=4)
    casilla_n18 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave18"]
    )
    casilla_n18.grid(padx=20, pady=20, row=3, column=4)
    casilla_n19 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave19"]
    )
    casilla_n19.grid(padx=20, pady=20, row=4, column=4)
    casilla_n20 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave20"]
    )
    casilla_n20.grid(padx=20, pady=20, row=5, column=4)

    casilla_n21 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave21"]
    )
    casilla_n21.grid(padx=40, pady=20, row=1, column=5)
    casilla_n22 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave22"]
    )
    casilla_n22.grid(padx=20, pady=20, row=2, column=5)
    casilla_n23 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave23"]
    )
    casilla_n23.grid(padx=20, pady=20, row=3, column=5)
    casilla_n24 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave24"]
    )
    casilla_n24.grid(padx=20, pady=20, row=4, column=5)
    casilla_n25 = tk.Checkbutton(
        ventana_secundaria, text=diccionario["clave25"]
    )
    casilla_n25.grid(padx=20, pady=20, row=5, column=5)
    tk.Button(
        ventana_secundaria,
        text="BINGO",
        activebackground="black",
        activeforeground="white"
    ).grid(row=8, column=2, columnspan=2)
    ventana_secundaria.mainloop()
