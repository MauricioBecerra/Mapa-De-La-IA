import numpy as np  # Importa la librería NumPy

# Definición de las recompensas (R)
R = np.array([
    [-1, -3],  # Estado 0: Acción 0 -> Recompensa -1, Acción 1 -> Recompensa -3
    [-2, 10]   # Estado 1: Acción 0 -> Recompensa -2, Acción 1 -> Recompensa 10
])

# Definición de las probabilidades de transición (T)
T = np.array([
    [[1, 0], [0, 1]],  # Desde el estado 0, Acción 0: 100% de probabilidad de permanecer en el estado 0
                       # Desde el estado 0, Acción 1: 100% de probabilidad de pasar al estado 1
    [[1, 0], [0, 1]]   # Desde el estado 1, Acción 0: 100% de probabilidad de permanecer en el estado 1
                       # Desde el estado 1, Acción 1: 100% de probabilidad de permanecer en el estado 1
])

# Definición de la política inicial
politica = np.ones((2, 2)) / 2  # Igual probabilidad para cada acción en cada estado

def evaluacion_politica(politica, R, T, gamma=0.9, theta=0.0001):
    """
    Evalúa la política para calcular los valores de los estados.

    Args:
        politica (numpy.array): Matriz de política.
        R (numpy.array): Matriz de recompensas.
        T (numpy.array): Matriz de probabilidades de transición.
        gamma (float): Factor de descuento.
        theta (float): Umbral de convergencia.

    Returns:
        numpy.array: Valores de los estados.
    """
    V = np.zeros(len(R))  # Inicializa los valores de los estados a 0
    while True:  # Bucle hasta que se alcance la convergencia
        delta = 0  # Variable para rastrear el cambio máximo en los valores de los estados
        for s in range(len(R)):  # Itera sobre cada estado en el problema
            v = V[s]  # Almacena el valor actual del estado
            # Calcula el nuevo valor del estado utilizando la política y las recompensas
            V[s] = sum(politica[s, a] * sum(T[s, a, s1] * (R[s, a] + gamma * V[s1]) for s1 in range(len(R))) for a in range(len(politica[s])))
            # Actualiza el valor de cambio máximo
            delta = max(delta, abs(v - V[s]))
        if delta < theta:  # Comprueba si se ha alcanzado la convergencia
            break  # Si el cambio es lo suficientemente pequeño, se detiene la iteración
    return V  # Devuelve los valores de los estados calculados

# Ejecución de la evaluación de política para obtener los valores de los estados
valores = evaluacion_politica(politica, R, T)

print("Valores de los estados son: ")  # Imprime los valores de los estados
print(valores)  # Imprime los valores de los estados
