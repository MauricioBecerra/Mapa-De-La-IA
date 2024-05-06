class Regla:
    def __init__(self, condiciones, clase):
        self.condiciones = condiciones  # Condiciones de la regla
        self.clase = clase  # Clase que representa la regla

    def cubre(self, instancia):
        for i, condicion in enumerate(self.condiciones):
            if condicion != instancia[i] and condicion != '?':
                return False  # La regla no cubre la instancia si alguna condición no coincide
        return True  # La regla cubre completamente la instancia

class AprendizajeInductivo:
    def __init__(self, features, target):
        self.features = features  # Características (atributos) de las instancias
        self.target = target  # Clase objetivo
        self.reglas = []  # Lista de reglas aprendidas

    def train(self, instances):
        for instance in instances:
            regla = Regla(instance[:-1], instance[-1])  # Crea una nueva regla
            self.reglas.append(regla)  # Agrega la regla a la lista de reglas

    def explain(self, instance):
        explanations = []  # Almacenará las explicaciones de la instancia
        for regla in self.reglas:
            if regla.cubre(instance):
                explanation = {
                    'regla': regla.condiciones,
                    'clase': regla.clase
                }  # Guarda la regla y su clase asociada
                explanations.append(explanation)  # Agrega la explicación a la lista
        return explanations

# Nuevo conjunto de datos de ejemplo
new_instances = [
    ['Soleado', 'Calor', 'Normal', 'Si'],
    ['Lluvia', 'Frio', '?', 'No'],
    ['Nublado', '?', 'Alto', 'Si'],
    ['Soleado', 'Templado', 'Alto', 'Si']
]

# Entrenamiento del modelo con el nuevo conjunto de datos
ai = AprendizajeInductivo(features=['Tiempo', 'Temperatura', 'Humedad'], target='Jugar')
ai.train(new_instances)

# Explicaciones para nuevas instancias
new_instance = ['Lluvia', 'Frio', 'Normal']  # Nueva instancia para explicar
explanations = ai.explain(new_instance)  # Obtiene las explicaciones para la instancia
print("Explicaciones para la instancia", new_instance)
for explanation in explanations:
    print("Regla:", explanation['regla'], "Clase:", explanation['clase'])  # Imprime las explicaciones
