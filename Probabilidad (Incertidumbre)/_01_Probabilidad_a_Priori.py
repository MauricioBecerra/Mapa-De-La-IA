def probabilidad_a_priori(evento, espacio_muestral):
    # Calcula la probabilidad a priori de un evento dado el espacio muestral.
    conteo_evento = sum(1 for e in espacio_muestral if e in evento)  # Cuenta cuántos elementos del evento están en el espacio muestral
    return conteo_evento / len(espacio_muestral)  # Retorna la probabilidad dividiendo el conteo entre el tamaño del espacio muestral

def main():
    espacio_muestral = list(range(1, 21))  # Espacio muestral del 1 al 20
    evento_impar = [n for n in espacio_muestral if n % 2 != 0]  # Lista de números impares del 1 al 20
    p_a_priori_impar = probabilidad_a_priori(evento_impar, espacio_muestral)  # Calcula la probabilidad a priori de obtener un número impar
    print("Probabilidad a priori de obtener un número impar:", p_a_priori_impar)  # Imprime el resultado

if __name__ == "__main__":
    main()
