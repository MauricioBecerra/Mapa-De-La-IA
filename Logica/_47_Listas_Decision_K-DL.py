import numpy as np  # Importa numpy para operaciones numéricas

class KDLClassifier:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        y_pred = []
        for sample in X:
            # Calcula las distancias euclidianas entre el nuevo punto y todos los puntos en el conjunto de entrenamiento
            distances = np.sqrt(np.sum((self.X - sample) ** 2, axis=1))
            # Encuentra los índices de los k vecinos más cercanos
            k_nearest_indices = np.argsort(distances)[:self.k]
            # Obtiene las etiquetas de los k vecinos más cercanos
            k_nearest_labels = self.y[k_nearest_indices]
            # Cuenta las ocurrencias de cada etiqueta
            unique_labels, counts = np.unique(k_nearest_labels, return_counts=True)
            # Elige la etiqueta con la mayor cantidad de ocurrencias como la predicción
            predicted_label = unique_labels[np.argmax(counts)]
            y_pred.append(predicted_label)
        return np.array(y_pred)

# Carga un conjunto de datos diferente (cáncer de mama de Wisconsin)
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carga el conjunto de datos de cáncer de mama de Wisconsin
breast_cancer = load_breast_cancer()

# Obtiene las características (X) y las etiquetas (y) del conjunto de datos de cáncer de mama
X = breast_cancer.data
y = breast_cancer.target

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea y entrena el clasificador K-DL con k=7
kdl_classifier = KDLClassifier(k=7)
kdl_classifier.fit(X_train, y_train)

# Realiza predicciones sobre los datos de prueba
y_pred = kdl_classifier.predict(X_test)

# Calcula la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Imprime la precisión del clasificador K-DL
print("Precisión del clasificador K-DL en el conjunto de datos de cáncer de mama de Wisconsin:", accuracy)
