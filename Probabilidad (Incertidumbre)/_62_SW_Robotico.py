import numpy as np  

def control_p(error, Kp):
    return Kp * error  # Función para calcular la corrección proporcional de la velocidad

Kp_value = 0.2  # Nueva ganancia proporcional

x_initial = 2  # Nueva posición inicial en el eje x
y_initial = -1  # Nueva posición inicial en el eje y
theta_initial = np.pi / 4  # Nueva orientación inicial del robot (en radianes)
v_robot = 1.5  # Nueva velocidad lineal del robot

x_line = np.linspace(-4, 4, 100)  # Nuevas coordenadas x de la línea a seguir
y_line = np.cos(x_line)  # Nuevas coordenadas y de la línea a seguir

time_step = 0.05  # Nuevo paso de tiempo
time_simulation = np.arange(0, 15, time_step)  # Nuevo vector de tiempo

x_robot_hist = []  # Historial de posiciones en x del robot
y_robot_hist = []  # Historial de posiciones en y del robot

for t in time_simulation:
    error = y_initial - np.interp(x_initial, x_line, y_line)  # Calcula el error de seguimiento de la línea
    correction_speed = control_p(error, Kp_value)  # Calcula la corrección de velocidad proporcional
    x_initial += v_robot * np.cos(theta_initial) * time_step  # Actualiza la posición x del robot
    y_initial += v_robot * np.sin(theta_initial) * time_step  # Actualiza la posición y del robot
    theta_initial -= correction_speed * time_step  # Actualiza la orientación del robot
    x_robot_hist.append(x_initial)  # Almacena la posición x actual del robot
    y_robot_hist.append(y_initial)  # Almacena la posición y actual del robot

import matplotlib.pyplot as plt  

plt.figure(figsize=(8, 6))

plt.plot(x_line, y_line, label='Línea a seguir', color='black')  # Grafica la línea a seguir

plt.plot(x_robot_hist, y_robot_hist, label='Trayectoria del robot', color='red')  # Grafica la trayectoria del robot

plt.xlabel('Posición en x')  # Etiqueta del eje x
plt.ylabel('Posición en y')  # Etiqueta del eje y
plt.title('Movimiento del Robot Siguiendo una Línea')  # Título de la gráfica
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra la cuadrícula
plt.axis('equal')  # Ajusta los ejes para que tengan la misma escala

plt.show()  # Muestra la gráfica
