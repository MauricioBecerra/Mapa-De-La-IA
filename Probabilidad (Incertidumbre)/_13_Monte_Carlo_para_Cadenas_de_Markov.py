import random

# Definimos una matriz de transición modificada con probabilidades desiguales
transition_matrix = [[0.3, 0.7], [0.6, 0.4]]

# Función para realizar una transición en la cadena de Markov
def transition(current_state):
    next_state = random.choices([0, 1], weights=transition_matrix[current_state])[0]
    return next_state

# Función de densidad de probabilidad modificada con valores desiguales
def pdf(state):
    return 0.3 if state == 0 else 0.7

# Función de Monte Carlo para generar muestras de la cadena de Markov
def monte_carlo_mcmc(num_samples):
    current_state = random.choice([0, 1])  # Seleccionamos un estado inicial aleatorio
    samples = []
    for _ in range(num_samples):
        proposed_state = transition(current_state)  # Realizamos una transición propuesta
        acceptance_ratio = pdf(proposed_state) / pdf(current_state)  # Calculamos la razón de aceptación
        if random.random() < acceptance_ratio:  # Comprobamos si se acepta la transición
            current_state = proposed_state  # Actualizamos el estado actual
        samples.append(current_state)  # Agregamos el estado actual a las muestras
    return samples

num_samples = 500  # Número de muestras reducido para el ejemplo

samples = monte_carlo_mcmc(num_samples)

print("Algunas muestras generadas:", samples[:10])  # Imprimimos algunas muestras generadas