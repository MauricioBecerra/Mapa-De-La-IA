import numpy as np

# Función de predicción del filtro de Kalman extendido (EKF)
def prediccion(x, P, F, Q):
    # Predicción del nuevo estado utilizando la matriz de transición de estado F
    x_prediccion = np.dot(F, x)
    # Predicción de la nueva covarianza del estado
    P_prediccion = np.dot(F, np.dot(P, F.T)) + Q
    return x_prediccion, P_prediccion

# Función de actualización del filtro de Kalman extendido (EKF)
def actualización(x_prediccion, P_prediccion, z, H, R):
    # Calcula la innovación entre la medición y la predicción
    y = z - np.dot(H, x_prediccion)
    # Calcula la matriz de covarianza de la innovación
    S = np.dot(H, np.dot(P_prediccion, H.T)) + R
    # Calcula la ganancia de Kalman
    K = np.dot(P_prediccion, np.dot(H.T, np.linalg.inv(S)))
    # Actualiza el estado estimado
    x_actualizado = x_prediccion + np.dot(K, y)
    # Actualiza la covarianza del estado
    P_actualizado = P_prediccion - np.dot(K, np.dot(H, P_prediccion))
    return x_actualizado, P_actualizado

# Intervalo de tiempo entre cada actualización
dt = 0.05
# Matriz de transición de estado (modelo dinámico del sistema)
F = np.array([[1, dt], [0, 1]])
# Matriz de observación (relaciona el estado con las observaciones)
H = np.array([[1, 0]])
# Covarianza del proceso (incertidumbre del modelo)
Q = np.array([[0.01, 0], [0, 0.001]])
# Covarianza de la medición (incertidumbre de las observaciones)
R = np.array([[0.5]])

# Estado inicial (posición y velocidad)
x = np.array([10, 0])
# Covarianza inicial del estado
P = np.array([[1, 0], [0, 1]])

# Datos de la medición
mediciones = [10.2, 10.5, 11.0, 11.6, 11.8]

# Listas para almacenar los resultados de la estimación
resultados_estado = []
resultados_covarianza = []

# Aplicar el filtro de Kalman extendido (EKF) para cada medición
for z in mediciones:
    # Predicción del estado siguiente
    x_prediccion, P_prediccion = prediccion(x, P, F, Q)
    # Actualización del estado basada en la medición
    x, P = actualización(x_prediccion, P_prediccion, z, H, R)
    # Almacenar los resultados de la estimación del estado y la covarianza
    resultados_estado.append(x)
    resultados_covarianza.append(P)

# Imprimir los resultados de la estimación
for i in range(len(mediciones)):
    print("Medición:", mediciones[i])
    print("Estado estimado:", resultados_estado[i])
    print("Covarianza del estado:", resultados_covarianza[i])
    print()
