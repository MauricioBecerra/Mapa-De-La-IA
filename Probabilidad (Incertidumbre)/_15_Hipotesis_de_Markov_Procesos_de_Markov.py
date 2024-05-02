import numpy as np

# Definición de una clase para una cadena de Markov
class MarkovChain:
    # Método de inicialización de la clase
    def __init__(self, transition_matrix, states):
        # Inicializa la matriz de transición y los estados
        self.transition_matrix = transition_matrix
        self.states = states
        # Calcula el número de estados
        self.num_states = len(states)

    # Método para obtener el próximo estado dado el estado actual
    def next_state(self, current_state):
        # Selecciona aleatoriamente el próximo estado según la matriz de transición
        return np.random.choice(self.states, p=self.transition_matrix[current_state])

    # Método para generar una secuencia de estados a partir de un estado inicial
    def generate_states(self, start_state, num_steps):
        # Inicializa el estado actual con el estado inicial
        current_state = start_state
        # Inicializa una lista para almacenar la secuencia de estados
        states_sequence = [current_state]
        # Itera sobre el número de pasos especificado
        for _ in range(num_steps - 1):
            # Obtiene el próximo estado y lo agrega a la secuencia
            current_state = self.next_state(current_state)
            states_sequence.append(current_state)
        # Devuelve la secuencia de estados generada
        return states_sequence

# Nueva matriz de transición con probabilidades alteradas
transition_matrix = np.array([[0.8, 0.2], [0.2, 0.8]])
states = [0, 1] 

# Crear una instancia de la clase MarkovChain con la nueva matriz de transición y estados
markov_chain = MarkovChain(transition_matrix, states)

start_state = 1  # Estado inicial cambiado a 1
num_steps = 15  # Número de pasos incrementado a 15
states_sequence = markov_chain.generate_states(start_state, num_steps)

print("Secuencia de estados generada por la cadena de Markov:")
print(states_sequence)
