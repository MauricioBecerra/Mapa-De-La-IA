import numpy as np  # Importa la librería NumPy para manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Importa matplotlib para graficar
from sklearn.datasets import make_moons  # Importa make_moons para generar datos en forma de media luna
from sklearn.cluster import AgglomerativeClustering  # Importa AgglomerativeClustering para el agrupamiento jerárquico
from sklearn.neighbors import KNeighborsClassifier  # Importa KNeighborsClassifier para el clasificador k-NN

# Genera datos de ejemplo con dos clusters en forma de media luna
X, y = make_moons(n_samples=400, noise=0.1, random_state=42)
# Se crean 400 puntos distribuidos en dos media lunas con un poco de ruido.

plt.figure(figsize=(12, 4))  # Se crea una figura con un tamaño específico

plt.subplot(131)  # Se crea el primer subplot en una fila de 1x3, posición 1
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # Se grafican los datos con colores según las etiquetas
plt.title("Datos de entrada")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje x
plt.ylabel("Característica 2")  # Etiqueta del eje y

# Aplica k-NN
knn = KNeighborsClassifier(n_neighbors=5)  # Crea una instancia del clasificador k-NN con 5 vecinos
knn.fit(X, y)  # Entrena el clasificador con los datos de entrada

plt.subplot(132)  # Se crea el segundo subplot en una fila de 1x3, posición 2
plt.scatter(X[:, 0], X[:, 1], c=knn.predict(X), cmap='viridis')  # Se grafican los datos coloreados según las predicciones de k-NN
plt.title("k-NN")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje x
plt.ylabel("Característica 2")  # Etiqueta del eje y

# Aplica agrupamiento jerárquico aglomerativo
agglomerative = AgglomerativeClustering(n_clusters=2)  # Crea una instancia del algoritmo de agrupamiento jerárquico con 2 clusters
labels = agglomerative.fit_predict(X)  # Realiza el agrupamiento y asigna etiquetas a los clusters

plt.subplot(133)  # Se crea el tercer subplot en una fila de 1x3, posición 3
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')  # Se grafican los datos con colores según las etiquetas de cluster
plt.title("Agrupamiento Aglomerativo")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje x
plt.ylabel("Característica 2")  # Etiqueta del eje y

plt.tight_layout()  # Ajusta el diseño de los subplots para evitar superposiciones
plt.show()  # Muestra la figura con los subplots
