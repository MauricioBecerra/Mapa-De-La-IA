import numpy as np
import matplotlib.pyplot as plt

# Función de control PD
def control_pd(theta, theta_p, Kp, Kd):
    # Calcula la señal de control como la suma de la componente proporcional y derivativa
    return Kp * theta + Kd * theta_p

# Parámetros del péndulo
m = 0.5  # Masa del péndulo (kg)
l = 0.8  # Longitud del péndulo (m)
g = 9.81  # Aceleración debido a la gravedad (m/s^2)

# Parámetros del control PD
Kp = 15  # Ganancia proporcional
Kd = 3   # Ganancia derivativa

# Condiciones iniciales
theta_0 = np.pi / 3  # Ángulo inicial del péndulo (rad)
theta_p_0 = 0         # Velocidad angular inicial del péndulo (rad/s)

# Tiempo de simulación
dt = 0.02                         # Paso de tiempo (s)
t_simulacion = np.arange(0, 10, dt)  # Vector de tiempo (s)

# Inicialización de variables
theta = theta_0         # Ángulo inicial del péndulo
theta_p = theta_p_0     # Velocidad angular inicial del péndulo
theta_hist = []         # Historial de ángulos del péndulo
theta_p_hist = []       # Historial de velocidades angulares del péndulo
u_hist = []             # Historial de señales de control

# Simulación del control del péndulo
for t in t_simulacion:
    # Almacena los valores actuales de ángulo y velocidad angular
    theta_hist.append(theta)
    theta_p_hist.append(theta_p)
    
    # Calcula la señal de control utilizando el control PD
    u = control_pd(theta, theta_p, Kp, Kd)
    u_hist.append(u)
    
    # Calcula la aceleración angular utilizando el modelo dinámico del péndulo
    theta_pp = (-g / l) * np.sin(theta) + u / (m * l**2)
    
    # Actualiza el ángulo y la velocidad angular utilizando la integración numérica
    theta += theta_p * dt
    theta_p += theta_pp * dt

# Visualización de los resultados
plt.figure(figsize=(10, 6))

# Graficar el ángulo del péndulo en función del tiempo
plt.subplot(2, 1, 1)
plt.plot(t_simulacion, np.rad2deg(theta_hist), label='Ángulo (grados)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (grados)')
plt.legend()

# Graficar la velocidad angular del péndulo en función del tiempo
plt.subplot(2, 1, 2)
plt.plot(t_simulacion, np.rad2deg(theta_p_hist), label='Velocidad Angular (grados/s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Angular (grados/s)')
plt.legend()

plt.tight_layout()
plt.show()
