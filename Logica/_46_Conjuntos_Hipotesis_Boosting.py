import numpy as np  # Importa numpy para operaciones numéricas
from sklearn.datasets import load_wine  # Importa load_wine para cargar un conjunto de datos
from sklearn.model_selection import train_test_split  # Importa train_test_split para dividir los datos
from sklearn.ensemble import AdaBoostClassifier  # Importa AdaBoostClassifier para el modelo de boosting
from sklearn.metrics import accuracy_score  # Importa accuracy_score para calcular la precisión

# Carga un conjunto de datos diferente (vino)
wine = load_wine()

# Obtiene las características (X) y las etiquetas (y) del conjunto de datos de vino
X = wine.data
y = wine.target

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define los hiperparámetros del modelo de boosting
n_estimators = 100  # Número de estimadores (modelos) en el conjunto
learning_rate = 0.5  # Tasa de aprendizaje del modelo
random_state = 42  # Semilla aleatoria para reproducibilidad

# Crea el clasificador de boosting con AdaBoost
boosting_classifier = AdaBoostClassifier(n_estimators=n_estimators, learning_rate=learning_rate, random_state=random_state)

# Entrena el clasificador de boosting con los datos de entrenamiento
boosting_classifier.fit(X_train, y_train)

# Realiza predicciones sobre los datos de prueba
y_pred = boosting_classifier.predict(X_test)

# Calcula la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Imprime la precisión del clasificador
print("Precisión:", accuracy)
