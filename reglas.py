def verificar_ganador(carton_ganador, numeros_anunciados):
    if len(carton_ganador) == 25:
        ganador = True
        for numero in carton_ganador:
            if numero not in numeros_anunciados:
                ganador = False
        if ganador:
            print("\nGANASTE")
        else:
            print("\nESTAFADOR")
    else:
        print("\nEL CARTÓN NO TIENE 25 NÚMEROS")
