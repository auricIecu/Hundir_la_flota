from utils import *

# Flota estándar para el juego
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

# Limpiar para volver al estado inicial y mostrar solo el tablero del jugador
limpiar_consola()
print(f"Estado del juego, {nombre_jugador}:")
tablero_jugador.mostrar_tablero()
print("\n¡Comienza el juego! Tu turno primero.")
print("Ingresa las coordenadas para disparar (fila columna, ej: 0 0) o 'salir' para terminar:")

# Juego con turnos
max_turnos = 10
turno = 0
mensaje_jugador = ""
mensaje_computadora = ""

while turno < max_turnos:
    # Turno del jugador
    try:
        entrada = input().strip().lower()
        if entrada == 'salir':
            break
        fila, columna = map(int, entrada.split())
        mensaje_jugador = tablero_jugador.disparar((fila, columna), tablero_computadora)
    except (ValueError, IndexError):
        mensaje_jugador = "Entrada inválida. Usa dos números entre 0 y 9 separados por un espacio (ej: 0 0)."

    # Turno de la computadora
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
    mensaje_computadora = tablero_jugador.recibir_disparo((fila, columna))  # Corregido: dispara al tablero del jugador
    mensaje_computadora += f"\nLa computadora disparó a ({fila}, {columna})"

    # Actualizar pantalla
    limpiar_consola()
    print(f"Estado del juego, {nombre_jugador} (Turno {turno + 1}):")
    tablero_jugador.mostrar_tablero()
    print(f"\n{mensaje_jugador}")
    print(f"{mensaje_computadora}")
    print("\nIngresa las coordenadas para disparar (fila columna, ej: 0 0) o 'salir' para terminar:")
    
    turno += 1
    time.sleep(1)

# Calcular y mostrar el ganador
limpiar_consola()
print(f"Estado final del juego, {nombre_jugador}:")
tablero_jugador.mostrar_tablero()
calcular_ganador(tablero_jugador, tablero_computadora, nombre_jugador)  # Pasamos nombre_jugador