import heapq

grafo = { # Se estable el grafo
    'Jalisco': {'Nayarit': 14, 'Zacatecas': 7},
    'Nayarit': {'Jalisco': 11, 'Durango': 10, 'Sinaloa': 1},
    'Zacatecas': {'Jalisco': 5, 'Durango': 2, 'Nuevo Leon': 14, 'Coahuila': 3},
    'Durango': {'Zacatecas': 8, 'Nayarit': 4, 'Coahuila': 15, 'Chihuahua': 6, 'Sinaloa': 12},
    'Coahuila': {'Zacatecas': 9, 'Durango': 13, 'Nuevo Leon': 1, 'Chihuahua': 7},
    'Nuevo Leon': {'Zacatecas': 10, 'Coahuila': 11},
    'Chihuahua': {'Durango': 14, 'Sinaloa': 8, 'Coahuila': 5, 'Sonora': 3},
    'Sinaloa': {'Nayarit': 13, 'Durango': 7, 'Sonora': 9, 'Chihuahua': 15},
    'Sonora': {'Sinaloa': 9, 'Chihuahua': 15, 'Baja California': 10},
    'Baja California': {'Sonora': 2}
}

def busqueda_ao_estrella(grafo, inicio, objetivo, alpha):
    frontera = [] # Creamos una lista vacía que contendrá las fronteras
    heapq.heappush(frontera, (0, inicio, [inicio])) # Añadimos a la frontera una tupla con el costo cero, el nodo de inicio y una lista que contiene solo el nodo de inicio

    visitados = set() # Creamos un conjunto vacío para mantener los nodos visitados

    while frontera: # Mientras haya nodos en la frontera:
        costo_actual, nodo_actual, camino_actual = heapq.heappop(frontera) # Extraemos de la frontera el nodo con el menor costo actual, junto con su costo actual y su camino hasta el momento

        if nodo_actual == objetivo: # Si el nodo actual es igual al objetivo:
            return camino_actual # Retornamos el camino actual, hemos encontrado el objetivo

        visitados.add(nodo_actual) # Añadimos el nodo actual a los nodos visitados

        for vecino, costo in grafo[nodo_actual].items(): # Para cada vecino del nodo actual y su costo:
            if vecino not in visitados: # Si el vecino no está en los nodos visitados:
                nuevo_camino = list(camino_actual) # Creamos una nueva lista de camino basada en el camino actual
                nuevo_camino.append(vecino) # Añadimos el vecino al nuevo camino
                costo_total = costo_actual + costo + alpha * heuristica(vecino, objetivo) # Calculamos el costo total del nuevo camino, que incluye el costo actual, el costo del vecino y una heurística ponderada por alpha
                heapq.heappush(frontera, (costo_total, vecino, nuevo_camino)) # Añadimos el nuevo camino a la frontera con su costo total

    return None # Si no se encuentra el objetivo, retornamos None


def heuristica(nodo_actual, nodo_objetivo):
    coordenadas = { # Se establecen las cordenadas.
    'Jalisco': (38, 63),
    'Nayarit': (75, 80),
    'Zacatecas': (72, 2),
    'Durango': (94, 36),
    'Coahuila': (57, 96),
    'Nuevo Leon': (75, 8),
    'Chihuahua': (80, 56),
    'Sinaloa': (98, 50),
    'Sonora': (83, 5),
    'Baja California': (93, 82)
    }
    x1, y1 = coordenadas[nodo_actual]  # Obtiene las coordenadas 'x' e 'y' del nodo actual
    x2, y2 = coordenadas[nodo_objetivo]  # Obtiene las coordenadas 'x' e 'y' del nodo objetivo
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  #Retorna la distancia euclidiana entre el nodo actual y el nodo objetivo

print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")# Se imprime un menu
est_inicio = input("Ingrese el estado de partida: ") # Se solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ") # Se solicita una entrada
factor = float(input("Ingrese el factor de adaptación heurística: ")) # Se solicita el factor
ruta = busqueda_ao_estrella(grafo, est_inicio, est_objetivo, factor) # Se llama a la funcion de busqueda
if ruta: # Si la ruta es verdadera imprimos la ruta
    print(f"Se encontró un ruta de {est_inicio} a {est_objetivo}: {' -> '.join(ruta)}") #Se imprime un mensaje mostrando la ruta
else:
    print(f"No se encontró un ruta de {est_inicio} a {est_objetivo}.")# Si no se encuentra la ruta imprime el msg

