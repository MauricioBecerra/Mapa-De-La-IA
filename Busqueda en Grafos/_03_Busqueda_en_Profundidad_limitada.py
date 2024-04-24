def dfs_limit(graph, start, objetivo, prof_max):
    visitados = set() #Se crea un conjunto para mantener un registro de los nodos visitados
    stack = [(start, [start], 0)] #Se inicializa una pila con una tupla que contiene el nodo de inicio y el camino desde el inicio
    while stack: #Se inicia un bucle que se ejecuta mientras la pila no esté vacía
        node, path, depth = stack.pop() #Se extrae el último elemento de la pila, que contiene el nodo actual, el camino y la profundidad
        if node not in visitados: #Se verifica si el nodo actual no ha sido visitado
            if node == objetivo: #Se verifica si el nodo actual es el objetivo
                return path #Se devuelve el camino actual si se ha alcanzado el objetivo
            if depth < prof_max: #Se verifica si la profundidad actual es menor que la profundidad máxima permitida
                visitados.add(node) #Se añade el nodo actual al conjunto de visitados
                for vecinos in graph[node]: #Se itera sobre los vecinos del nodo actual
                    stack.append((vecinos, path + [vecinos], depth + 1)) # Se añaden los vecinos a la pila con el camino actualizado y la profundidad incrementada
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
prof_max = int(input("Ingrese profundidad maxima: ")) #Se solicita la profundidad maxima
print("El camino encontrado es:", dfs_limit(graph, est_inicio, est_objetivo,prof_max)) #Se imprime la ruta despues de llamar la funcion dfs