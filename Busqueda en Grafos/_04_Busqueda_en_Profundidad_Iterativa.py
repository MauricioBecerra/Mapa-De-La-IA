def dfs_iterative(graph, start, Objetivo, Prof_max): #Se define la función de búsqueda en profundidad iterativa
    for depth_limit in range(1, Prof_max + 1): #Se itera sobre un rango de profundidades desde 1 hasta el máximo especificado
        result = dfs_limit(graph, start, Objetivo, depth_limit) # Se llama a la función de búsqueda en profundidad limitada con el límite de profundidad actual
        if result is not None: #Se verifica si se encontró un resultado
            return result #Se devuelve el resultado si se encontró un camino
    return None #Se devuelve None si no se encontró ningún camino después de iterar a través de todas las profundidades

def dfs_limit(graph, start, Objetivo, Prof_max): #Se define la función de búsqueda en profundidad limitada
    visitados = set() #Se inicializa un conjunto para llevar un registro de los nodos visitados
    stack = [(start, [start], 0)] #Se inicializa una pila con el nodo de inicio, el camino desde el inicio y la profundidad inicial
    while stack: #Se inicia un bucle que se ejecuta mientras la pila no esté vacía
        node, path, depth = stack.pop() #Se extrae el nodo, el camino y la profundidad del último elemento de la pila
        if node not in visitados: #Se verifica si el nodo no ha sido visitado
            if node == Objetivo: #Se verifica si el nodo es el objetivo
                return path #Se devuelve el camino si se alcanzó el objetivo
            if depth < Prof_max: #Se verifica si la profundidad actual es menor que la profundidad máxima permitida
                visitados.add(node) #Se añade el nodo al conjunto de visitados
                for vecinos in graph[node]: #Se itera sobre los vecinos del nodo actual
                    stack.append((vecinos, path + [vecinos], depth + 1)) #Se añaden los vecinos a la pila con el camino actualizado y la profundidad incrementada
    return None #Se devuelve None si no se encuentra un camino al objetivo dentro del límite de profundidad


graph = {
    'Jalisco': ['Nayarit', 'Zacatecas'], #Se define una lista de vecinos para el nodo 'Jalisco'
    'Nayarit': ['Jalisco', 'Durango', 'Sinaloa'], #Se define una lista de vecinos para el nodo 'Nayarit'
    'Zacatecas': ['Jalisco', 'Durango', 'Nuevo Leon', 'Coahuila'], #Se define una lista de vecinos para el nodo 'Zacatecas'
    'Durango': ['Zacatecas', 'Nayarit', 'Coahuila', 'Chihuahua', 'Sinaloa'], #Se define una lista de vecinos para el nodo 'Durango'
    'Coahuila': ['Zacatecas', 'Durango', 'Nuevo Leon', 'Chihuahua'], #Se define una lista de vecinos para el nodo 'Coahuila'
    'Nuevo Leon': ['Zacatecas', 'Coahuila'], #Se define una lista de vecinos para el nodo 'Nuevo Leon'
    'Chihuahua': ['Durango', 'Sinaloa', 'Coahuila', 'Sonora'], #Se define una lista de vecinos para el nodo 'Chihuahua'
    'Sinaloa': ['Nayarit', 'Durango', 'Sonora', 'Chihuahua'], #Se define una lista de vecinos para el nodo 'Sinaloa'
    'Sonora': ['Sinaloa', 'Chihuahua', 'Baja California'], #Se define una lista de vecinos para el nodo 'Sonora'
    'Baja California': ['Sonora'] #Se define una lista de vecinos para el nodo 'Baja California'
}

print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")#Se imprime un menu
est_inicio = input("Ingrese el estado de partida: ") #Se solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ") #Se solicita una entrada
prof_max = int(input("Ingrese profundidad maxima: ")) #Se solicita la profundidad maxima para cada iteracion

print("El camino encontrado es:", dfs_iterative(graph, est_inicio, est_objetivo,prof_max))
