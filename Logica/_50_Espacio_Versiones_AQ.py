class EspacioVersiones:
    def __init__(self, num_features):
        self.num_features = num_features  # Número de características
        self.hypothesis = ['0'] * num_features  # Inicializa la hipótesis con valores por defecto

    def generalize(self, instance):
        for i, value in enumerate(instance):
            if self.hypothesis[i] != value:
                self.hypothesis[i] = '?'  # Generaliza la hipótesis si hay diferencias

    def specialize(self, instance):
        for i, value in enumerate(instance):
            if self.hypothesis[i] == '?':
                self.hypothesis[i] = value  # Especializa la hipótesis si hay valores específicos

    def predict(self, instance):
        for i, value in enumerate(instance):
            if self.hypothesis[i] != '?' and self.hypothesis[i] != value:
                return 'No se puede clasificar'  # Si hay discrepancias, no se puede clasificar
        return 'Positivo'  # Si no hay discrepancias, la predicción es positiva

class AQ:
    def __init__(self, num_features):
        self.hypothesis = EspacioVersiones(num_features)

    def train(self, instances):
        for instance in instances:
            if instance[-1] == 'Positivo':
                self.hypothesis.generalize(instance[:-1])  # Generaliza si es positivo
            else:
                self.hypothesis.specialize(instance[:-1])  # Especializa si es negativo

    def predict(self, instance):
        return self.hypothesis.predict(instance)

# Nuevo conjunto de datos de ejemplo
new_instances = [
    ['1', '0', 'Positivo'],
    ['?', '0', 'Negativo'],
    ['1', '?', 'Positivo'],
    ['?', '?', 'Negativo']
]

# Entrenamiento del modelo
aq = AQ(num_features=2)
aq.train(new_instances)

# Predicción de nuevas instancias
new_instances_to_predict = [
    ['1', '1'],
    ['0', '1'],
    ['1', '0'],
    ['0', '0']
]

for instance in new_instances_to_predict:
    prediction = aq.predict(instance)
    print("Instancia:", instance, "Predicción:", prediction)
