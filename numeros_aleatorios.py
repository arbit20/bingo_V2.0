import random
# Establcemos un rengo para los numeros aleatorio
lista = list(range(0, 101))


def elegir_azar():
    elegido = random.choice(lista)
    lista.remove(elegido)
    return elegido
