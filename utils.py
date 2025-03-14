import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, '_')

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Acertaste")
        tablero[casilla] = "X"
    else:
        print("Fallaste")
        tablero[casilla]  = "A"
    return tablero

def crear_barco_aleatorio(eslora):
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    barco_aleatorio = [(fila, columna)]

    orientacion = random.choice(["Horizontal", "Vertical"])
    while len(barco_aleatorio) < eslora:
        if orientacion == "Horizontal":
            columna = columna + 1
            barco_aleatorio.append((fila, columna))
        else:
            fila = fila + 1
            barco_aleatorio.append((fila, columna))
    return barco_aleatorio
