import numpy as np  # Importa la librería NumPy para operaciones numéricas
import time  # Importa el módulo time para la función de espera

def imprimir_cuadricula(cuadricula):
    """
    Función para imprimir la cuadrícula en la consola.
    Args:
        cuadricula (array): Matriz que representa la cuadrícula.
    """
    for fila in cuadricula:
        print(' '.join(fila))  # Imprime cada fila de la cuadrícula uniendo los elementos con un espacio

def simular_movimiento(cuadricula):
    """
    Función para simular el movimiento del objeto en la cuadrícula.
    Args:
        cuadricula (array): Matriz que representa la cuadrícula.
    Returns:
        array: Nueva cuadrícula con el movimiento simulado.
    """
    nueva_cuadricula = np.full_like(cuadricula, ' ')  # Crea una nueva cuadrícula llena de espacios en blanco
    
    # Itera sobre cada celda en la cuadrícula
    for i in range(len(cuadricula)):
        for j in range(len(cuadricula[0])):
            if cuadricula[i][j] == 'O':  # Si la celda contiene el objeto 'O'
                nueva_posicion = (i + 1, j)  # Calcula la nueva posición (movimiento hacia abajo)
                # Verifica si la nueva posición está dentro de la cuadrícula
                if 0 <= nueva_posicion[0] < len(cuadricula):
                    nueva_cuadricula[nueva_posicion] = 'O'  # Coloca el objeto en la nueva posición
    
    return nueva_cuadricula  # Devuelve la nueva cuadrícula con el movimiento simulado

filas = 8  # Número de filas en la cuadrícula (cambiado de 5 a 8 para una cuadrícula más grande)
columnas = 6  # Número de columnas en la cuadrícula (cambiado de 10 a 6 para una cuadrícula más pequeña)

# Crea una cuadrícula inicial llena de espacios en blanco
cuadricula = np.full((filas, columnas), ' ')
# Coloca un objeto 'O' en la posición (3, 2) de la cuadrícula
cuadricula[3][2] = 'O'

# Itera 4 veces para simular el movimiento del objeto en la cuadrícula (cambiado de 5 a 4 iteraciones)
for _ in range(4):
    imprimir_cuadricula(cuadricula)  # Imprime la cuadrícula actual en la consola
    print('-' * (columnas * 2))  # Imprime una línea divisoria
    cuadricula = simular_movimiento(cuadricula)  # Actualiza la cuadrícula con el movimiento simulado
    time.sleep(1)  # Espera 1 segundo antes de la siguiente iteración
