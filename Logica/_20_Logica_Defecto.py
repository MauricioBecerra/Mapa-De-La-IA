class DefaultLogic:
    def __init__(self):
        self.knowledge_base = {}  # Inicializa la base de conocimiento como un diccionario vacío

    def add_rule(self, rule, conclusion):
        if conclusion not in self.knowledge_base:
            self.knowledge_base[conclusion] = []  # Si la conclusión no está en la base de conocimiento, se agrega como una nueva lista
        self.knowledge_base[conclusion].append(rule)  # Se agrega la regla a la lista de reglas para la conclusión

    def infer(self, query):
        if query in self.knowledge_base:  # Si la consulta está en la base de conocimiento
            print("La conclusión es verdadera debido a las siguientes reglas:")  # Se imprime un mensaje indicando que la conclusión es verdadera
            for rule in self.knowledge_base[query]:  # Se itera sobre las reglas asociadas a la conclusión
                print("- ", rule)  # Se imprime cada regla
        else:
            print("No se puede inferir la verdad de la conclusión.")  # Si la consulta no está en la base de conocimiento, se imprime un mensaje de que la conclusión no puede ser inferida

# Creamos una instancia de DefaultLogic
dl = DefaultLogic()

# Agregamos reglas a la base de conocimiento
dl.add_rule("Si es un ave, entonces vuela.", "vuela")
dl.add_rule("Si es un pingüino, entonces no vuela.", "no vuela")

# Consultamos si "vuela" es verdadero
query = "vuela"
dl.infer(query)