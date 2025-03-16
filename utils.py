import numpy as np
import random
import os
import time

"""
CLASE TABLERO
"""

#Creamos la clase tablero, con un parametro fijo de tamano (10, 10) y le agregamos un metodo crear_tablero

class Tablero:
    def __init__(self, tamano=(10, 10)):
        self.tamano = tamano
        self.grid = np.full(tamano, '_')
        self.tablero_disparos = np.full(tamano, '_')  # Agregamos un tablero de disparos contra el enemigo
        self.disparos_realizados = []  # Lista para almacenar las casillas disparadas
        self.disparos_recibidos = []   # Nueva lista para disparos recibidos

    def mostrar_tablero(self):
        print("Sus barcos capitán: ")
        print(self.grid)
        print("\nTu tablero de disparos contra su enemigo: ")
        print(self.tablero_disparos)

    def recibir_disparo(self, casilla):
        #Proceso disparos recibidos (usado por la computadora contra el jugador)
        fila, columna = casilla
        if fila >= self.tamano[0] or columna >= self.tamano[1]:
            return "Disparo fuera del tablero" # Se devuelve la respuesta como una cadena anidada, asi se muestran abajo del tablero
        if casilla in self.disparos_recibidos:  # Cambié a disparos_recibidos
            return "La computadora ya disparó aquí"
        self.disparos_realizados.append(casilla)
        if self.grid[fila, columna] == 'O':
            self.grid[fila, columna] = 'X'
            return "¡La computadora ha acertado y comprometido una de tus flotas!"
        elif self.grid[fila, columna] == '_':
            self.grid[fila, columna] = 'A'
            return "La computadora ha fallado"
        return ""
    
    def disparar(self, casilla, tablero_enemigo):
        """
        Registra el disparo del jugador en el tablero de disparos 
        y actualiza el tablero enemigo
        """
        fila, columna = casilla
        if casilla in self.disparos_realizados:
            return "Ya disparaste aquí"
        self.disparos_realizados.append(casilla) # Si llega hasta aqui es porque la casilla no esta en el conjunto de las previas
        if tablero_enemigo.grid[fila, columna] == 'O':
            self.tablero_disparos[fila, columna] = 'X'
            tablero_enemigo.grid[fila, columna] = 'X'  # Actualiza el tablero enemigo
            return "¡Acertaste!"
        else:
            self.tablero_disparos[fila, columna] = 'A'
            tablero_enemigo.grid[fila, columna] = 'A'
            return "Has fallado al enemigo"
        return ""
    
"""
CLASE BARCO
"""

class Barco:
    def __init__(self, posiciones):
        self.posiciones = posiciones

    def colocar_barco(self, tablero):
        for fila, columna in self.posiciones:
        # Eliminamos el if, y dejamos solo la colocacion del barco, asumiendo que las posiciones ya son validas
            tablero.grid[fila, columna] = 'O'
        return tablero
    
    @staticmethod
    def crear_barco_aleatorio(eslora, tablero):
        while True:
            orientacion = random.choice(["Horizontal", "Vertical"])
            if orientacion == "Horizontal":
                fila = random.randint(0, tablero.tamano[0] - 1)
                columna_inicial = random.randint(0, tablero.tamano[1] - eslora)
            else:
                fila_inicial = random.randint(0, tablero.tamano[0] - eslora)
                columna = random.randint(0, tablero.tamano[1] - 1)

            barco_aleatorio = []
            for i in range(eslora):
                if orientacion == "Horizontal":
                    casilla = (fila, columna_inicial + i)
                else:
                    casilla = (fila_inicial + i, columna)
                
                # Verificar antes de añadir
                fila_casilla, columna_casilla = casilla
                if tablero.grid[fila_casilla, columna_casilla] != '_':
                    break  # Si está ocupada, salimos del for y probamos otra vez
                barco_aleatorio.append(casilla)
            else:  # Se ejecuta si el for termina sin break
                return barco_aleatorio  # Todas las posiciones estaban libres
                        
"""
FUNCIONES INDEPENDIENTES
"""

def colocar_flota_aleatoria(tablero, flota):
    for eslora, cantidad in flota:
        for i in range(cantidad):
            barco = Barco(Barco.crear_barco_aleatorio(eslora, tablero))
            tablero = barco.colocar_barco(tablero)
    return tablero

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_ganador(tablero_jugador, tablero_computadora, nombre_jugador):
    """Calcula los porcentajes de aciertos y determina el ganador"""
    # Aciertos del jugador (contar 'X' en el tablero de la computadora)
    aciertos_jugador = np.sum(tablero_computadora.grid == 'X')
    disparos_jugador = len(tablero_jugador.disparos_realizados)
    porcentaje_jugador = (aciertos_jugador / disparos_jugador * 100) if disparos_jugador > 0 else 0

    # Aciertos de la computadora (contar 'X' en el tablero del jugador)
    aciertos_computadora = np.sum(tablero_jugador.grid == 'X')
    disparos_computadora = len(tablero_jugador.disparos_recibidos)
    porcentaje_computadora = (aciertos_computadora / disparos_computadora * 100) if disparos_computadora > 0 else 0

    print(f"\nEstadísticas finales:")
    print(f"Jugador - Aciertos: {aciertos_jugador}/{disparos_jugador} ({porcentaje_jugador:.2f}%)")
    print(f"Computadora - Aciertos: {aciertos_computadora}/{disparos_computadora} ({porcentaje_computadora:.2f}%)")

    if porcentaje_jugador > porcentaje_computadora:
        print(f"¡Ganaste, {nombre_jugador}! Tu precisión fue mayor.")
    elif porcentaje_computadora > porcentaje_jugador:
        print("La computadora gana. Su precisión fue mayor.")
    else:
        print("¡Empate! Ambos tuvieron la misma precisión.")