import numpy as np  # Importa el módulo numpy y lo renombra como np

distancias = np.array([[0, 1, 3, 0, 1],  # Crea una matriz numpy que representa las distancias entre puntos
                       [2, 0, 5, 0, 4],  # Las distancias están dispuestas en una matriz bidimensional
                       [0, 3, 0, 1, 0],  # Cada fila representa las distancias desde un punto de origen
                       [0, 2, 0, 0, 5],  # Cada columna representa las distancias hacia un punto de destino
                       [4, 0, 0, 1, 0]]) 

def distancia_total(ruta, distancias):  # Define una función para calcular la distancia total de una ruta
    distancia = 0  # Inicializa la distancia en 0
    for i in range(len(ruta) - 1):  # Itera sobre la longitud de la ruta
        distancia += distancias[ruta[i]][ruta[i+1]]  # Suma la distancia entre los puntos consecutivos de la ruta
    return distancia  # Retorna la distancia total de la ruta

def temple_simulado_busqueda_ruta(distancias, punto_inicio, punto_destino, temperatura_inicial, factor_enfriamiento, max_iter):  # Define la función para la búsqueda de ruta utilizando el algoritmo de Temple Simulado
    mejor_ruta = [punto_inicio]  # Inicializa la mejor ruta con el punto de inicio
    mejor_distancia = distancias[punto_inicio][punto_destino]  # Calcula la mejor distancia inicial
    ruta_actual = mejor_ruta  # Inicializa la ruta actual como la mejor ruta
    distancia_actual = mejor_distancia  # Inicializa la distancia actual como la mejor distancia
    temperatura_actual = temperatura_inicial  # Inicializa la temperatura actual con la temperatura inicial
    
    for _ in range(max_iter):  # Realiza un número máximo de iteraciones
        intersecciones = list(range(1, len(distancias) - 1))  # Crea una lista de intersecciones (excluyendo el punto de inicio y destino)
        np.random.shuffle(intersecciones)  # Mezcla aleatoriamente las intersecciones
        
        ruta_vecina = [punto_inicio] + intersecciones + [punto_destino]  # Construye una ruta vecina que comienza con el punto de inicio, seguido de las intersecciones y termina en el punto de destino
        
        distancia_vecina = distancia_total(ruta_vecina, distancias)  # Calcula la distancia total de la ruta vecina
        
        diferencia = distancia_vecina - distancia_actual  # Calcula la diferencia entre la nueva distancia y la distancia actual
        
        if diferencia < 0 or np.random.rand() < np.exp(-diferencia / temperatura_actual):  # Si la nueva distancia es mejor o se acepta una peor distancia según la probabilidad de Boltzmann
            ruta_actual = ruta_vecina  # Actualiza la ruta actual con la ruta vecina
            distancia_actual = distancia_vecina  # Actualiza la distancia actual con la distancia de la ruta vecina
        
        if distancia_actual < mejor_distancia:  # Si la distancia actual es mejor que la mejor distancia encontrada
            mejor_ruta = ruta_actual  # Actualiza la mejor ruta con la ruta actual
            mejor_distancia = distancia_actual  # Actualiza la mejor distancia con la distancia actual
        
        temperatura_actual *= factor_enfriamiento  # Enfría la temperatura
    
    return mejor_ruta, mejor_distancia  # Retorna la mejor ruta encontrada y su distancia

punto_inicio = 1  # Define el punto de inicio de la búsqueda
punto_destino = 4  # Define el punto de destino de la búsqueda
temperatura_inicial = 100  # Define la temperatura inicial del algoritmo de Temple Simulado
factor_enfriamiento = 0.95  # Define el factor de enfriamiento del algoritmo de Temple Simulado
max_iter = 1000  # Define el número máximo de iteraciones del algoritmo de Temple Simulado

mejor_ruta, mejor_distancia = temple_simulado_busqueda_ruta(distancias, punto_inicio, punto_destino, temperatura_inicial, factor_enfriamiento, max_iter)  # Ejecuta el algoritmo de Temple Simulado

print("La ruta mas factible encontrada es:", mejor_ruta)  # Imprime la mejor ruta encontrada
