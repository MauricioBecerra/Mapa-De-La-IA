import numpy as np  # Importa la librería numpy para cálculos numéricos

def probabilidad_condicionada(evento_a, evento_b):
    """
    Calcula la probabilidad condicionada P(A|B) dada P(A∩B) y P(B).
    """
    return evento_a / evento_b

def normalizar(datos):
    """
    Normaliza un conjunto de datos para que tengan media 0 y desviación estándar 1.
    """
    media = np.mean(datos)  # Calcula la media de los datos
    desviacion_estandar = np.std(datos)  # Calcula la desviación estándar de los datos
    datos_normalizados = (datos - media) / desviacion_estandar  # Normaliza los datos
    return datos_normalizados

probabilidad_b = 0.6  # Define la probabilidad de B
probabilidad_a_interseccion_b = 0.3  # Define la probabilidad de la intersección de A y B

probabilidad_a_dado_b = probabilidad_condicionada(probabilidad_a_interseccion_b, probabilidad_b)  # Calcula P(A|B)
print("La probabilidad condicionada P(A|B) es:", probabilidad_a_dado_b)  # Imprime el resultado

datos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])  # Define un conjunto de datos
datos_normalizados = normalizar(datos)  # Normaliza los datos
print("Datos normalizados:", datos_normalizados)  # Imprime los datos normalizados
