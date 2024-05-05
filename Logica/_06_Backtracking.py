def solucionar_sudoku(sudoku):
    if not encontrar_celda_vacia(sudoku):  # Si no hay celdas vacías en el sudoku
        return True  # Sudoku resuelto

    fila, columna = encontrar_celda_vacia(sudoku)  # Encuentra la primera celda vacía

    for numero in range(1, 10):  # Itera sobre los números del 1 al 9
        if es_numero_valido(sudoku, fila, columna, numero):  # Si el número es válido para esa celda
            sudoku[fila][columna] = numero  # Asigna el número a la celda

            if solucionar_sudoku(sudoku):  # Intenta resolver recursivamente el sudoku con este número asignado
                return True  # Si se encuentra una solución, devuelve True

            sudoku[fila][columna] = 0  # Si no se encuentra una solución, retrocede y vuelve a poner 0 en la celda

    return False  # Si no se encuentra solución

def encontrar_celda_vacia(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:  # Busca la primera celda vacía
                return i, j  # Devuelve sus coordenadas
    return None

def es_numero_valido(sudoku, fila, columna, numero):
    return not en_fila(sudoku, fila, numero) and \
           not en_columna(sudoku, columna, numero) and \
           not en_cuadrante(sudoku, fila - fila % 3, columna - columna % 3, numero)

def en_fila(sudoku, fila, numero):
    return numero in sudoku[fila]  # Verifica si el número ya está en la fila

def en_columna(sudoku, columna, numero):
    return numero in [sudoku[i][columna] for i in range(9)]  # Verifica si el número ya está en la columna

def en_cuadrante(sudoku, fila_inicio, columna_inicio, numero):
    return any(numero == sudoku[fila][columna] for fila in range(fila_inicio, fila_inicio + 3) for columna in range(columna_inicio, columna_inicio + 3))  # Verifica si el número ya está en el cuadrante

def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(fila)

sudoku = [
    [0, 0, 5, 0, 0, 0, 0, 8, 0],  # Nuevo problema de Sudoku
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 9, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7]
]

print("Problema de Sudoku:")
imprimir_sudoku(sudoku)

if solucionar_sudoku(sudoku):
    print("\nSolución encontrada:")
    imprimir_sudoku(sudoku)
else:
    print("\nNo se encontró solución.")
