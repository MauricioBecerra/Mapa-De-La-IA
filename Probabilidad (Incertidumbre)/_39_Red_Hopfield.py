import numpy as np

# Definición de la función de activación de la red de Hopfield
def hopfield_activation(x, weights):
    return np.sign(np.dot(weights, x))

# Nuevos datos de entrada y pesos
x_new = np.array([-1, 1, -1])  # Nuevos datos de entrada
weights_new = np.array([[1, 0, -1],   # Nuevos pesos de la red
                        [0, -1, 1],
                        [-1, 1, 0]])

# Calcula la activación de la red de Hopfield con los nuevos datos
activation_new = hopfield_activation(x_new, weights_new)

# Imprime la activación resultante
print("Activación de la red de Hopfield (nuevos datos):", activation_new)
