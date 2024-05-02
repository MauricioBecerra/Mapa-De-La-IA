import random  # Importa la biblioteca random para generar números aleatorios
import math    # Importa la biblioteca math para realizar operaciones matemáticas

def estimar_pi_muestreo_directo(num_puntos):
    puntos_dentro_semicirculo = 0  # Inicializa el contador de puntos dentro del semicírculo
    for _ in range(num_puntos):  # Itera num_puntos veces
        x = random.uniform(-1, 1)  # Genera una coordenada x aleatoria en el rango [-1, 1)
        y = random.uniform(0, 1)   # Genera una coordenada y aleatoria en el rango [0, 1)
        distancia_al_centro = math.sqrt(x**2 + y**2)  # Calcula la distancia al centro del punto generado
        if distancia_al_centro <= 1:  # Si la distancia es menor o igual a 1, el punto está dentro del semicírculo
            puntos_dentro_semicirculo += 1  # Incrementa el contador de puntos dentro del semicírculo
    return 2 * puntos_dentro_semicirculo / num_puntos  # Devuelve la estimación de pi

def estimar_pi_muestreo_por_rechazo(num_puntos):
    puntos_dentro_semicirculo = 0  # Inicializa el contador de puntos dentro del semicírculo
    puntos_totales = 0  # Inicializa el contador de puntos totales generados
    while puntos_totales < num_puntos:  # Repite el proceso hasta generar num_puntos puntos
        x = random.uniform(-1, 1)  # Genera una coordenada x aleatoria en el rango [-1, 1)
        y = random.uniform(0, 1)   # Genera una coordenada y aleatoria en el rango [0, 1)
        distancia_al_centro = math.sqrt(x**2 + y**2)  # Calcula la distancia al centro del punto generado
        if distancia_al_centro <= 1:  # Si la distancia es menor o igual a 1, el punto está dentro del semicírculo
            puntos_dentro_semicirculo += 1  # Incrementa el contador de puntos dentro del semicírculo
        puntos_totales += 1  # Incrementa el contador de puntos totales generados
    return 2 * puntos_dentro_semicirculo / puntos_totales  # Devuelve la estimación de pi

num_puntos = 50000  # Número de puntos para la estimación de pi

pi_estimado_directo = estimar_pi_muestreo_directo(num_puntos)  # Estimación de pi utilizando muestreo directo
print("Estimación de pi utilizando muestreo directo:", pi_estimado_directo)

pi_estimado_rechazo = estimar_pi_muestreo_por_rechazo(num_puntos)  # Estimación de pi utilizando muestreo por rechazo
print("Estimación de pi utilizando muestreo por rechazo:", pi_estimado_rechazo)
