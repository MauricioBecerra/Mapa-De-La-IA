from sympy import symbols, Not, Or, And, Implies, satisfiable
from sympy.logic.boolalg import to_cnf

# Definimos los símbolos A y B
A, B = symbols('A B')

# Definimos las cláusulas que forman la fórmula
clauses = [
    Or(A, B),  # Clausula 1: A o B
    Or(A),     # Clausula 2: A
    Or(B)      # Clausula 3: B
]

# Convertimos las cláusulas a forma normal conjuntiva (CNF)
cnf = to_cnf(And(*clauses))

print("Forma normal conjuntiva (CNF):", cnf)

# Verificamos si la fórmula es satisfacible
if satisfiable(cnf):
    print("La fórmula es satisfacible.")  # Si es satisfacible, imprimimos un mensaje
else:
    print("La fórmula no es satisfacible.")  # Si no es satisfacible, imprimimos otro mensaje
