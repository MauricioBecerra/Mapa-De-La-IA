import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons  # Cambio: Usamos make_moons en lugar de make_circles
from sklearn.svm import SVC

# Genera datos de ejemplo en forma de dos medias lunas con ruido
X, y = make_moons(n_samples=200, noise=0.2, random_state=42)  # Cambio: Usamos make_moons
# Se generan 200 puntos distribuidos en dos medias lunas con ruido

# Visualiza los datos de entrada
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # Grafica los puntos de datos con colores basados en las etiquetas y
plt.title("Datos de entrada")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje x
plt.ylabel("Característica 2")  # Etiqueta del eje y
plt.show()

# Entrena un modelo SVM con kernel RBF
svm = SVC(kernel='rbf', C=10, gamma='auto', random_state=42)  # Cambio: Ajustamos C y gamma
svm.fit(X, y)

# Función para visualizar las fronteras de decisión
def plot_decision_boundaries(model, X, y):
    h = .02  # Tamaño del paso para la malla
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1  # Límites del eje x
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1  # Límites del eje y
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))  # Malla de puntos para visualización
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])  # Predicciones para cada punto de la malla
    Z = Z.reshape(xx.shape)  # Ajuste de la forma de Z
    plt.contourf(xx, yy, Z, alpha=0.8, cmap='viridis')  # Regiones de decisión
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # Puntos de datos

# Visualiza las fronteras de decisión del modelo SVM
plt.figure(figsize=(6, 6))
plot_decision_boundaries(svm, X, y)
plt.title("Fronteras de decisión SVM con kernel RBF")  # Título del gráfico
plt.xlabel("Característica 1")  # Etiqueta del eje x
plt.ylabel("Característica 2")  # Etiqueta del eje y
plt.show()