import numpy as np  

# Función para calcular la cinemática inversa de un robot de 2DOF
def cinemática_inversa(x, y, L1, L2):
    # Calcula la distancia desde el origen al punto objetivo utilizando el teorema de Pitágoras
    distancia = np.sqrt(x**2 + y**2)
    
    # Calcula el ángulo entre el segmento L1 y la línea que conecta el origen con el punto objetivo
    beta = np.arccos((L1**2 + distancia**2 - L2**2) / (2 * L1 * distancia))
    
    # Calcula el ángulo entre el segmento L2 y la línea que conecta el punto objetivo con el segmento L1
    gamma = np.arctan2(y, x)  # Usamos la función arctan2 para manejar todos los cuadrantes
    
    # Calcula el ángulo de la articulación 1 restando beta de gamma
    theta1 = gamma - beta
    
    # Calcula el ángulo de la articulación 2 utilizando la ley de los cosenos
    theta2 = np.arccos((L1**2 + L2**2 - distancia**2) / (2 * L1 * L2))
    
    return np.degrees(theta1), np.degrees(theta2)  # Convierte los ángulos a grados y los devuelve

# Dimensiones del robot (longitudes de los eslabones)
L1 = 5  # Longitud del primer eslabón
L2 = 4  # Longitud del segundo eslabón

# Nuevas longitudes de los eslabones
L1_nuevo = 10  
L2_nuevo = 7  

# Posición objetivo en el espacio cartesiano
x_objetivo = 2
y_objetivo = 3

# Nueva posición objetivo
x_nuevo_objetivo = 3
y_nuevo_objetivo = 6

# Calcula los ángulos de las articulaciones necesarios para alcanzar la posición objetivo original
theta1, theta2 = cinemática_inversa(x_objetivo, y_objetivo, L1, L2)

# Imprime los ángulos calculados para la posición objetivo original
print("Ángulo de la articulación 1 para la posición objetivo original:", theta1, "grados")
print("Ángulo de la articulación 2 para la posición objetivo original:", theta2, "grados")

# Calcula los ángulos de las articulaciones necesarios para alcanzar la nueva posición objetivo
theta1_nuevo, theta2_nuevo = cinemática_inversa(x_nuevo_objetivo, y_nuevo_objetivo, L1_nuevo, L2_nuevo)

# Imprime los ángulos calculados para la nueva posición objetivo
print("Ángulo de la articulación 1 para la nueva posición objetivo:", theta1_nuevo, "grados")
print("Ángulo de la articulación 2 para la nueva posición objetivo:", theta2_nuevo, "grados")