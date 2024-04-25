import numpy as np  # Importa el módulo numpy como np

def funcion_objetivo(x):  # Define la función objetivo
    return x**4 - 3 * x**3 + 2 * x**2 + x

def busqueda_haz_local(func_obj, x_inicial, paso, max_iter):  # Define la función para la búsqueda de haz local
    x_actual = x_inicial  # Inicializa la posición actual en x
    
    for _ in range(max_iter):  # Itera el número máximo de veces especificado
        valor_actual = func_obj(x_actual)  # Calcula el valor de la función en la posición actual
        
        vecino = x_actual + np.random.uniform(-paso, paso)  # Genera un vecino aleatorio
        
        valor_vecino = func_obj(vecino)  # Calcula el valor de la función en el vecino
        
        if valor_vecino < valor_actual:  # Compara si el vecino es mejor que la posición actual
            x_actual = vecino  # Actualiza la posición actual si el vecino es mejor
    
    return x_actual, func_obj(x_actual)  # Retorna la mejor solución encontrada y su valor

x_inicial = 1  # Punto de inicio de la búsqueda
paso = 0.1  # Tamaño del paso para generar vecinos
max_iter = 10000  # Número máximo de iteraciones

# Ejecución del algoritmo de búsqueda de haz local
mejor_solucion, mejor_valor = busqueda_haz_local(funcion_objetivo, x_inicial, paso, max_iter)

# Imprime el resultado
print("La mejor solución encontrada es: ", mejor_solucion)
print("El valor encontrado de la función en la mejor solución es:", mejor_valor)