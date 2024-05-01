import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas

class AgenteEpsilonGreedy:
    def __init__(self, num_acciones, epsilon=0.1):
        self.num_acciones = num_acciones  # Número de acciones disponibles para el agente
        self.epsilon = epsilon  # Valor de epsilon para la estrategia epsilon-greedy
        self.valores_accion = np.zeros(num_acciones)  # Inicializa los valores estimados de las acciones a cero
        self.contadores_accion = np.zeros(num_acciones)  # Inicializa los contadores de las acciones seleccionadas a cero

    def seleccionar_accion(self):
        if np.random.rand() < self.epsilon:  # Exploración: con probabilidad epsilon
            accion = np.random.randint(self.num_acciones)  # Se elige una acción aleatoria
        else:  # Explotación: con probabilidad 1-epsilon
            accion = np.argmax(self.valores_accion)  # Se elige la acción con el mayor valor estimado
        return accion

    def actualizar_valor_accion(self, accion, recompensa):
        self.contadores_accion[accion] += 1  # Incrementa el contador de la acción seleccionada
        # Actualiza el valor estimado de la acción mediante una media ponderada
        self.valores_accion[accion] += (recompensa - self.valores_accion[accion]) / self.contadores_accion[accion]

class BanditMultiBrazo:
    def __init__(self, num_acciones):
        self.num_acciones = num_acciones  # Número de acciones en el bandit multi-brazo
        # Valores reales de cada acción (extraídos de una distribución normal con media 0 y desviación estándar 1)
        self.valores_accion_real = np.random.normal(loc=0, scale=1, size=num_acciones)

    def obtener_recompensa(self, accion):
        # La recompensa es una muestra de una distribución normal con media igual al valor real de la acción
        return np.random.normal(loc=self.valores_accion_real[accion], scale=1)

num_acciones = 10  # Número de acciones en el bandit multi-brazo
num_pasos = 1000  # Número de pasos de interacción agente-entorno
epsilon = 0.1  # Parámetro epsilon para la estrategia epsilon-greedy

bandit = BanditMultiBrazo(num_acciones)  # Crear el bandit multi-brazo
agente = AgenteEpsilonGreedy(num_acciones, epsilon)  # Crear el agente epsilon-greedy

recompensa_total = 0  # Inicializar la recompensa total acumulada

# Iterar sobre los pasos de interacción agente-entorno
for _ in range(num_pasos):
    accion = agente.seleccionar_accion()  # El agente selecciona una acción
    recompensa = bandit.obtener_recompensa(accion)  # El entorno devuelve la recompensa para la acción seleccionada
    agente.actualizar_valor_accion(accion, recompensa)  # El agente actualiza su estimación del valor de la acción
    recompensa_total += recompensa  # Se acumula la recompensa obtenida

print("Recompensa total obtenida:", recompensa_total)  # Imprimir la recompensa total obtenida
