class BayesianNetwork:
    def __init__(self):
        self.nodes = {}  # Inicializa un diccionario para almacenar los nodos de la red bayesiana

    def add_node(self, node_name, parents, probabilities):
        """
        Agrega un nodo a la red bayesiana con sus padres y las probabilidades condicionales.

        Args:
        - node_name: El nombre del nodo.
        - parents: Una lista de nombres de los padres del nodo.
        - probabilities: Un diccionario de tuplas de padres a la probabilidad del nodo dado esos padres.
        """
        self.nodes[node_name] = {'parents': parents, 'probabilities': probabilities}  # Agrega el nodo al diccionario de nodos

    def calculate_probability(self, node_name, evidence):
        """
        Calcula la probabilidad de un nodo dado una evidencia.

        Args:
        - node_name: El nombre del nodo cuya probabilidad se quiere calcular.
        - evidence: Un diccionario que contiene la evidencia de los padres del nodo.

        Returns:
        - La probabilidad del nodo dado la evidencia.
        """
        if node_name not in self.nodes:
            print(f"El nodo {node_name} no está presente en la red.")
            return None

        node = self.nodes[node_name]
        parents = node['parents']
        probabilities = node['probabilities']

        if set(parents) != set(evidence.keys()):
            print(f"No se proporcionó evidencia para todos los padres de {node_name}.")
            return None

        probability_index = tuple(evidence[parent] for parent in parents)  # Obtiene el índice correspondiente a las evidencias
        probability = probabilities[probability_index]  # Obtiene la probabilidad del nodo dado los valores de los padres

        return probability

bn = BayesianNetwork()

# Agrega nodos y sus probabilidades condicionales
bn.add_node('Lluvia', [], {(): 0.2})  # Nodo Lluvia sin padres
bn.add_node('Riego', ['Lluvia'], {(True,): 0.1, (False,): 0.5})  # Nodo Riego con un padre Lluvia

# Calcula la probabilidad de lluvia
print("Probabilidad de lluvia:")
print("P(Lluvia) =", bn.calculate_probability('Lluvia', {}))

# Calcula la probabilidad de riego dado que está lloviendo
print("\nProbabilidad de riego dado que está lloviendo:")
print("P(Riego | Lluvia=True) =", bn.calculate_probability('Riego', {'Lluvia': True}))

# Calcula la probabilidad de riego dado que no está lloviendo
print("\nProbabilidad de riego dado que no está lloviendo:")
print("P(Riego | Lluvia=False) =", bn.calculate_probability('Riego', {'Lluvia': False}))
