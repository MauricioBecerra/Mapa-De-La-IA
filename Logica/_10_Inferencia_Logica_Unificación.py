# Función para unificar una variable con un término
def unify_var(var, x, theta):
    if var in theta:  # Si la variable ya está en el conjunto de sustituciones
        return unify(theta[var], x, theta)  # Unificar el valor de la variable en theta con x
    elif x in theta:  # Si x ya está en el conjunto de sustituciones
        return unify(var, theta[x], theta)  # Unificar var con el valor de x en theta
    else:  # Si no hay una coincidencia anterior
        theta[var] = x  # Añadir var a theta con el valor de x
        return theta

# Función para unificar dos términos
def unify(x, y, theta):
    if theta is None:  # Si theta es None, la unificación ha fallado
        return None
    elif x == y:  # Si los términos son idénticos, no se necesita ninguna sustitución
        return theta
    elif isinstance(x, str) and x.islower():  # Si x es una variable
        return unify_var(x, y, theta)  # Llama a unify_var para unificar x con y
    elif isinstance(y, str) and y.islower():  # Si y es una variable
        return unify_var(y, x, theta)  # Llama a unify_var para unificar y con x
    elif isinstance(x, list) and isinstance(y, list):  # Si x e y son listas
        if len(x) != len(y):  # Si las listas no tienen la misma longitud, la unificación falla
            return None
        else:  # Si las listas tienen la misma longitud
            for xi, yi in zip(x, y):  # Itera sobre los elementos de las listas de manera paralela
                theta = unify(xi, yi, theta)  # Unifica cada elemento de x con su correspondiente en y
            return theta
    else:  # En todos los demás casos (no se pueden unificar)
        return None

x = ['P', 'x', 'y']  # Primer término
y = ['P', 'A', 'B']  # Segundo término
theta = {}  # Conjunto de sustituciones vacío

resultado = unify(x, y, theta)  # Realiza la unificación

print(resultado)  # Imprime el resultado de la unificación
