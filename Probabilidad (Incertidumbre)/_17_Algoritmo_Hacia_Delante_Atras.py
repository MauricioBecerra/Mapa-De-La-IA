class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.padres = []  # Lista para almacenar los nodos padres
        self.hijos = []   # Lista para almacenar los nodos hijos
        self.probabilidad = None  # Probabilidad inicialmente nula

    def agregar_padre(self, padre):  # Método para agregar un nodo padre
        self.padres.append(padre)

    def agregar_hijo(self, hijo):  # Método para agregar un nodo hijo
        self.hijos.append(hijo)


class RedBayesiana:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos de la red bayesiana

    def agregar_nodo(self, nombre):  # Método para agregar un nuevo nodo
        self.nodos[nombre] = Nodo(nombre)  # Crea un nuevo nodo con el nombre dado

    def agregar_arco(self, padre, hijo):  # Método para agregar un arco dirigido entre nodos
        self.nodos[padre].agregar_hijo(self.nodos[hijo])  # Agrega el hijo a la lista de hijos del padre
        self.nodos[hijo].agregar_padre(self.nodos[padre])  # Agrega el padre a la lista de padres del hijo

    def hacia_adelante(self):  # Método para realizar la propagación hacia adelante
        for nombre_nodo in self.nodos:  # Itera sobre todos los nodos
            nodo = self.nodos[nombre_nodo]  # Obtiene el nodo actual
            if not nodo.padres:  # Si el nodo no tiene padres
                nodo.probabilidad = 0.5  # Establece la probabilidad en 0.5
            else:  # Si el nodo tiene padres
                nodo.probabilidad = 1.0  # Inicializa la probabilidad en 1.0
                for padre in nodo.padres:  # Itera sobre los padres
                    nodo.probabilidad *= padre.probabilidad  # Multiplica las probabilidades de los padres

    def hacia_atras(self, consulta, evidencia):  # Método para realizar la propagación hacia atrás
        for nombre_nodo in self.nodos:  # Itera sobre todos los nodos
            nodo = self.nodos[nombre_nodo]  # Obtiene el nodo actual
            if nombre_nodo in evidencia:  # Si el nodo está en la evidencia
                nodo.probabilidad = evidencia[nombre_nodo]  # Actualiza la probabilidad con el valor de la evidencia

        for nombre_nodo in reversed(list(self.nodos.keys())):  # Itera en orden inverso
            nodo = self.nodos[nombre_nodo]  # Obtiene el nodo actual
            if nombre_nodo != consulta:  # Si no es el nodo de consulta
                suma = 0.0  # Inicializa la suma de las probabilidades de los hijos
                for hijo in nodo.hijos:  # Itera sobre los hijos
                    suma += hijo.probabilidad  # Agrega la probabilidad del hijo a la suma
                nodo.probabilidad *= suma  # Multiplica la probabilidad por la suma de las probabilidades de los hijos

# Creación de una nueva red bayesiana y definición de nodos y arcos
red_bayesiana = RedBayesiana()
red_bayesiana.agregar_nodo("X")  # Agrega un nodo X
red_bayesiana.agregar_nodo("Y")  # Agrega un nodo Y
red_bayesiana.agregar_nodo("Z")  # Agrega un nodo Z

red_bayesiana.agregar_arco("X", "Y")  # Agrega un arco de X a Y
red_bayesiana.agregar_arco("Y", "Z")  # Agrega un arco de Y a Z

red_bayesiana.hacia_adelante()  # Realiza la propagación hacia adelante
red_bayesiana.hacia_atras("Z", {"X": 0.6, "Y": 0.7})  # Realiza la propagación hacia atrás con evidencia para X e Y

# Imprime las probabilidades resultantes
for nombre_nodo in red_bayesiana.nodos:  # Itera sobre todos los nodos
    nodo = red_bayesiana.nodos[nombre_nodo]  # Obtiene el nodo actual
    print(f"Probabilidad de {nodo.nombre}: {nodo.probabilidad}")  # Imprime la probabilidad del nodo