import numpy as np  # Importa la librería numpy para operaciones matemáticas

class POMDP:  # Define una clase para el POMDP
    def __init__(self, estados, acciones, observaciones, probabilidades_transicion, probabilidades_observacion, recompensas, factor_descuento):
        # Constructor de la clase POMDP
        self.estados = estados  # Define los estados posibles
        self.acciones = acciones  # Define las acciones posibles
        self.observaciones = observaciones  # Define las observaciones posibles
        self.probabilidades_transicion = probabilidades_transicion  # Define las probabilidades de transición
        self.probabilidades_observacion = probabilidades_observacion  # Define las probabilidades de observación
        self.recompensas = recompensas  # Define las recompensas
        self.factor_descuento = factor_descuento  # Define el factor de descuento

    def iteracion_valor(self, epsilon=0.01):
        # Método para realizar la iteración de valor y encontrar la política óptima
        V = {s: 0 for s in self.estados}  # Inicializa la función de valor V

        while True:
            delta = 0  # Inicializa el cambio en la función de valor
            for s in self.estados:  # Itera sobre todos los estados posibles
                v = V[s]  # Almacena el valor actual de V[s]
                # Calcula el nuevo valor de V[s] como el máximo valor Q(s, a) para todas las acciones a
                V[s] = max([self.calcular_valor_q(s, a, V) for a in self.acciones])
                # Actualiza delta al máximo cambio en V[s] en esta iteración
                delta = max(delta, abs(v - V[s]))
            # Si el cambio en V[s] es menor que epsilon, se considera que ha convergido y se termina el bucle
            if delta < epsilon:
                break

        # Una vez convergido, extrae la política óptima
        politica = {}
        for s in self.estados:
            # Para cada estado, selecciona la acción que maximiza Q(s, a) como la acción óptima
            politica[s] = max(self.acciones, key=lambda a: self.calcular_valor_q(s, a, V))
        
        return V, politica

    def calcular_valor_q(self, estado, accion, V):
        # Calcula el valor Q(s, a) para un estado y una acción dados
        valor_q = sum([
            # Suma sobre todos los posibles estados siguientes
            self.probabilidades_transicion[estado][accion][siguiente_estado] *
            (self.recompensas[estado][accion][siguiente_estado] +
            self.factor_descuento * V[siguiente_estado])
            for siguiente_estado in self.estados  # Para cada estado siguiente en los estados posibles
        ])
        return valor_q

    def observar(self, estado, accion, observacion):
        # Calcula la creencia posterior basada en la observación
        creencia = {}
        for siguiente_estado in self.estados:  # Para cada estado siguiente en los estados posibles
            # Calcula la creencia como la suma ponderada de la creencia anterior y la probabilidad de transición y observación
            creencia[siguiente_estado] = sum([
                self.probabilidades_transicion[estado][accion][siguiente_estado] *
                self.probabilidades_observacion[accion][siguiente_estado][observacion] *
                (self.recompensas[estado][accion][siguiente_estado] +
                self.factor_descuento * V[siguiente_estado])
                for estado in self.estados  # Para cada estado en los estados posibles
            ])
        return creencia

