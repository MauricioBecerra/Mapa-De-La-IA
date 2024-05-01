import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas

class BusquedaPolitica():
    def __init__(self, n_estados, n_acciones, gamma=0.95, theta=1e-4):
        # Inicializa el objeto BusquedaPolitica con los parámetros dados
        self.n_estados = n_estados  # Número de estados en el modelo
        self.n_acciones = n_acciones  # Número de acciones posibles
        self.gamma = gamma  # Factor de descuento para futuras recompensas
        self.theta = theta  # Umbral de convergencia para detener la iteración
        self.V = np.zeros(n_estados)  # Inicializa el vector de valores de los estados con ceros

    def encontrar_politica(self, modelo_transiciones, recompensas):
        # Método para encontrar la política óptima basada en el algoritmo de iteración de valor
        while True:
            delta = 0  # Inicializa el cambio en los valores de los estados
            # Itera sobre todos los estados
            for s in range(self.n_estados):
                v = self.V[s]  # Almacena el valor actual del estado
                # Calcula el nuevo valor del estado como el máximo de los valores futuros
                self.V[s] = max([sum([p * (recompensas[s][a] + self.gamma * self.V[s1]) for (p, s1) in modelo_transiciones[s][a]]) for a in range(self.n_acciones)])
                # Calcula la diferencia de valores para verificar la convergencia
                delta = max(delta, abs(v - self.V[s]))
            # Comprueba si se ha alcanzado la convergencia
            if delta < self.theta:
                break

        # Construye la política óptima basada en los valores de los estados
        politica = np.zeros(self.n_estados, dtype=int)
        for s in range(self.n_estados):
            # Para cada estado, elige la acción que maximiza el valor esperado
            politica[s] = np.argmax([sum([p * (recompensas[s][a] + self.gamma * self.V[s1]) for (p, s1) in modelo_transiciones[s][a]]) for a in range(self.n_acciones)])

        return politica

# Ejemplo de uso
if __name__ == "__main__":
    n_estados = 4  # Número de estados
    n_acciones = 3  # Número de acciones

    # Modelo de transiciones: especifica las probabilidades de transición y los estados alcanzables dado un estado-acción
    modelo_transiciones = [
        # Transiciones desde el estado 0
        [[(0.85, 0), (0.15, 1)],  
         [(0.05, 0), (0.95, 1)], 
         [(0.2, 0), (0.8, 3)]], 
        # Transiciones desde el estado 1
        [[(0.75, 0), (0.25, 2)],  
         [(0.6, 0), (0.4, 2)], 
         [(0.3, 1), (0.7, 3)]],
        # Transiciones desde el estado 2
        [[(0.65, 2), (0.35, 2)],  
         [(0.1, 0), (0.9, 2)], 
         [(0.5, 1), (0.5, 3)]],
        # Transiciones desde el estado 3
        [[(0.55, 3), (0.45, 3)],  
         [(0.25, 0), (0.75, 3)], 
         [(0.4, 1), (0.6, 2)]]
    ]

    # Recompensas: especifica las recompensas asociadas a cada estado-acción
    recompensas = [
        [-1, 1, 0],  # Recompensas para el estado 0
        [-2, -1, 1], # Recompensas para el estado 1
        [0, 1, -1],  # Recompensas para el estado 2
        [1, 0, -1]   # Recompensas para el estado 3
    ]

    # Crear instancia de la clase BusquedaPolitica
    busqueda_politica = BusquedaPolitica(n_estados, n_acciones)

    # Encontrar la política óptima
    politica_optima = busqueda_politica.encontrar_politica(modelo_transiciones, recompensas)

    # Imprimir la política óptima encontrada
    print("Política óptima encontrada:", politica_optima)
