class Creencia:
    def __init__(self, sujeto, objeto, predicado):
        # Inicializa una nueva creencia con un sujeto, objeto y predicado
        self.sujeto = sujeto
        self.objeto = objeto
        self.predicado = predicado

    def __str__(self):
        # Devuelve una representación en cadena de la creencia
        return f"({self.sujeto}, {self.predicado}, {self.objeto})"

class BaseConocimiento:
    def __init__(self):
        # Inicializa una nueva base de conocimiento con una lista vacía de creencias
        self.creencias = []

    def agregar_creencia(self, creencia):
        # Agrega una creencia a la base de conocimiento
        self.creencias.append(creencia)

    def consultar_creencias(self):
        # Muestra todas las creencias en la base de conocimiento
        for creencia in self.creencias:
            print(creencia)

# Creación de una base de conocimiento
bc = BaseConocimiento()

# Agregando creencias a la base de conocimiento
bc.agregar_creencia(Creencia("Juan", "hamburguesa", "come"))
bc.agregar_creencia(Creencia("María", "c++", "programa"))
bc.agregar_creencia(Creencia("Ana", "cuaderno", "apunta"))

# Consultando y mostrando las creencias en la base de conocimiento
print("Creencias en la base de conocimiento:")
bc.consultar_creencias()
