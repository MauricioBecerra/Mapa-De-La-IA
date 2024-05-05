class Ontology:
    def __init__(self):
        # Inicializa una nueva ontología vacía
        self.ontology = {}

    def add_relation(self, subject, relation, object):
        # Agrega una relación entre un sujeto, una relación y un objeto a la ontología
        if subject not in self.ontology:
            # Si el sujeto no existe en la ontología, crea un nuevo diccionario para él
            self.ontology[subject] = {}
        if relation not in self.ontology[subject]:
            # Si la relación no existe para el sujeto, crea un nuevo conjunto para ella
            self.ontology[subject][relation] = set()
        # Agrega el objeto a la relación del sujeto
        self.ontology[subject][relation].add(object)

    def query(self, subject, relation):
        # Realiza una consulta en la ontología para encontrar objetos relacionados con un sujeto a través de una relación
        if subject in self.ontology and relation in self.ontology[subject]:
            # Si el sujeto y la relación existen en la ontología, devuelve el conjunto de objetos relacionados
            return self.ontology[subject][relation]
        else:
            # Si no se encuentra ninguna relación, devuelve un conjunto vacío
            return set()

# Creación de la ontología
ontology = Ontology()

# Agregar relaciones a la ontología
ontology.add_relation("Perro", "es_un", "Animal")
ontology.add_relation("Perro", "tiene", "Cuatro patas")
ontology.add_relation("Perro", "hace", "Ladrar")
ontology.add_relation("Perro", "come", "Carne")
ontology.add_relation("Gato", "es_un", "Animal")
ontology.add_relation("Gato", "tiene", "Cuatro patas")
ontology.add_relation("Gato", "hace", "Maullar")
ontology.add_relation("Gato", "come", "Pescado")

# Consultas a la ontología
print("El perro es un:", ontology.query("Perro", "es_un"))
print("El gato tiene:", ontology.query("Gato", "tiene"))
print("¿Qué hace un perro?", ontology.query("Perro", "hace"))
print("¿Qué hace un gato?", ontology.query("Gato", "hace"))
print("¿Qué come un perro?", ontology.query("Perro", "come"))
print("¿Qué come un gato?", ontology.query("Gato", "come"))
