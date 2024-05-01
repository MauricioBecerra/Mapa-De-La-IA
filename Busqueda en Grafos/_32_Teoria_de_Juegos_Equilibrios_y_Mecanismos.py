
def juego_piedra_papel_tijeras(jugador1, jugador2):
    # Diccionario que contiene las reglas del juego, donde las claves son las combinaciones de jugadas y los valores son las recompensas para cada jugador
    reglas = {
        ("piedra", "papel"): (0, 1),       # Si el jugador 1 elige piedra y el jugador 2 elige papel, el jugador 2 gana
        ("piedra", "tijeras"): (1, 0),     # Si el jugador 1 elige piedra y el jugador 2 elige tijeras, el jugador 1 gana
        ("papel", "piedra"): (1, 0),       # Si el jugador 1 elige papel y el jugador 2 elige piedra, el jugador 1 gana
        ("papel", "tijeras"): (0, 1),      # Si el jugador 1 elige papel y el jugador 2 elige tijeras, el jugador 2 gana
        ("tijeras", "piedra"): (0, 1),     # Si el jugador 1 elige tijeras y el jugador 2 elige piedra, el jugador 2 gana
        ("tijeras", "papel"): (1, 0)       # Si el jugador 1 elige tijeras y el jugador 2 elige papel, el jugador 1 gana
    }
    # Se obtienen las recompensas para las jugadas dadas
    resultado_jugador1, resultado_jugador2 = reglas[(jugador1, jugador2)]
    return resultado_jugador1, resultado_jugador2

def main():
    # Mensaje de bienvenida al juego
    print("Bienvenido al juego de Piedra, Papel o Tijeras.")
    # Solicitar la jugada del jugador 1
    print("Jugador 1, ¿piedra (r), papel (p) o tijeras (t)?")
    eleccion_jugador1 = input().strip().lower()
    # Solicitar la jugada del jugador 2
    print("Jugador 2, ¿piedra (r), papel (p) o tijeras (t)?")
    eleccion_jugador2 = input().strip().lower()

    # Verificar si las jugadas son válidas
    if eleccion_jugador1 not in ["r", "p", "t"] or eleccion_jugador2 not in ["r", "p", "t"]:
        print("Por favor, introduce 'r' para piedra, 'p' para papel o 't' para tijeras.")
        return

    # Convertir las jugadas a texto para mejor legibilidad
    if eleccion_jugador1 == "r":
        eleccion_jugador1_texto = "piedra"
    elif eleccion_jugador1 == "p":
        eleccion_jugador1_texto = "papel"
    else:
        eleccion_jugador1_texto = "tijeras"

    if eleccion_jugador2 == "r":
        eleccion_jugador2_texto = "piedra"
    elif eleccion_jugador2 == "p":
        eleccion_jugador2_texto = "papel"
    else:
        eleccion_jugador2_texto = "tijeras"

    # Se ejecuta la función que simula el juego y se obtienen las recompensas
    resultado_jugador1, resultado_jugador2 = juego_piedra_papel_tijeras(eleccion_jugador1_texto, eleccion_jugador2_texto)
    # Se muestra el resultado del juego
    if resultado_jugador1 == resultado_jugador2:
        print("¡Empate!")
    elif resultado_jugador1 > resultado_jugador2:
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")

if __name__ == "__main__":
    main()
