class CSP:
    # Inicializa la clase CSP con una lista de variables y un diccionario de dominios.
    def __init__(self, variables, dominios):
        self.variables = variables  # Lista de variables del problema CSP.
        self.dominios = dominios  # Diccionario que asigna a cada variable su conjunto de valores posibles.
        self.restricciones = {}  # Diccionario para almacenar las restricciones por variable.

    # Agrega una restricción al problema CSP.
    def agregar_restriccion(self, restriccion):
        for var in restriccion.alcance:
            if var not in self.restricciones:
                self.restricciones[var] = []  # Crea una lista vacía para las restricciones de la variable.
            self.restricciones[var].append(restriccion)  # Agrega la restricción a la lista correspondiente.

    # Verifica si una asignación es consistente con las restricciones.
    def consistente(self, var, valor, asignacion):
        for restriccion in self.restricciones.get(var, []):
            if not restriccion.satisfecha(valor, asignacion):
                return False  # La asignación no es consistente si alguna restricción no se cumple.
        return True  # La asignación es consistente si todas las restricciones se cumplen.

    # Implementa la búsqueda por retroceso para encontrar una solución.
    def busqueda_retroceso(self, asignacion={}):
        if len(asignacion) == len(self.variables):
            return asignacion  # Si la asignación cubre todas las variables, se ha encontrado una solución.
        var = self.seleccionar_variable_no_asignada(asignacion)  # Selecciona una variable no asignada.
        for valor in self.ordenar_valores_dominio(var, asignacion):
            if self.consistente(var, valor, asignacion):
                asignacion[var] = valor  # Asigna el valor a la variable.
                resultado = self.busqueda_retroceso(asignacion)  # Realiza la búsqueda recursiva.
                if resultado is not None:
                    return resultado  # Si se encuentra una solución, la devuelve.
                del asignacion[var]  # Si no se encuentra una solución, deshace la asignación.
        return None  # No se encontró una solución.

    # Selecciona una variable no asignada.
    def seleccionar_variable_no_asignada(self, asignacion):
        for var in self.variables:
            if var not in asignacion:
                return var

    # Devuelve los valores del dominio de una variable.
    def ordenar_valores_dominio(self, var, asignacion):
        return self.dominios[var]


class Restriccion:
    # Inicializa una restricción con un conjunto de variables en su alcance.
    def __init__(self, alcance):
        self.alcance = alcance  # Lista de variables involucradas en la restricción.

    # Método abstracto para verificar si la restricción se satisface con una asignación dada.
    def satisfecha(self, asignacion):
        raise NotImplementedError  # Cada restricción concreta debe implementar este método.


class RestriccionDistinto(Restriccion):
    # Verifica si el valor dado es diferente de los valores asignados a las variables en el alcance.
    def satisfecha(self, valor, asignacion):
        if valor in asignacion.values():
            return False  # La restricción no se satisface si el valor está presente en la asignación.
        return True  # La restricción se satisface si el valor no está presente en la asignación.


variables = ['Jalisco', 'Nayarit', 'Zacatecas', 'Durango']  # Nombres de las variables del problema CSP.
dominios = {
    'Jalisco': [1, 2, 3],     # Posibles valores para la variable Jalisco.
    'Nayarit': [1, 2, 3],     # Posibles valores para la variable Nayarit.
    'Zacatecas': [1, 2, 3],   # Posibles valores para la variable Zacatecas.
    'Durango': [1, 2, 3]      # Posibles valores para la variable Durango.
}
csp = CSP(variables, dominios)  # Instancia un objeto CSP con las variables y los dominios definidos.

csp.agregar_restriccion(RestriccionDistinto(['Jalisco', 'Nayarit']))  # Agrega una restricción entre Jalisco y Nayarit.
csp.agregar_restriccion(RestriccionDistinto(['Nayarit', 'Zacatecas']))  # Agrega una restricción entre Nayarit y Zacatecas.

solucion = csp.busqueda_retroceso()  # Realiza la búsqueda por retroceso para encontrar una solución.
if solucion is not None:
    print("La solución encontrada es:", solucion)  # Imprime la solución encontrada.
else:
    print("No se encontró solución. :c")  # Imprime un mensaje si no se encontró solución.
