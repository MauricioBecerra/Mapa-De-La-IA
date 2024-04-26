class CSP:
    # Definición de una clase para resolver problemas CSP (Constraint Satisfaction Problems).
    def __init__(self, variables, dominios, restricciones):
        # Inicialización de la clase con variables, dominios y restricciones.
        self.variables = variables  # Lista de variables del problema CSP.
        self.dominios = dominios  # Diccionario que mapea cada variable a su conjunto de dominio.
        self.restricciones = restricciones  # Diccionario que mapea cada variable a las variables con las que tiene restricciones.

    def es_consistente(self, variable, asignacion):
        # Método para verificar si asignar un valor a una variable es consistente con las restricciones.
        for vecino in self.restricciones.get(variable, []):
            # Para cada variable vecina de la variable actual:
            if vecino in asignacion and asignacion[vecino] == asignacion[variable]:
                # Si la variable vecina está asignada y tiene el mismo valor que la variable actual:
                return False  # La asignación no es consistente.
        return True  # La asignación es consistente.

    def busqueda_con_retroceso(self, asignacion={}):
        # Implementación del algoritmo de búsqueda con retroceso.
        if len(asignacion) == len(self.variables):
            # Si la asignación es completa (todas las variables están asignadas), se ha encontrado una solución.
            return asignacion
        var = next((v for v in self.variables if v not in asignacion), None)
        # Selecciona una variable no asignada.
        for valor in self.dominios[var]:
            # Para cada valor en el dominio de la variable seleccionada:
            if self.es_consistente(var, {**asignacion, var: valor}):
                # Si la asignación de ese valor es consistente con las asignaciones actuales:
                asignacion[var] = valor  # Asigna ese valor a la variable.
                resultado = self.busqueda_con_retroceso(asignacion)
                # Realiza una búsqueda recursiva con la nueva asignación.
                if resultado is not None:
                    return resultado  # Si se encuentra una solución, devuelve la asignación.
                del asignacion[var]  # Si no se encuentra una solución, elimina la asignación.
        return None  # No se encontró una solución.

if __name__ == "__main__":
    # Ejemplo de uso del algoritmo de búsqueda con retroceso para resolver un CSP.
    variables = ['Jalisco', 'Nayarit', 'Zacatecas', 'Durango']  # Nombres de las variables del problema CSP.
    dominios = {
        'Jalisco': ['Camion', 'Tren', 'Carros'],  # Posibles valores para la variable Jalisco.
        'Nayarit': ['Camion', 'Tren', 'Carros'],  # Posibles valores para la variable Nayarit.
        'Zacatecas': ['Camion', 'Tren', 'Carros'],  # Posibles valores para la variable Zacatecas.
        'Durango': ['Camion', 'Tren', 'Carros']   # Posibles valores para la variable Durango.
    }
    restricciones = {
        'Jalisco': ['Nayarit', 'Durango'],     # Restricciones de la variable Jalisco.
        'Nayarit': ['Jalisco', 'Zacatecas', 'Durango'],  # Restricciones de la variable Nayarit.
        'Zacatecas': ['Jalisco', 'Durango', 'Nayarit'],  # Restricciones de la variable Zacatecas.
        'Durango': ['Nayarit', 'Zacatecas']      # Restricciones de la variable Durango.
    }
    csp = CSP(variables, dominios, restricciones)  # Creación de una instancia del problema CSP.
    solucion = csp.busqueda_con_retroceso()  # Ejecución del algoritmo de búsqueda con retroceso.
    if solucion:
        # Si se encontró una solución, imprime la asignación de variables.
        print("Se encontró una solución:")
        for variable, valor in solucion.items():
            print(f"{variable}: {valor}")
    else:
        # Si no se encontró una solución, imprime un mensaje indicándolo.
        print("No se encontró una solución.")
