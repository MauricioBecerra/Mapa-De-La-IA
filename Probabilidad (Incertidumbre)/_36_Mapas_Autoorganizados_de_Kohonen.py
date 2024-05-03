import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas
from minisom import MiniSom  # Importa MiniSom, una biblioteca para implementar SOM
import matplotlib.pyplot as plt  # Importa matplotlib para visualización
from matplotlib.gridspec import GridSpec  # Importa GridSpec para manejar la disposición de subtramas

# Datos de ejemplo (5 dimensiones)
data = np.array([[0.1, 0.9, 0.4, 0.6, 0.7],
                  [0.7, 0.2, 0.6, 0.3, 0.8],
                  [0.9, 0.5, 0.2, 0.7, 0.1],
                  [0.2, 0.4, 0.8, 0.1, 0.5],
                  [0.4, 0.6, 0.1, 0.9, 0.3],
                  [0.5, 0.3, 0.7, 0.2, 0.4]])

# Tamaño del SOM
som_rows = 8  # Número de filas en el SOM
som_cols = 8  # Número de columnas en el SOM

# Entrenamiento del SOM
som = MiniSom(som_rows, som_cols, data.shape[1], sigma=1.5, learning_rate=0.4)  # Crea una instancia de MiniSom
som.train_random(data, 1500)  # Entrenamiento con 1500 iteraciones

# Mapa de calor de las neuronas
plt.figure(figsize=(10, 8))  # Crea una figura con el tamaño especificado
plt.pcolor(som.distance_map().T, cmap='coolwarm')  # Plot de la distancia de cada neurona a sus vecinas
plt.colorbar()  # Agrega una barra de color para mostrar la escala de colores

# Plot de los datos en el SOM
plt.figure(figsize=(10, 8))  # Crea una nueva figura con el tamaño especificado
for i, d in enumerate(data):  # Itera sobre los datos de entrada
    winning_position = som.winner(d)  # Encuentra la posición ganadora para el dato actual
    plt.text(winning_position[0]+0.5, winning_position[1]+0.5, str(i),
             color='k', fontdict={'weight': 'bold', 'size': 11})  # Etiqueta la posición ganadora con el índice del dato

plt.axis([0, som_rows, 0, som_cols])  # Establece los límites del eje x e y
plt.gca().invert_yaxis()  # Invierte el eje y para que la numeración comience desde arriba
plt.title('Mapa Autoorganizado de Kohonen')  # Establece el título del gráfico
plt.show()  # Muestra el gráfico