import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para graficar

# Nuevos valores para la media y la desviación estándar
mean = 2
std_dev = 0.5
num_samples = 500
num_steps = 50

# Generación de muestras con la nueva media y desviación estándar
samples = np.random.normal(mean, std_dev, size=(num_samples, num_steps))

# Cálculo de la media y la varianza a lo largo del tiempo
mean_over_time = np.mean(samples, axis=0)  # Calcula la media a lo largo del tiempo
variance_over_time = np.var(samples, axis=0)  # Calcula la varianza a lo largo del tiempo

# Creación de pasos de tiempo para el eje x
time_steps = np.arange(num_steps)  # Crea una matriz de pasos de tiempo
plt.figure(figsize=(10, 6))  # Establece el tamaño de la figura
plt.plot(time_steps, mean_over_time, label='Media')  # Grafica la evolución de la media en función del tiempo
plt.plot(time_steps, variance_over_time, label='Varianza')  # Grafica la evolución de la varianza en función del tiempo
plt.xlabel('Tiempo')  # Etiqueta del eje x
plt.ylabel('Valor')  # Etiqueta del eje y
plt.title('Evolución de la Media y la Varianza con Nueva Configuración')  # Título de la gráfica
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra una cuadrícula en el gráfico
plt.show()  # Muestra la gráfica
