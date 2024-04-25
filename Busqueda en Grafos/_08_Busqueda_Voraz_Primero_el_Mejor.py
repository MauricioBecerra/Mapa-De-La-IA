import heapq
#Se crea el grafo
grafo = {
    
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

def busqueda_voraz(grafo, inicio, objetivo):
    frontera = []
    heapq.heappush(frontera, (0, [inicio]))
    visitados = set()

    while frontera:
        _, camino_actual = heapq.heappop(frontera)
        nodo_actual = camino_actual[-1]

        if nodo_actual == objetivo:
            return camino_actual

        visitados.add(nodo_actual)

        for vecino, _ in grafo[nodo_actual].items():
            if vecino not in visitados:
                nuevo_camino = list(camino_actual)
                nuevo_camino.append(vecino)
                valor_heuristico = distancia_euclidiana(vecino, objetivo)
                heapq.heappush(frontera, (valor_heuristico, nuevo_camino))

    return None

def distancia_euclidiana(nodo_actual, nodo_objetivo):
    coordenadas = {
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

    x1, y1 = coordenadas[nodo_actual]
    x2, y2 = coordenadas[nodo_objetivo]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")#Se imprime un menu
est_inicio = input("Ingrese el estado de partida: ") #Se solicita una entrada
est_objetivo = input("Ingrese el estado est_objetivo: ") #Se solicita una entrada
ruta = busqueda_voraz(grafo, est_inicio, est_objetivo) #se llama a la funcion de busqueda
if ruta: #Si la ruta es verdadera imprimos la ruta
    print(f"Se encontró un ruta de {est_inicio} a {est_objetivo}: {' -> '.join(ruta)}")
else:
    print(f"No se encontró un ruta de {est_inicio} a {est_objetivo}.")#Si no se encuentra la ruta imprime el msg