# Definición de los estados, acciones, observaciones, probabilidades y recompensas
estados = ['A', 'B', 'C']  # Estados posibles del robot en el laberinto
acciones = ['Norte', 'Sur', 'Este', 'Oeste']  # Acciones posibles del robot
observaciones = ['Pared', 'Camino']  # Observaciones posibles del robot
probabilidades_transicion = {
    'A': {  # Transiciones posibles desde el estado A
        'Norte': {'A': 0.8, 'B': 0.1, 'C': 0.1},  # Probabilidades de ir al estado A, B o C después de tomar la acción Norte
        'Sur': {'A': 0.1, 'B': 0.8, 'C': 0.1},   # Probabilidades de ir al estado A, B o C después de tomar la acción Sur
        'Este': {'A': 0.1, 'B': 0.8, 'C': 0.1},  # Probabilidades de ir al estado A, B o C después de tomar la acción Este
        'Oeste': {'A': 0.1, 'B': 0.1, 'C': 0.8}  # Probabilidades de ir al estado A, B o C después de tomar la acción Oeste
    },
    'B': {  # Transiciones posibles desde el estado B
        'Norte': {'A': 0.1, 'B': 0.8, 'C': 0.1},  # Probabilidades de ir al estado A, B o C después de tomar la acción Norte
        'Sur': {'A': 0.8, 'B': 0.1, 'C': 0.1},   # Probabilidades de ir al estado A, B o C después de tomar la acción Sur
        'Este': {'A': 0.1, 'B': 0.1, 'C': 0.8},  # Probabilidades de ir al estado A, B o C después de tomar la acción Este
        'Oeste': {'A': 0.8, 'B': 0.1, 'C': 0.1}  # Probabilidades de ir al estado A, B o C después de tomar la acción Oeste
    },
    'C': {  # Transiciones posibles desde el estado C
        'Norte': {'A': 0.1, 'B': 0.1, 'C': 0.8},  # Probabilidades de ir al estado A, B o C después de tomar la acción Norte
        'Sur': {'A': 0.1, 'B': 0.1, 'C': 0.8},   # Probabilidades de ir al estado A, B o C después de tomar la acción Sur
        'Este': {'A': 0.8, 'B': 0.1, 'C': 0.1},  # Probabilidades de ir al estado A, B o C después de tomar la acción Este
        'Oeste': {'A': 0.1, 'B': 0.8, 'C': 0.1}  # Probabilidades de ir al estado A, B o C después de tomar la acción Oeste
    }
}
probabilidades_observacion = {
    'Norte': {  # Probabilidades de observación al tomar la acción Norte
        'A': {'Pared': 0.8, 'Camino': 0.2},  # Probabilidades de observar Pared o Camino si se está en el estado A
        'B': {'Pared': 0.2, 'Camino': 0.8},  # Probabilidades de observar Pared o Camino si se está en el estado B
        'C': {'Pared': 0.8, 'Camino': 0.2}   # Probabilidades de observar Pared o Camino si se está en el estado C
    },
    'Sur': {  # Probabilidades de observación al tomar la acción Sur
        'A': {'Pared': 0.2, 'Camino': 0.8},  # Probabilidades de observar Pared o Camino si se está en el estado A
        'B': {'Pared': 0.8, 'Camino': 0.2},  # Probabilidades de observar Pared o Camino si se está en el estado B
        'C': {'Pared': 0.8, 'Camino': 0.2}   # Probabilidades de observar Pared o Camino si se está en el estado C
    },
    'Este': {  # Probabilidades de observación al tomar la acción Este
        'A': {'Pared': 0.2, 'Camino': 0.8},  # Probabilidades de observar Pared o Camino si se está en el estado A
        'B': {'Pared': 0.2, 'Camino': 0.8},  # Probabilidades de observar Pared o Camino si se está en el estado B
        'C': {'Pared': 0.8, 'Camino': 0.2}   # Probabilidades de observar Pared o Camino si se está en el estado C
    },
    'Oeste': {  # Probabilidades de observación al tomar la acción Oeste
        'A': {'Pared': 0.8, 'Camino': 0.2},  # Probabilidades de observar Pared o Camino si se está en el estado A
        'B': {'Pared': 0.2, 'Camino': 0.8},  # Probabilidades de observar Pared o Camino si se está en el estado B
        'C': {'Pared': 0.2, 'Camino': 0.8}   # Probabilidades de observar Pared o Camino si se está en el estado C
    }
}
recompensas = {
    'A': {  # Recompensas asociadas al estado A
        'Norte': {'A': 0, 'B': 10, 'C': 0},  # Recompensas al tomar la acción Norte desde el estado A
        'Sur': {'A': 10, 'B': 0, 'C': 0},   # Recompensas al tomar la acción Sur desde el estado A
        'Este': {'A': 0, 'B': 0, 'C': 0},   # Recompensas al tomar la acción Este desde el estado A
        'Oeste': {'A': 0, 'B': 0, 'C': 0}   # Recompensas al tomar la acción Oeste desde el estado A
    },
    'B': {  # Recompensas asociadas al estado B
        'Norte': {'A': 0, 'B': 0, 'C': 0},   # Recompensas al tomar la acción Norte desde el estado B
        'Sur': {'A': 0, 'B': 10, 'C': 0},    # Recompensas al tomar la acción Sur desde el estado B
        'Este': {'A': 0, 'B': 0, 'C': 0},    # Recompensas al tomar la acción Este desde el estado B
        'Oeste': {'A': 0, 'B': 0, 'C': 0}    # Recompensas al tomar la acción Oeste desde el estado B
    },
    'C': {  # Recompensas asociadas al estado C
        'Norte': {'A': 0, 'B': 0, 'C': 0},   # Recompensas al tomar la acción Norte desde el estado C
        'Sur': {'A': 0, 'B': 0, 'C': 10},    # Recompensas al tomar la acción Sur desde el estado C
        'Este': {'A': 0, 'B': 0, 'C': 0},    # Recompensas al tomar la acción Este desde el estado C
        'Oeste': {'A': 0, 'B': 0, 'C': 0}    # Recompensas al tomar la acción Oeste desde el estado C
    }
}
factor_descuento = 0.9  # Factor de descuento para las recompensas futuras

# Instancia de POMDP con los parámetros definidos
pomdp = POMDP(estados, acciones, observaciones, probabilidades_transicion, probabilidades_observacion, recompensas, factor_descuento)

# Realiza la iteración de valor para encontrar la política óptima y la función de valor
funcion_valor, politica = pomdp.iteracion_valor()

# Imprime la política óptima
print("Política Óptima:")
print(politica)