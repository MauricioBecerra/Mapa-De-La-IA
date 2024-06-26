import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Genera datos de ejemplo con cuatro clusters
X, _ = make_blobs(n_samples=400, centers=4, cluster_std=0.8, random_state=42)
# La función make_blobs genera datos de puntos con clusters. 
# En este caso, creamos 400 puntos distribuidos en 4 clusters,
# con una desviación estándar de 0.8 y una semilla aleatoria fija para reproducibilidad.

# Inicializa el modelo K-Means con cuatro clusters
kmeans = KMeans(n_clusters=4, random_state=42)
# Crea una instancia del modelo K-Means con 4 clusters.
# KMeans es el estimador de scikit-learn que implementa el algoritmo K-Means para agrupamiento.

# Entrena el modelo K-Means
kmeans.fit(X)
# Entrena el modelo K-Means utilizando los datos X.

# Obtiene las etiquetas de cluster asignadas a cada muestra
etiquetas = kmeans.labels_
# Obtiene las etiquetas de cluster asignadas a cada muestra en X.

# Obtiene las coordenadas de los centroides de los clusters
centroides = kmeans.cluster_centers_
# Obtiene las coordenadas de los centroides de los clusters identificados por el modelo.

# Visualiza los clusters y los centroides
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', s=50, alpha=0.5)
# Dibuja los puntos de datos, coloreándolos según las etiquetas de cluster.
# El parámetro 'c' especifica los colores basados en las etiquetas de cluster.
# El parámetro 's' especifica el tamaño de los puntos.
# El parámetro 'alpha' controla la transparencia de los puntos.
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, marker='x')
# Dibuja los centroides de los clusters con un marcador 'x' de color rojo.
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Agrupamiento con K-Means')
plt.show()
# Añade etiquetas a los ejes y muestra el gráfico.
