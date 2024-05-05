import itertools  # Importa la biblioteca itertools para generar combinaciones

def generate_truth_table(expression):  # Define una función para generar una tabla de verdad
    variables = sorted(set(c for c in expression if c.isalpha()))  # Encuentra todas las letras (variables) en la expresión y las ordena alfabéticamente
    num_vars = len(variables)  # Obtiene el número de variables
    rows = list(itertools.product([True, False], repeat=num_vars))  # Genera todas las posibles combinaciones de True y False para las variables

    print("Truth Table for expression:", expression)  # Imprime un encabezado para la tabla de verdad
    print("-" * (4 * num_vars + 3))  # Imprime una línea para separar el encabezado de la tabla
    print("|", end="")  # Imprime el comienzo de la primera fila

    for var in variables:  # Itera sobre todas las variables
        print(f" {var} |", end="")  # Imprime cada variable con bordes verticales
    print(f" {expression} |")  # Imprime la expresión en la última columna de la primera fila
    print("-" * (4 * num_vars + 3))  # Imprime una línea para separar el encabezado de la tabla

    for row in rows:  # Itera sobre todas las combinaciones de valores de verdad
        row_eval = {var: val for var, val in zip(variables, row)}  # Crea un diccionario que asocia cada variable con su valor de verdad actual
        result = eval(expression, row_eval)  # Evalúa la expresión con los valores de verdad actuales
        print("|", end="")  # Imprime el comienzo de una nueva fila

        for val in row:  # Itera sobre los valores de verdad en la fila actual
            print(f" {val} |", end="")  # Imprime cada valor de verdad con bordes verticales
        print(f" {result} |")  # Imprime el resultado de la evaluación de la expresión en la última columna
        print("-" * (4 * num_vars + 3))  # Imprime una línea para separar las filas de la tabla

if __name__ == "__main__":  # Verifica si el script es el programa principal
    expression = '(p | q) & (~p)'  # Define una nueva expresión
    generate_truth_table(expression)  # Genera la tabla de verdad para la nueva expresión
