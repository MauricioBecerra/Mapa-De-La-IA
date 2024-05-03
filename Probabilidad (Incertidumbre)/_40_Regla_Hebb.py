import numpy as np

# Función para la regla de Hebb
def hebb_rule(x):
    return np.outer(x, x)

# Nuevos datos de entrada
y1 = np.array([0, 1, 0])
y2 = np.array([1, 0, 1])

# Calcula los pesos utilizando la regla de Hebb
new_weights = hebb_rule(y1) + hebb_rule(y2)
print("Pesos ajustados con la regla de Hebb:\n", new_weights)
