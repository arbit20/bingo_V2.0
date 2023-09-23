from numeros_aleatorios import elegir_azar


def devolver_25():
    elegidos = []
    for num in range(0, 25):
        elegido = elegir_azar()
        elegidos.append(elegido)
    return elegidos
