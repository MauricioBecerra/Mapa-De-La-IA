from sklearn.datasets import load_breast_cancer  # Importa un nuevo conjunto de datos
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Carga un conjunto de datos diferente (cáncer de mama de Wisconsin)
breast_cancer = load_breast_cancer()

# Obtiene las características (X) y las etiquetas (y) del conjunto de datos de cáncer de mama
X = breast_cancer.data
y = breast_cancer.target

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea un clasificador de árbol de decisión
dt_classifier = DecisionTreeClassifier()

# Entrena el clasificador de árbol de decisión
dt_classifier.fit(X_train, y_train)

# Realiza predicciones sobre los datos de prueba
y_pred = dt_classifier.predict(X_test)

# Calcula la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Imprime la precisión del clasificador de árbol de decisión
print("Precisión del clasificador de árbol de decisión:", accuracy)
