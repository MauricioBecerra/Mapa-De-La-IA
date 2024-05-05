class ConjuntoDifuso:
    def __init__(self, nombre, funcion_membresia):
        self.nombre = nombre  # Define el nombre del conjunto difuso
        self.funcion_membresia = funcion_membresia  # Asigna la función de membresía al conjunto

    def membresia(self, valor):
        return self.funcion_membresia(valor)  # Calcula y devuelve el valor de membresía para un valor dado


def triangulo(a, b, c):
    # Define una función de membresía triangular con parámetros a, b, c
    def funcion(valor):
        if valor <= a or valor >= c:
            return 0  # Si el valor está fuera del intervalo, la membresía es cero
        elif a < valor < b:
            return (valor - a) / (b - a)  # Si el valor está en la pendiente ascendente, calcula la membresía
        elif b <= valor <= c:
            return (c - valor) / (c - b)  # Si el valor está en la pendiente descendente, calcula la membresía
        else:
            return 0  # Si el valor está fuera del intervalo, la membresía es cero
    return funcion  # Devuelve la función de membresía


def trapezoide(a, b, c, d):
    # Define una función de membresía trapezoidal con parámetros a, b, c, d
    def funcion(valor):
        if valor <= a or valor >= d:
            return 0  # Si el valor está fuera del intervalo, la membresía es cero
        elif a < valor < b:
            return (valor - a) / (b - a)  # Si el valor está en la pendiente ascendente, calcula la membresía
        elif c < valor < d:
            return (d - valor) / (d - c)  # Si el valor está en la pendiente descendente, calcula la membresía
        else:
            return 1  # Si el valor está en el "platou", la membresía es uno
    return funcion  # Devuelve la función de membresía


# Creamos dos conjuntos difusos utilizando funciones trapezoidales
conjunto_frio = ConjuntoDifuso("Frio", trapezoide(0, 0, 10, 20))
conjunto_caliente = ConjuntoDifuso("Caliente", trapezoide(10, 20, 30, 30))

temperatura = 15  # Temperatura a evaluar

# Mostramos las membresías de la temperatura en los conjuntos difusos
print(f"La membresía de {temperatura} en el conjunto {conjunto_frio.nombre} es: {conjunto_frio.membresia(temperatura)}")
print(f"La membresía de {temperatura} en el conjunto {conjunto_caliente.nombre} es: {conjunto_caliente.membresia(temperatura)}")
