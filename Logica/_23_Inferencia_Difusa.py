import numpy as np

class ConjuntoDifuso:
    def __init__(self, nombre, funcion_membresia):
        # Inicializa un conjunto difuso con un nombre y una función de membresía
        self.nombre = nombre
        self.funcion_membresia = funcion_membresia

    def membresia(self, valor):
        # Devuelve el grado de membresía para un valor dado utilizando la función de membresía del conjunto
        return self.funcion_membresia(valor)

class ReglaDifusa:
    def __init__(self, antecedente, consecuente):
        # Inicializa una regla difusa con un antecedente y un consecuente
        self.antecedente = antecedente
        self.consecuente = consecuente

    def activacion(self, entrada):
        # Calcula la activación de la regla para una entrada dada
        # Es el mínimo del grado de membresía del antecedente y el valor de membresía del consecuente
        return min(self.antecedente.membresia(entrada), self.consecuente.funcion_membresia(entrada))

class SistemaDifuso:
    def __init__(self, reglas):
        # Inicializa un sistema difuso con una lista de reglas
        self.reglas = reglas

    def inferencia(self, entrada):
        # Realiza la inferencia para una entrada dada y devuelve los resultados
        resultados = []
        for regla in self.reglas:
            # Itera sobre todas las reglas y calcula su activación
            activacion = regla.activacion(entrada)
            resultados.append((regla.consecuente.nombre, activacion))  # Almacena el nombre del consecuente y su activación
        return resultados

# Funciones de membresía
def triangular(a, b, c):
    # Define una función de membresía triangular
    def funcion(valor):
        if valor <= a or valor >= c:
            return 0
        elif a < valor <= b:
            return (valor - a) / (b - a)
        elif b < valor < c:
            return (c - valor) / (c - b)
        else:
            return 0
    return funcion

def trapezoidal(a, b, c, d):
    # Define una función de membresía trapezoidal
    def funcion(valor):
        if valor <= a or valor >= d:
            return 0
        elif a < valor <= b:
            return (valor - a) / (b - a)
        elif c <= valor <= d:
            return 1
        elif b < valor < c:
            return (d - valor) / (d - c)
        else:
            return 0
    return funcion

# Creación de los conjuntos difusos de temperatura
temperatura_fria = ConjuntoDifuso("Fria", triangular(0, 0, 10))
temperatura_media = ConjuntoDifuso("Media", triangular(5, 10, 15))
temperatura_caliente = ConjuntoDifuso("Caliente", triangular(10, 20, 20))

# Definición de las reglas difusas
regla1 = ReglaDifusa(temperatura_fria, temperatura_caliente)
regla2 = ReglaDifusa(temperatura_media, temperatura_media)
regla3 = ReglaDifusa(temperatura_caliente, temperatura_fria)

# Creación del sistema difuso con las reglas definidas
sistema = SistemaDifuso([regla1, regla2, regla3])

# Entrada a evaluar en el sistema difuso
entrada = 12
resultado = sistema.inferencia(entrada)

# Impresión de los resultados de la inferencia
print("Resultado de la inferencia:")
for nombre_consecuente, activacion in resultado:
    print(f"{nombre_consecuente}: {activacion}")
