import numpy as np  # Importa la librería NumPy para operaciones numéricas
from collections import deque  # Importa la clase deque para una cola eficiente

# Definición de la clase del entorno
class Environment:
    def __init__(self, size_x, size_y, obstacles):
        self.size_x = size_x  # Tamaño del entorno en el eje X
        self.size_y = size_y  # Tamaño del entorno en el eje Y
        self.obstacles = obstacles  # Lista de coordenadas de obstáculos

    # Función para verificar si una coordenada está dentro del entorno y no está ocupada por un obstáculo
    def is_cell_free(self, coordinate):
        x, y = coordinate
        return 0 <= x < self.size_x and 0 <= y < self.size_y and (x, y) not in self.obstacles

# Función para encontrar un camino desde el punto de inicio hasta el punto de destino utilizando búsqueda en anchura
def find_path(environment, start, goal):
    # Inicialización
    visited = set()  # Conjunto de celdas visitadas
    queue = deque([(start, [])])  # Cola de celdas por visitar (cada elemento es una tupla (celda, camino))

    # Búsqueda en anchura
    while queue:
        current_cell, current_path = queue.popleft()  # Obtener la celda actual y el camino hasta ella
        if current_cell == goal:  # Si la celda actual es el destino, devolver el camino
            return current_path + [current_cell]
        if current_cell in visited:  # Si la celda ya ha sido visitada, pasar a la siguiente iteración
            continue
        visited.add(current_cell)  # Marcar la celda como visitada
        # Generar las coordenadas de las celdas adyacentes
        adjacent = [(current_cell[0] + dx, current_cell[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        # Filtrar las celdas adyacentes que están dentro del entorno y no están ocupadas por obstáculos
        free_adjacent = [c for c in adjacent if environment.is_cell_free(c)]
        # Agregar las celdas adyacentes a la cola con el camino actual más la celda adyacente
        for cell in free_adjacent:
            queue.append((cell, current_path + [cell]))

    # Si no se puede encontrar un camino, devolver None
    return None

# Definición del entorno (tamaño del entorno: 12x12, obstáculos en las celdas (3,4), (5,5) y (6,6))
environment = Environment(12, 12, [(3, 4), (5, 5), (6, 6)])

# Punto de inicio y destino
start_point = (2, 2)
goal_point = (10, 10)

# Encontrar un camino desde el punto de inicio hasta el punto de destino
path = find_path(environment, start_point, goal_point)

# Imprimir el camino encontrado
if path:
    print("Camino encontrado:", path)
else:
    print("No se pudo encontrar un camino.")
