def dfs(graph, start, objetivo): # Se inicia función dfs con 3 parámetros: grafo, inicio y objetivo
    visitados = set() # Se crea un conjunto para mantener un registro de los nodos visitados
    stack = [(start, [start])] # Se inicializa una pila con una tupla que contiene el nodo de inicio y el camino desde el inicio
    while stack: #Se inicia un bucle que se ejecuta mientras la pila no esté vacía
        (node, path) = stack.pop() # Se extrae el último elemento de la pila, que es una tupla con el nodo actual y el camino
        if node not in visitados: # Se verifica si el nodo actual no ha sido visitado
            if node == objetivo: # Se verifica si el nodo actual es el objetivo
                return path # Se devuelve el camino actual si se ha alcanzado el objetivo
            visitados.add(node) # Se añade el nodo actual al conjunto de visitados
            for vecinos in graph[node]: # Se itera sobre los vecinos del nodo actual
                stack.append((vecinos, path + [vecinos])) # Se añaden los vecinos a la pila con el camino actualizado
    return None # Se devuelve None si no se encuentra un camino al objetivo

graph = {
    'Jalisco': ['Nayarit', 'Zacatecas'], # Se define una lista de vecinos para el nodo 'Jalisco'
    'Nayarit': ['Jalisco', 'Durango', 'Sinaloa'], # Se define una lista de vecinos para el nodo 'Nayarit'
    'Zacatecas': ['Jalisco', 'Durango', 'Nuevo Leon', 'Coahuila'], # Se define una lista de vecinos para el nodo 'Zacatecas'
    'Durango': ['Zacatecas', 'Nayarit', 'Coahuila', 'Chihuahua', 'Sinaloa'], # Se define una lista de vecinos para el nodo 'Durango'
    'Coahuila': ['Zacatecas', 'Durango', 'Nuevo Leon', 'Chihuahua'], # Se define una lista de vecinos para el nodo 'Coahuila'
    'Nuevo Leon': ['Zacatecas', 'Coahuila'], # Se define una lista de vecinos para el nodo 'Nuevo Leon'
    'Chihuahua': ['Durango', 'Sinaloa', 'Coahuila', 'Sonora'], # Se define una lista de vecinos para el nodo 'Chihuahua'
    'Sinaloa': ['Nayarit', 'Durango', 'Sonora', 'Chihuahua'], # Se define una lista de vecinos para el nodo 'Sinaloa'
    'Sonora': ['Sinaloa', 'Chihuahua', 'Baja California'], # Se define una lista de vecinos para el nodo 'Sonora'
    'Baja California': ['Sonora'] # Se define una lista de vecinos para el nodo 'Baja California'
}


print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")#imprime un menu
est_inicio = input("Ingrese el estado de partida: ") #solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ") #solicita una entrada
print("El camino encontrado es::", dfs(graph, est_inicio, est_objetivo)) #imprime la ruta despues de llamar la funcion dfs