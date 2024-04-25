import numpy as np  # Importa la librería numpy bajo el alias np

mails = [(13, 12), (15, 2), (10, 15), (7, 13), (10, 12), (2, 9)]  # Define una lista de ubicaciones de correos electrónicos

def distancia(ubi1, ubi2):  # Define una función para calcular la distancia euclidiana entre dos ubicaciones
    return np.sqrt((ubi1[0] - ubi2[0])**2 + (ubi1[1] - ubi2[1])**2)

def fitness(ruta):  # Define una función de aptitud que cuenta el número de correos entregados en una ruta
    mails_entregados = 0
    for i in range(len(ruta) - 1):
        mails_entregados += 1
    return mails_entregados

def algoritmo_genetico(tam_poblacion, tam_ruta, num_generaciones):  # Define una función para el algoritmo genético
    poblacion = np.zeros((tam_poblacion, tam_ruta), dtype=int)  # Crea una población aleatoria
    for i in range(tam_poblacion):
        poblacion[i] = np.random.permutation(tam_ruta)
    best_solution = None  # Inicializa la mejor solución
    best_fitness = float('-inf')  # Inicializa la mejor aptitud
    
    for _ in range(num_generaciones):  # Itera sobre el número de generaciones especificado
        fitness_poblacion = [fitness(individuo) for individuo in poblacion]  # Calcula la aptitud de la población
        idx_mejor = np.argmax(fitness_poblacion)  # Encuentra el índice de la mejor solución
        if fitness_poblacion[idx_mejor] > best_fitness:  # Comprueba si se encontró una mejor solución
            best_fitness = fitness_poblacion[idx_mejor]  # Actualiza la mejor aptitud
            best_solution = poblacion[idx_mejor]  # Actualiza la mejor solución
        
        padres = seleccion_padres(poblacion, fitness_poblacion)  # Realiza la selección de padres
        descendencia = []  # Inicializa la lista de descendencia
        for i in range(0, tam_poblacion, 2):  # Itera sobre los padres
            hijo_1, hijo_2 = cruce(padres[i], padres[i+1])  # Realiza el cruce
            descendencia.append(hijo_1)  # Agrega el primer hijo a la descendencia
            descendencia.append(hijo_2)  # Agrega el segundo hijo a la descendencia
        
        poblacion = np.array(descendencia)  # Actualiza la población con la nueva descendencia
    
    return best_solution, best_fitness  # Devuelve la mejor solución y su aptitud

def seleccion_padres(poblacion, fitness_poblacion):  # Define una función para la selección de padres
    padres = []  # Inicializa la lista de padres
    for _ in range(len(poblacion)):  # Itera sobre la población
        idx1 = np.random.randint(0, len(poblacion))  # Elige un índice aleatorio para el primer padre
        idx2 = np.random.randint(0, len(poblacion))  # Elige un índice aleatorio para el segundo padre
        if fitness_poblacion[idx1] > fitness_poblacion[idx2]:  # Compara las aptitudes de los padres
            padres.append(poblacion[idx1])  # Agrega el primer padre si su aptitud es mejor
        else:
            padres.append(poblacion[idx2])  # Agrega el segundo padre si su aptitud es mejor
    return padres  # Devuelve la lista de padres seleccionados

def cruce(padre_1, padre_2):  # Define una función para el cruce
    punto_cruce = np.random.randint(1, len(padre_1))  # Elige un punto de cruce aleatorio
    hijo_1 = np.concatenate((padre_1[:punto_cruce], padre_2[punto_cruce:]))  # Genera el primer hijo
    hijo_2 = np.concatenate((padre_2[:punto_cruce], padre_1[punto_cruce:]))  # Genera el segundo hijo
    return hijo_1, hijo_2  # Devuelve los hijos generados

tam_poblacion = 50  # Tamaño de la población
tam_ruta = len(mails)  # Tamaño de la ruta (número de ubicaciones de correos electrónicos)
num_generaciones = 200  # Número de generaciones

best_solution, best_fitness = algoritmo_genetico(tam_poblacion, tam_ruta, num_generaciones)  # Ejecuta el algoritmo genético

print("La mejor ruta que se encontro es: ", best_solution)  # Imprime la mejor solución encontrada
print("Número de mails entregados por la ruta: ", best_fitness)  # Imprime el número de correos entregados por la ruta
