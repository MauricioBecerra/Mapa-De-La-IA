import numpy as np

# Definición de la función de activación de la red de Hamming
def hamming_activation(x, weights):
    return np.dot(x, weights)

# Datos de entrada y pesos
x = np.array([0, 1, 1])  # Nuevos valores de entrada
weights = np.array([[1, 0, 1],  # Nuevos valores de pesos
                    [0, 1, 0],
                    [1, 0, 1]])

# Calcula la activación de la red de Hamming
activation = hamming_activation(x, weights)
print("Activación de la red de Hamming:", activation)
