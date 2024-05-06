class FOIL:
    def __init__(self, target_predicate, background_knowledge):
        self.target_predicate = target_predicate  # Predicado objetivo
        self.background_knowledge = background_knowledge  # Conocimiento de fondo

    def train(self, examples):
        self.specific_clause = self.find_specific_clause(examples)  # Encuentra la cláusula específica
        self.general_clause = self.find_general_clause(examples)  # Encuentra la cláusula general

    def find_specific_clause(self, examples):
        specific_clause = []

        for example in examples:
            if example[1] == 'Yes':
                specific_clause.append(example[0])  # Agrega la instancia a la cláusula específica si la clase es 'Yes'

        return specific_clause

    def find_general_clause(self, examples):
        general_clause = []

        for example in examples:
            if example[1] == 'No':
                general_clause.append(example[0])  # Agrega la instancia a la cláusula general si la clase es 'No'

        return general_clause

    def predict(self, example):
        for term in self.specific_clause:
            if term not in example[0]:
                return 'No'  # Si algún término de la cláusula específica no está presente en el ejemplo, retorna 'No'

        for term in self.general_clause:
            if term in example[0]:
                return 'No'  # Si algún término de la cláusula general está presente en el ejemplo, retorna 'No'

        return 'Yes'  # Si no se encuentra ninguna contradicción, retorna 'Yes'

# Nuevo conjunto de datos de ejemplo
examples = [
    (['nublado', 'frio', 'normal'], 'No'),
    (['soleado', 'calor', 'alta'], 'Yes'),
    (['nublado', 'calor', 'normal'], 'Yes'),
    (['lluvia', 'frio', 'normal'], 'No'),
    (['soleado', 'templado', 'alta'], 'Yes')
]

# Predicado objetivo y conocimiento de fondo
target_predicate = 'Jugar'
background_knowledge = []

# Entrenamiento del modelo FOIL
foil = FOIL(target_predicate, background_knowledge)
foil.train(examples)

# Predicción para un nuevo ejemplo
new_example = (['soleado', 'frio', 'normal'], 'Unknown')
prediction = foil.predict(new_example)
print("Predicción para el ejemplo:", prediction)
