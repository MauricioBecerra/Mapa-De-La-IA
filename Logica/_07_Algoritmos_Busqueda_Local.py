import random  # Importa el módulo random para generar números aleatorios

def generar_tablero(n):
    tablero = []  # Inicializa una lista vacía que representará el tablero
    columnas_disponibles = list(range(n))  # Genera una lista con las columnas disponibles para colocar las reinas
    for _ in range(n):  # Itera sobre el número de filas del tablero
        columna = random.choice(columnas_disponibles)  # Selecciona aleatoriamente una columna disponible para colocar una reina
        fila = [0] * n  # Crea una fila vacía
        fila[columna] = 1  # Coloca una reina en la fila actual y la columna seleccionada aleatoriamente
        tablero.append(fila)  # Agrega la fila al tablero
        columnas_disponibles.remove(columna)  # Elimina la columna seleccionada de las disponibles
    return tablero  # Devuelve el tablero generado

def evaluar_tablero(tablero):
    n = len(tablero)  # Obtiene el tamaño del tablero (número de filas o columnas)
    ataques = 0  # Inicializa el contador de ataques a 0
    for i in range(n):  # Itera sobre las filas del tablero
        for j in range(n):  # Itera sobre las columnas del tablero
            if tablero[i][j] == 1:  # Si hay una reina en la posición [i][j]
                for k in range(n):  # Itera sobre las filas del tablero para comprobar ataques
                    if k != i:  # Evita comparar la misma fila
                        if tablero[k][j] == 1:  # Si hay otra reina en la misma columna
                            ataques += 1  # Incrementa el contador de ataques
                        if abs(k - i) == abs(tablero[k].index(1) - j):  # Si hay otra reina en la misma diagonal
                            ataques += 1  # Incrementa el contador de ataques
    return ataques // 2  # Retorna la mitad de los ataques totales (ya que se cuentan dos veces)

def mover_reina(tablero, fila, nueva_columna):
    tablero[fila] = [0] * len(tablero)  # Borra la fila actual
    tablero[fila][nueva_columna] = 1  # Coloca una reina en la nueva columna

def busqueda_local(n, iteraciones):
    mejor_tablero = generar_tablero(n)  # Genera un tablero inicial aleatorio
    mejor_evaluacion = evaluar_tablero(mejor_tablero)  # Evalúa el tablero inicial

    for _ in range(iteraciones):  # Realiza un número determinado de iteraciones
        fila = random.randint(0, n - 1)  # Escoge aleatoriamente una fila del tablero
        columna_actual = mejor_tablero[fila].index(1)  # Obtiene la columna actual de la reina en esa fila
        nueva_columna = random.randint(0, n - 1)  # Escoge aleatoriamente una nueva columna
        if nueva_columna != columna_actual:  # Si la nueva columna es diferente a la actual
            tablero_temporal = [fila[:] for fila in mejor_tablero]  # Crea una copia temporal del tablero
            mover_reina(tablero_temporal, fila, nueva_columna)  # Mueve la reina a la nueva columna
            evaluacion_temporal = evaluar_tablero(tablero_temporal)  # Evalúa el nuevo tablero
            if evaluacion_temporal < mejor_evaluacion:  # Si la nueva evaluación es mejor que la mejor hasta ahora
                mejor_tablero = tablero_temporal  # Actualiza el tablero mejor
                mejor_evaluacion = evaluacion_temporal  # Actualiza la mejor evaluación
        if mejor_evaluacion == 0:  # Si no hay ataques, se ha encontrado una solución
            break  # Termina la búsqueda

    return mejor_tablero  # Retorna el mejor tablero encontrado

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if celda == 1 else "." for celda in fila))  # Imprime el tablero con "Q" representando una reina y "." representando una celda vacía

n = 8  # Tamaño del tablero (número de filas y columnas)
iteraciones = 10000  # Número de iteraciones para la búsqueda local

mejor_tablero = busqueda_local(n, iteraciones)  # Encuentra la mejor solución para el problema

def verificar_solucion(tablero):
    for i in range(n):  # Itera sobre todas las filas
        for j in range(i+1, n):  # Itera sobre las filas restantes
            if sum(tablero[i]) > 1 or sum(tablero[j]) > 1 or tablero[i].index(1) == tablero[j].index(1):
                return False  # Si hay más de una reina en una fila o columna, o si dos reinas están en la misma posición, retorna Falso
            if abs(i - j) == abs(tablero[i].index(1) - tablero[j].index(1)):
                return False  # Si dos reinas están en la misma diagonal, retorna Falso
    return True  # Si no se encontraron problemas, retorna Verdadero

if verificar_solucion(mejor_tablero):  # Verifica si la solución es válida
    print("Solución válida:")  # Imprime que la solución es válida
    imprimir_tablero(mejor_tablero)  # Imprime el tablero con la solución encontrada
else:
    print("Solución inválida.")  # Imprime que la solución es inválida si no cumple con las condiciones
