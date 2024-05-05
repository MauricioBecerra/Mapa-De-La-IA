from sympy import symbols, Or, And, Not, to_cnf  # Importa las funciones necesarias desde la biblioteca sympy

def obtener_variables(expresion):
    return list(expresion.free_symbols)  # Obtiene las variables en la expresión

def forma_normal_conjuntiva(expresion):
    fnc = to_cnf(expresion)  # Convierte la expresión a su Forma Normal Conjuntiva (FNC)
    return fnc

# Define nuevas variables lógicas
A, B, C = symbols('A B C')

# Define una nueva expresión lógica
expresion_logica = Or(And(A, B), Or(Not(A), C))

# Obtiene las variables de la expresión
variables = obtener_variables(expresion_logica)

# Obtiene la Forma Normal Conjuntiva (FNC) de la expresión
fnc = forma_normal_conjuntiva(expresion_logica)

# Imprime los resultados
print("Expresión original:", expresion_logica)
print("Variables en la expresión:", variables)
print("Forma Normal Conjuntiva (FNC):", fnc)
