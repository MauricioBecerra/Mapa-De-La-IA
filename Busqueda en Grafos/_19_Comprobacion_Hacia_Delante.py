class Restriccion:
    # Define una clase para representar restricciones entre variables.
    def __init__(self, variable1, variable2):
        # Inicializa la restricción con dos variables.
        self.variable1 = variable1  # Guarda la primera variable.
        self.variable2 = variable2  # Guarda la segunda variable.

    def cumple_restriccion(self, valor1, valor2):
        # Comprueba si dos valores cumplen la restricción.
        return valor1 != valor2  # Devuelve True si los valores son diferentes, False en caso contrario.


class CSP:
    # Define una clase para el Problema de Satisfacción de Restricciones (CSP).
    def __init__(self, variables, dominio):
        # Inicializa el problema CSP con un conjunto de variables y su dominio.
        self.variables = variables  # Lista de variables del problema CSP.
        self.dominio = dominio  # Diccionario que mapea cada variable a su conjunto de valores posibles.
        self.restricciones = []  # Lista para almacenar las restricciones del problema.

    def agregar_restriccion(self, restriccion):
        # Agrega una restricción al problema CSP.
        self.restricciones.append(restriccion)  # Añade la restricción a la lista de restricciones.

    def comprobacion_hacia_adelante(self, variable, valor):
        # Realiza comprobación hacia adelante para propagar restricciones cuando se asigna un valor a una variable.
        for restriccion in self.restricciones:
            # Itera sobre todas las restricciones del problema.
            if restriccion.variable1 == variable:
                # Si la primera variable de la restricción es la variable actual:
                vecino = restriccion.variable2  # Identifica la variable vecina.
                for val in self.dominio[vecino]:
                    # Itera sobre los valores del dominio de la variable vecina.
                    if not restriccion.cumple_restriccion(valor, val):
                        # Si el valor asignado y el valor de la variable vecina no cumplen la restricción:
                        self.dominio[vecino].remove(val)
                        # Elimina el valor de la lista de valores posibles de la variable vecina.

variables = ['Jalisco', 'Nayarit', 'Zacatecas', 'Durango']  # Nombres de las variables del problema CSP.
dominio = {
    'Jalisco': ['Camion', 'Tren', 'Carros'],     # Posibles valores para la variable Jalisco.
    'Nayarit': ['Camion', 'Tren', 'Carros'],     # Posibles valores para la variable Nayarit.
    'Zacatecas': ['Camion', 'Tren', 'Carros'],   # Posibles valores para la variable Zacatecas.
    'Durango': ['Camion', 'Tren', 'Carros']      # Posibles valores para la variable Durango.
}

csp = CSP(variables, dominio)  # Crea una instancia del problema CSP.

# Agrega las restricciones (las regiones adyacentes no pueden tener el mismo transporte)
csp.agregar_restriccion(Restriccion('Jalisco', 'Nayarit'))    # Restricción entre Jalisco y Nayarit.
csp.agregar_restriccion(Restriccion('Jalisco', 'Zacatecas'))  # Restricción entre Jalisco y Zacatecas.
csp.agregar_restriccion(Restriccion('Nayarit', 'Zacatecas'))  # Restricción entre Nayarit y Zacatecas.
csp.agregar_restriccion(Restriccion('Nayarit', 'Durango'))    # Restricción entre Nayarit y Durango.
csp.agregar_restriccion(Restriccion('Zacatecas', 'Durango'))  # Restricción entre Zacatecas y Durango.

variable = 'Jalisco'  # Selecciona la variable 'Jalisco'.
valor = 'Carros'      # Asigna el valor 'Carros' a la variable 'Jalisco'.

csp.comprobacion_hacia_adelante(variable, valor)  # Realiza la propagación de restricciones.

print("Dominio después de la comprobación hacia adelante:")
for variable, valores in csp.dominio.items():
    # Imprime el dominio actualizado después de la propagación.
    print(variable + ":", valores)

