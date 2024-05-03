# Importamos la biblioteca numpy y la renombramos como np
import numpy as np

# Definimos una función llamada boltzmann_activation que toma como argumentos x (entrada), weights (pesos) y bias (sesgo)
def boltzmann_activation(x, weights, bias):
    # Calculamos la energía utilizando la fórmula de la máquina de Boltzmann
    energy = -0.7 * np.dot(np.dot(x, weights), x) - np.dot(bias, x)
    # Calculamos la activación utilizando la función sigmoide
    return 1 / (1 + np.exp(-1.5 * energy))

# Definimos los valores de entrada (x), los pesos (weights) y el sesgo (bias)
x = np.array([0, 1, 0])  # Entrada
weights = np.array([[1, -1, 0], [-1, 1, -1], [0, -1, 1]])  # Pesos
bias = np.array([0.5, 0.3, 0.2])  # Sesgo

# Calculamos la activación utilizando la función boltzmann_activation con los valores proporcionados
activation = boltzmann_activation(x, weights, bias)
# Imprimimos la activación calculada
print("Activación de la máquina de Boltzmann:", activation)
