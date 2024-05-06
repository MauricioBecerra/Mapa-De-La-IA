class MejorHipotesisActual:
    def __init__(self, features, target):
        self.features = features  # Características utilizadas para entrenar el modelo
        self.target = target  # Etiqueta objetivo
        self.hypothesis = None  # Inicialmente, la hipótesis es nula

    def train(self, instances):
        self.hypothesis = {}  # Inicializa la hipótesis como un diccionario vacío
        for i, val in enumerate(self.features):
            self.hypothesis[val] = self.find_most_frequent_value(instances, i)  # Encuentra el valor más frecuente para cada característica

    def find_most_frequent_value(self, instances, index):
        values = [instance[index] for instance in instances]  # Obtiene los valores para la característica específica
        return max(set(values), key=values.count)  # Encuentra el valor más frecuente

    def predict(self, instance):
        if self.hypothesis is None:
            raise Exception("El modelo aún no ha sido entrenado.")
        prediction = self.hypothesis[self.features[0]]  # Inicialmente, predice con el valor más frecuente de la primera característica
        for i, val in enumerate(self.features):
            if instance[i] != self.hypothesis[val]:  # Si el valor de la instancia no coincide con el de la hipótesis
                return prediction  # Retorna la predicción actual
        return prediction  # Si no hay discrepancias, retorna la predicción

# Nuevo conjunto de datos y características
features = ['F1', 'F2', 'F3']
target = 'Clase'
instances = [
    ['A', 'X', 'Y', 'Positivo'],
    ['B', 'X', 'Y', 'Positivo'],
    ['A', 'Z', 'Y', 'Negativo'],
    ['B', 'Z', 'X', 'Negativo'],
    ['A', 'X', 'X', 'Positivo']
]

# Crea una instancia del modelo MejorHipotesisActual
mha = MejorHipotesisActual(features, target)

# Entrena el modelo con el conjunto de datos
mha.train(instances)

# Nueva instancia para predecir
new_instance = ['B', 'X', 'X']

# Realiza una predicción sobre la nueva instancia
prediction = mha.predict(new_instance)

# Imprime la predicción
print("Predicción:", prediction)