import random  # Importa el módulo random para generar números aleatorios

def funcion_objetivo(posicion):  # Define una función que evalúa una posición dada
    # Diccionario que contiene las evaluaciones para diferentes posiciones
    evaluacion = {
        ('Jalisco', '1'): 1.5, ('Nayarit', '1'): 0.7, ('Zacatecas', '1'): 0.9, ('Durango', '1'): 1.2, ('Coahuila', '1'): 1.8,
        ('Jalisco', '2'): 0.4, ('Nayarit', '2'): 0.8, ('Zacatecas', '2'): 1.7, ('Durango', '2'): 1.0, ('Coahuila', '2'): 0.6,
        ('Jalisco', '3'): 1.4, ('Nayarit', '3'): 1.9, ('Zacatecas', '3'): 0.3, ('Durango', '3'): 1.6, ('Coahuila', '3'): 1.1,
        ('Jalisco', '4'): 0.2, ('Nayarit', '4'): 1.3, ('Zacatecas', '4'): 1.5, ('Durango', '4'): 0.5, ('Coahuila', '4'): 0.1,
        ('Jalisco', '5'): 1.7, ('Nayarit', '5'): 0.5, ('Zacatecas', '5'): 0.8, ('Durango', '5'): 1.3, ('Coahuila', '5'): 1.0,
    }
    return evaluacion.get(posicion, 0.0)  # Devuelve la evaluación de la posición dada o 0.0 si no está en el diccionario

def ascenso_colinas_con_objetivo(max_iter, rango_filas, rango_columnas):  # Define la función de búsqueda por ascenso de colinas
    mejor_posicion = None  # Inicializa la variable para la mejor posición encontrada
    mejor_valor = float('-inf')  # Inicializa la variable para el mejor valor encontrado como infinito negativo

    for _ in range(max_iter):  # Realiza la búsqueda por el número máximo de iteraciones
        fila = random.choice(rango_filas)  # Elige una fila aleatoria del rango dado
        columna = random.choice(rango_columnas)  # Elige una columna aleatoria del rango dado
        posicion_actual = (fila, columna)  # Crea una tupla con la fila y columna actuales

        valor_actual = funcion_objetivo(posicion_actual)  # Obtiene la evaluación de la posición actual

        if valor_actual > mejor_valor:  # Si la evaluación actual es mejor que la mejor encontrada hasta ahora
            mejor_valor = valor_actual  # Actualiza el mejor valor
            mejor_posicion = posicion_actual  # Actualiza la mejor posición

    return mejor_posicion, mejor_valor  # Devuelve la mejor posición y su valor

# Define los rangos de filas y columnas para la búsqueda
rango_filas = ['Jalisco', 'Nayarit', 'Zacatecas', 'Durango', 'Coahuila']
rango_columnas = ['1', '2', '3', '4', '5']
max_iter = 1000  # Establece el número máximo de iteraciones para la búsqueda

mejor_posicion, mejor_valor = ascenso_colinas_con_objetivo(max_iter, rango_filas, rango_columnas) # Ejecuta la función de búsqueda y almacena la mejor posición y su valor
print(f"La mejor posicion es: {mejor_posicion} ,con un valor de: {mejor_valor}.") # Imprime la mejor posición encontrada y su valor