import numpy as np

# Definimos una función para detectar si una línea en una imagen es horizontal o vertical
def detectar_linea(imagen):
    altura, ancho = imagen.shape  # Obtenemos las dimensiones de la imagen (altura y ancho)

    # Calculamos la suma de los valores de píxeles a lo largo de las filas y columnas
    suma_filas = np.sum(imagen, axis=1)  # Suma de píxeles por fila
    suma_columnas = np.sum(imagen, axis=0)  # Suma de píxeles por columna

    # Comparamos las medias de las sumas de píxeles de filas y columnas para determinar si la línea es horizontal o vertical
    if np.mean(suma_filas) > np.mean(suma_columnas):
        return "horizontal"  # Si la media de las sumas de píxeles de filas es mayor, la línea es horizontal
    else:
        return "vertical"  # Si la media de las sumas de píxeles de columnas es mayor, la línea es vertical

# Definimos una nueva imagen de ejemplo que contiene una línea inclinada
imagen_inclinada = np.array([[0, 0, 1, 0, 0],  # Definimos la matriz de la imagen
                             [0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1],
                             [0, 0, 0, 1, 0]])

# Probamos la función con la nueva imagen
resultado_inclinado = detectar_linea(imagen_inclinada)

# Imprimimos el resultado de la detección de línea para la imagen inclinada
print("La línea en la imagen inclinada es:", resultado_inclinado)
