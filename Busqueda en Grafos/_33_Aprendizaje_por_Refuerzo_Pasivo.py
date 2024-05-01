import numpy as np  # Importa la librería NumPy

class AgenteAPR:
    def __init__(self, num_acciones, valor_inicial=0):
        # Inicializa un Agente de Aprendizaje por Refuerzo Pasivo (APR).
        self.num_acciones = num_acciones  # Número de acciones disponibles para el agente
        self.valor_estimado = np.full(num_acciones, valor_inicial, dtype=float)    # Valores estimados iniciales
        self.contador_acciones = np.zeros(num_acciones)  # Contador de veces que se ha seleccionado cada acción

    def seleccionar_accion(self):
        # Selecciona una acción basada en los valores estimados actuales.
        return np.argmax(self.valor_estimado)

    def actualizar_valor_estimado(self, accion, recompensa):
        # Actualiza el valor estimado de una acción basada en la recompensa recibida.
        self.contador_acciones[accion] += 1  # Actualizar el contador de veces que se ha seleccionado la acción
        n = self.contador_acciones[accion]  # Número de veces que se ha seleccionado la acción
        valor_antiguo = self.valor_estimado[accion]  # Valor estimado anterior de la acción
        # Actualizar el valor estimado de la acción utilizando la regla incremental
        self.valor_estimado[accion] = valor_antiguo + (1/n) * (recompensa - valor_antiguo)

def main():
    num_acciones = 10  # Número de acciones disponibles para el agente
    num_iteraciones = 10000  # Número de iteraciones o pasos de tiempo

    # Crear un agente de aprendizaje por refuerzo pasivo
    agente = AgenteAPR(num_acciones)

    for i in range(num_iteraciones):
        # El agente selecciona una acción
        accion_elegida = agente.seleccionar_accion()
        
        # Simular una recompensa para la acción seleccionada (en este ejemplo, una recompensa aleatoria)
        recompensa = np.random.normal(loc=0, scale=1)
        
        # Actualizar los valores estimados del agente basados en la recompensa recibida
        agente.actualizar_valor_estimado(accion_elegida, recompensa)

    # Imprimir los valores estimados finales del agente
    print("Valores estimados finales:")
    print(agente.valor_estimado)

if __name__ == "__main__":
    main()
