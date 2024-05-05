import numpy as np  # Importa la librería NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la librería Matplotlib para visualización

num_particles = 1500  # Número de partículas
map_limit_x = 12  # Límite del mapa en el eje x
map_limit_y = 12  # Límite del mapa en el eje y
num_steps = 25  # Número de pasos

# Función para generar partículas aleatorias dentro del área del mapa
def generate_particles(num_particles, limit_x, limit_y):
    return np.random.uniform(low=(0, 0), high=(limit_x, limit_y), size=(num_particles, 2))

# Función para simular la medición de distancia (en este caso, solo usamos la distancia al origen)
def measure_distance(position):
    return np.linalg.norm(position, axis=1)

# Función para realizar el re-muestreo de las partículas basadas en las probabilidades de peso
def resample_particles(particles, weights):
    indices = np.random.choice(len(particles), size=len(particles), p=weights)
    return particles[indices]

# Función para visualizar el mapa y la trayectoria estimada del robot
def visualize_map(particles, trajectory, real_map=None):
    plt.figure(figsize=(8, 6))  # Configura el tamaño de la figura
    plt.scatter(particles[:, 0], particles[:, 1], color='b', s=5, alpha=0.5)  # Dibuja las partículas en azul
    plt.plot(trajectory[:, 0], trajectory[:, 1], color='r', linewidth=2)  # Dibuja la trayectoria estimada en rojo
    if real_map is not None:
        plt.scatter(real_map[:, 0], real_map[:, 1], color='g', s=20, marker='x')  # Dibuja el mapa real (si está disponible) en verde
    plt.xlabel('X')  # Etiqueta del eje X
    plt.ylabel('Y')  # Etiqueta del eje Y
    plt.title('Mapa y trayectoria estimada del robot')  # Título de la gráfica
    plt.grid(True)  # Habilita la cuadrícula en la gráfica
    plt.axis('equal')  # Configura los ejes para que tengan la misma escala
    plt.show()  # Muestra la gráfica

# Inicialización: Generar partículas aleatorias uniformemente distribuidas en el área del mapa
particles = generate_particles(num_particles, map_limit_x, map_limit_y)

# Inicializar trayectoria del robot
trajectory = np.zeros((num_steps, 2))

# Iteración a través de los pasos de tiempo
for step in range(num_steps):
    # Movimiento: Simular el movimiento del robot (en este ejemplo, simplemente se agrega ruido gaussiano a las partículas)
    particles += np.random.normal(loc=0, scale=0.7, size=particles.shape)

    # Medición: Simular la obtención de observaciones (en este caso, solo la distancia al origen)
    measurements = measure_distance(particles)

    # Calcular pesos basados en las medidas (usamos la inversa de la distancia como una medida de similitud)
    weights = 1 / measurements
    weights /= np.sum(weights)  # Normalizar los pesos para obtener una distribución de probabilidad

    # Re-muestreo: Actualizar las partículas basadas en los pesos
    particles = resample_particles(particles, weights)

    # Actualizar la trayectoria del robot (usamos la posición promedio de las partículas)
    trajectory[step] = np.mean(particles, axis=0)

# Visualizar el mapa y la trayectoria estimada del robot
visualize_map(particles, trajectory)