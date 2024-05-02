import numpy as np

class FiltroParticulas:
    def __init__(self, num_particulas, limite_superior):
        # Inicializa el filtro de partículas con el número de partículas y el límite superior del espacio de estado
        self.num_particulas = num_particulas
        self.limite_superior = limite_superior
        # Inicializa las partículas de manera uniforme en el intervalo [0, limite_superior)
        self.particulas = np.random.uniform(0, limite_superior, num_particulas)
        # Inicializa los pesos de las partículas uniformemente
        self.weights = np.ones(num_particulas) / num_particulas

    def predecir(self, movimiento):
        # Predice el siguiente estado moviendo las partículas según el modelo de movimiento
        self.particulas += movimiento
        # Maneja el desbordamiento del límite superior del espacio de estado
        self.particulas %= self.limite_superior

    def actualizar(self, observacion, varianza_sensor):
        # Actualiza los pesos de las partículas basados en la observación y la varianza del sensor
        likelihoods = 1 / np.sqrt(2 * np.pi * varianza_sensor) * np.exp(-0.5 * ((observacion - self.particulas) ** 2) / varianza_sensor)
        self.weights *= likelihoods
        self.weights /= np.sum(self.weights)

        # Evita NaN en los pesos
        self.weights = np.nan_to_num(self.weights, nan=1.0)

    def reponderar(self):
        # Resamplea las partículas basándose en sus pesos
        indices = np.random.choice(np.arange(self.num_particulas), size=self.num_particulas, p=self.weights)
        self.particulas = self.particulas[indices]
        self.weights = np.ones(self.num_particulas) / self.num_particulas

    def estimar_estado(self):
        # Estima el estado utilizando la media de las partículas ponderadas por sus pesos
        estado_estimado = np.sum(self.particulas * self.weights)
        return estado_estimado

# Definir los parámetros del filtro de partículas
num_particulas = 500  # Nuevo número de partículas
limite_superior = 20  # Nuevo límite superior del espacio de estado
varianza_sensor = 0.02  # Nueva varianza del sensor

# Crear una instancia del filtro de partículas con los nuevos parámetros
filtro = FiltroParticulas(num_particulas, limite_superior)

# Generar movimientos y observaciones
movimientos = np.random.normal(0.7, 0.1, 100)  # Generar movimientos aleatorios
observaciones_verdaderas = np.sin(np.linspace(0, 2*np.pi, 100)) + np.random.normal(0, np.sqrt(varianza_sensor), 100)  # Generar observaciones ruidosas

# Actualizar el filtro de partículas y estimar el estado en cada paso de tiempo
for movimiento, observacion in zip(movimientos, observaciones_verdaderas):
    filtro.predecir(movimiento)  # Predicción del siguiente estado basada en el modelo de movimiento
    filtro.actualizar(observacion, varianza_sensor)  # Actualización basada en la observación actual
    filtro.reponderar()  # Resampleo de las partículas basado en los pesos actualizados
    estado_estimado = filtro.estimar_estado()  # Estimación del estado basada en las partículas y pesos
    print("Estado estimado:", estado_estimado)  # Imprimir la estimación del estado en cada paso de tiempo