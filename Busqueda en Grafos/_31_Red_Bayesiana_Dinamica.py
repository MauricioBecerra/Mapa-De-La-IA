class NodoRB():
    # Define la clase NodoRB para representar nodos en la red bayesiana
    def __init__(self, nombre, valores_posibles, padres=[], probabilidad={}, utilidad={}):
        # Inicializa el nodo con su nombre, valores posibles, padres, probabilidad y utilidad
        self.nombre = nombre  # Nombre del nodo
        self.valores_posibles = valores_posibles  # Lista de posibles valores que puede tomar el nodo
        self.padres = padres  # Lista de nodos padres
        self.probabilidad = probabilidad  # Probabilidades condicionales del nodo
        self.utilidad = utilidad  # Utilidades asociadas a cada valor posible del nodo

    def obtener_utilidad(self, valor):
        # Método para obtener la utilidad asociada a un valor del nodo
        return self.utilidad[valor]

    def obtener_probabilidad(self, valor, **padres):
        # Método para obtener la probabilidad condicional de un valor dado los valores de los nodos padres
        clave_padres = tuple(padres[variable] for variable in self.padres)  # Obtiene los valores de los nodos padres
        return self.probabilidad[clave_padres][valor]  # Devuelve la probabilidad condicional del nodo


class RedBayesianaDinamica():
    # Define la clase RedBayesianaDinamica para representar una red bayesiana dinámica
    def __init__(self, nodos=[]):
        # Inicializa la red bayesiana con una lista de nodos
        self.nodos = nodos  # Lista de nodos en la red bayesiana

    def obtener_utilidad_esperada(self, decisiones, **evidencia):
        # Método para calcular la utilidad esperada dadas las decisiones y la evidencia
        utilidad_total = 0
        for decision in decisiones:
            # Para cada decisión en la lista de decisiones
            evidencia_actual = evidencia.copy()  # Copia la evidencia actual
            evidencia_actual.update(decision)  # Agrega la decisión a la evidencia actual
            utilidad_total += decision['utilidad']  # Suma la utilidad de la decisión actual
            # Calcula la utilidad esperada sumando la utilidad de cada nodo condicionada a la evidencia actual
            for nodo in self.nodos:
                if nodo.nombre not in decision:
                    # Si el nodo no está en la decisión actual
                    probabilidad = nodo.obtener_probabilidad(evidencia_actual[nodo.nombre], **evidencia_actual)
                    # Obtiene la probabilidad condicional del nodo dado los valores de los nodos padres
                    utilidad = nodo.obtener_utilidad(evidencia_actual[nodo.nombre])
                    # Obtiene la utilidad asociada al valor del nodo
                    utilidad_total += probabilidad * utilidad  # Suma la utilidad ponderada por la probabilidad
        return utilidad_total  # Devuelve la utilidad esperada


# Ejemplo de uso
if __name__ == "__main__":
    # Creación de nodos y relaciones
    clima = NodoRB('Clima', ['Soleado', 'Lluvioso'])  # Nodo Clima con dos valores posibles
    actividad = NodoRB('Actividad', ['Correr', 'Nadar'], padres=['Clima'],  # Nodo Actividad con dos valores posibles y Clima como padre
                       probabilidad={('Soleado',): {'Correr': 0.8, 'Nadar': 0.2},  # Probabilidades condicionales para Clima
                                     ('Lluvioso',): {'Correr': 0.4, 'Nadar': 0.6}},
                       utilidad={'Correr': 10, 'Nadar': 15})  # Utilidades asociadas a cada valor posible de Actividad

    red_bayesiana = RedBayesianaDinamica([clima, actividad])  # Creación de la red bayesiana con los nodos definidos

    decisiones = [{'Clima': 'Soleado', 'Actividad': 'Correr', 'utilidad': 10},  # Lista de decisiones posibles
                  {'Clima': 'Soleado', 'Actividad': 'Nadar', 'utilidad': 15},
                  {'Clima': 'Lluvioso', 'Actividad': 'Correr', 'utilidad': 10},
                  {'Clima': 'Lluvioso', 'Actividad': 'Nadar', 'utilidad': 15}]

    utilidad_esperada = red_bayesiana.obtener_utilidad_esperada(decisiones)  # Cálculo de la utilidad esperada
    print("La utilidad esperada es:", utilidad_esperada)  # Imprime la utilidad esperada
