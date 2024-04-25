def funcion_objetivo(x):  # Definición de la función objetivo
    return (x - 5) ** 2 + 8  # Retorna el resultado de la función (x - 5)^2 + 8

def generar_vecino(x, delta):  # Definición de la función para generar vecinos
    return x + delta  # Retorna el valor de x sumado al delta

def busqueda_tabu(func_obj, x_inicial, max_iter, delta, tabu_tenure):  # Implementación del algoritmo de búsqueda tabú
    mejor_solucion = x_inicial  # Almacena la mejor solución encontrada hasta el momento
    mejor_valor = func_obj(x_inicial)  # Almacena el valor de la mejor solución
    solucion_actual = x_inicial  # Almacena la solución actual
    lista_tabu = []  # Lista de soluciones prohibidas (tabú)

    for _ in range(max_iter):  # Realiza un número máximo de iteraciones
        vecinos = [generar_vecino(solucion_actual, delta), generar_vecino(solucion_actual, -delta)]  # Genera dos vecinos: uno con un incremento y otro con un decremento
        vecinos = [(vecino, func_obj(vecino)) for vecino in vecinos if vecino not in lista_tabu]  # Evalúa los vecinos y filtra aquellos que no están en la lista tabú
        if not vecinos:  # Si no hay vecinos disponibles, termina el algoritmo
            break
        vecinos.sort(key=lambda x: x[1])  # Ordena los vecinos según el valor de la función objetivo
        mejor_vecino, mejor_valor_vecino = vecinos[0]  # Obtiene el mejor vecino y su valor
        
        # Si el valor del mejor vecino es mejor que el mejor valor actual, actualiza la mejor solución
        if mejor_valor_vecino < mejor_valor:
            mejor_solucion = mejor_vecino
            mejor_valor = mejor_valor_vecino
        
        solucion_actual = mejor_vecino  # Actualiza la solución actual
        lista_tabu.append(solucion_actual)  # Agrega la solución actual a la lista tabú
        
        # Si la lista tabú excede la longitud especificada, elimina el elemento más antiguo
        if len(lista_tabu) > tabu_tenure:
            lista_tabu.pop(0)

    return mejor_solucion, mejor_valor  # Retorna la mejor solución encontrada y su valor

x_inicial = 0  # Punto de inicio de la búsqueda
max_iter = 100  # Número máximo de iteraciones
delta = 0.1  # Tamaño del paso para generar vecinos
tabu_tenure = 5  # Duración máxima de la prohibición de soluciones (lista tabú)

# Ejecución del algoritmo
mejor_solucion, mejor_valor = busqueda_tabu(funcion_objetivo, x_inicial, max_iter, delta, tabu_tenure)

print("La mejor solución es:", mejor_solucion)  # Imprime la mejor solución encontrada
print("Valor de la función en la mejor solución:", mejor_valor)  # Imprime el valor de la función en la mejor solución
