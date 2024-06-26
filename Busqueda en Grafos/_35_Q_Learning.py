import numpy as np  # Importa la biblioteca NumPy para cálculos numéricos

class QLearning:
    def __init__(self, num_estados, num_acciones, tasa_aprendizaje=0.1, factor_descuento=0.9, tasa_exploracion=0.1):
        # Inicialización de la clase QLearning
        self.num_estados = num_estados  # Número de estados en el entorno
        self.num_acciones = num_acciones  # Número de acciones disponibles para el agente
        self.tasa_aprendizaje = tasa_aprendizaje  # Tasa de aprendizaje (alfa)
        self.factor_descuento = factor_descuento  # Factor de descuento (gamma)
        self.tasa_exploracion = tasa_exploracion  # Tasa de exploración (epsilon)
        # Crear tabla Q inicializada con ceros
        self.tabla_q = np.zeros((num_estados, num_acciones))

    def elegir_accion(self, estado):
        # Selección de acción basada en la política epsilon-greedy
        if np.random.uniform(0, 1) < self.tasa_exploracion:
            # Acción aleatoria (exploración)
            return np.random.choice(self.num_acciones)
        else:
            # Acción según la política greedy (explotación)
            return np.argmax(self.tabla_q[estado, :])

    def actualizar_tabla_q(self, estado, accion, recompensa, proximo_estado):
        # Actualización de la tabla Q según la regla de actualización de Q-learning
        valor_q_actual = self.tabla_q[estado, accion]  # Valor Q(s,a) actual
        mejor_proximo_valor_q = np.max(self.tabla_q[proximo_estado, :])  # Max Q(s',a')
        nuevo_valor_q = valor_q_actual + self.tasa_aprendizaje * (recompensa + self.factor_descuento * mejor_proximo_valor_q - valor_q_actual)
        # Actualización del valor Q para el par estado-acción
        self.tabla_q[estado, accion] = nuevo_valor_q

def main():
    num_estados = 5  # Número total de estados
    num_acciones = 3  # Número total de acciones posibles
    estado_meta = 4  # Estado objetivo
    obstaculos = [2]  # Lista de estados considerados como obstáculos

    q_learning = QLearning(num_estados, num_acciones)  # Creación de una instancia de Q-Learning

    num_episodios = 1000  # Número de episodios de entrenamiento
    for episodio in range(num_episodios):
        estado = 0  # Estado inicial
        terminado = False
        while not terminado:
            accion = q_learning.elegir_accion(estado)  # Selección de acción
            if estado == estado_meta:
                recompensa = 1  # Recompensa por alcanzar el estado objetivo
                proximo_estado = estado
                terminado = True
            elif estado in obstaculos:
                recompensa = -1  # Penalización por estar en un obstáculo
                proximo_estado = estado
                terminado = True
            else:
                recompensa = 0
                proximo_estado = estado + 1  # Avance hacia adelante en la cuadrícula

            # Actualización de la tabla Q
            q_learning.actualizar_tabla_q(estado, accion, recompensa, proximo_estado)

            estado = proximo_estado

    # Impresión de la tabla Q aprendida
    print("La Tabla Q es: ")
    print(q_learning.tabla_q)

if __name__ == "__main__":
    main()