from utils import *

flota = [
    (4, 1),  # 1 barco de eslora 4
    (3, 2),  # 2 barcos de eslora 3
    (2, 3),  # 3 barcos de eslora 2
]

# Flujo inicial del programa
print("¡Bienvenido a Hundir la Flota Capitán!")
nombre_jugador = input("Por favor, ingrese su nombre: ")
print(f"¡Hola, {nombre_jugador}! Preparando los tableros...")

# Crear tableros
tablero_jugador = Tablero()  # Visible para el jugador
tablero_computadora = Tablero()  # No visible para el jugador

# Colocar barcos aleatorios en ambos tableros
tablero_jugador = colocar_flota_aleatoria(tablero_jugador, flota)
tablero_computadora = colocar_flota_aleatoria(tablero_computadora, flota)

# Mostrar solo el tablero del jugador
print(f"\nTu tablero, {nombre_jugador}:")
tablero_jugador.mostrar_tablero()

# Juego con turnos
print(f"\n¡Comienza el juego, {nombre_jugador}! Tu turno primero.")
max_turnos = 10  # Límite de turnos para probar (ajústalo si quieres)
turno = 0

while turno < max_turnos:
    # Turno del jugador
    try:
        print("\nIngresa las coordenadas para disparar (fila columna, ej: 0 0) o 'salir' para terminar:")
        entrada = input().strip().lower()
        if entrada == 'salir':
            break
        fila, columna = map(int, entrada.split())
        tablero_jugador.disparar((fila, columna), tablero_computadora)
        print(f"\nTableros tras tu turno, {nombre_jugador}:")
        tablero_jugador.mostrar_tablero()
    except (ValueError, IndexError):
        print("Entrada inválida. Usa dos números entre 0 y 9 separados por un espacio (ej: 0 0).")
        continue

    # Turno de la computadora
    print("\nTurno de la computadora:")
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
    tablero_jugador.recibir_disparo((fila, columna))
    print(f"La computadora disparó a ({fila}, {columna})")
    print(f"\nTableros tras el turno de la computadora, {nombre_jugador}:")
    tablero_jugador.mostrar_tablero()
    
    turno += 1

# Calcular y mostrar el ganador
calcular_ganador(tablero_jugador, tablero_computadora)