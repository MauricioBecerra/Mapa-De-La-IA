import random  # Importa el módulo random para generar números aleatorios

def obtener_recompensa(accion):
    if accion == 'X':
        return random.choice([1, -1])  # Devuelve una recompensa aleatoria positiva o negativa para la acción 'X'
    elif accion == 'Y':
        return random.choice([-1, 1])  # Devuelve una recompensa aleatoria positiva o negativa para la acción 'Y'

valores_Q = {'X': 0, 'Y': 0}  # Inicializa los valores Q para cada acción en 0
epsilon = 0.1  # Factor de exploración epsilon
alfa = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
num_episodios = 1000  # Número de episodios de entrenamiento

# Entrenamiento del agente
for _ in range(num_episodios):  # Bucle a través de cada episodio
    # Elegir una acción
    if random.random() < epsilon:
        accion = random.choice(['X', 'Y'])  # Explorar: elige una acción al azar con probabilidad epsilon
    else:
        accion = max(valores_Q, key=valores_Q.get)  # Explotar: elige la acción con el mayor valor Q
    
    # Obtener la recompensa
    recompensa = obtener_recompensa(accion)  # Obtiene la recompensa para la acción elegida
    
    # Actualizar el valor Q
    valores_Q[accion] = valores_Q[accion] + alfa * (recompensa - valores_Q[accion])  # Actualiza el valor Q utilizando la fórmula de Q-learning

# Probar el agente entrenado
recompensa_total = 0
for _ in range(100):  # Realizar 100 pruebas
    accion = max(valores_Q, key=valores_Q.get)  # Elige la acción con el mayor valor Q
    recompensa = obtener_recompensa(accion)  # Obtiene la recompensa para la acción elegida
    recompensa_total += recompensa  # Acumula la recompensa

print(f"Recompensa promedio: {recompensa_total / 100}")  # Imprime la recompensa promedio
