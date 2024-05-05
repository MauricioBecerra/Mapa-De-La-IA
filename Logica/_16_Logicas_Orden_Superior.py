from functools import reduce

# Definimos la función AND
def AND(*args):
    return reduce(lambda x, y: x and y, args)

# Definimos la función OR
def OR(*args):
    return reduce(lambda x, y: x or y, args)

# Definimos la función NOT
def NOT(x):
    return not x

# Definimos la función IMPLIES
def IMPLIES(x, y):
    return (not x) or y

# Definimos la función EQUIV
def EQUIV(x, y):
    return (x and y) or ((not x) and (not y))

# Definimos los valores de las variables proposicionales
p = True
q = False
r = True

# Imprimimos los resultados de las operaciones lógicas
print("AND(p, q, r) =", AND(p, q, r))     # Operación AND
print("OR(p, q, r) =", OR(p, q, r))       # Operación OR
print("NOT(p) =", NOT(p))                 # Operación NOT
print("IMPLIES(p, q) =", IMPLIES(p, q))   # Operación IMPLIES
print("EQUIV(p, q) =", EQUIV(p, q))       # Operación EQUIV
