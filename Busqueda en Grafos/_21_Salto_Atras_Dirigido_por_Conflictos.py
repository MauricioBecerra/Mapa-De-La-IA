class CSP:
    # Constructor de la clase CSP
    def __init__(self, variables, dominios):
        # Inicializa las variables, los dominios y las restricciones
        self.variables = variables
        self.dominios = dominios
        self.restricciones = {}

    # Método para agregar una restricción al problema CSP
    def add_constraint(self, constraint):
        # Itera sobre el alcance de la restricción
        for var in constraint.scope:
            # Si la variable no está en las restricciones, crea una lista vacía
            if var not in self.restricciones:
                self.restricciones[var] = []
            # Agrega la restricción a la lista de restricciones de la variable
            self.restricciones[var].append(constraint)

    # Método para verificar si una asignación es consistente con las restricciones
    def consistent(self, var, value, assignment):
        # Itera sobre las restricciones asociadas a la variable
        for constraint in self.restricciones.get(var, []):
            # Verifica si la restricción se satisface con el valor dado y la asignación actual
            if not constraint.satisfied(value, assignment):
                return False
        return True

    # Método para el Salto Atrás Dirigido por Conflictos
    def conflict_directed_backjumping(self, assignment={}, level=0):
        # Verifica si la asignación actual cubre todas las variables
        if len(assignment) == len(self.variables):
            return assignment
        # Selecciona una variable no asignada
        var = self.select_unassigned_variable(assignment)
        # Itera sobre los valores en el dominio de la variable
        for value in self.order_domain_values(var, assignment):
            # Verifica si el valor es consistente con la asignación actual
            if self.consistent(var, value, assignment):
                # Asigna el valor a la variable
                assignment[var] = value
                # Realiza la búsqueda recursiva con la nueva asignación
                result = self.conflict_directed_backjumping(assignment, level)
                # Si se encuentra una solución, la devuelve
                if result is not None:
                    return result
                # Si no se encuentra una solución, deshace la asignación
                del assignment[var]
        # Si no se encuentra ninguna solución, devuelve None
        return None

    # Método para seleccionar una variable no asignada
    def select_unassigned_variable(self, assignment):
        # Itera sobre las variables y devuelve la primera no asignada
        for var in self.variables:
            if var not in assignment:
                return var

    # Método para ordenar los valores del dominio de una variable
    def order_domain_values(self, var, assignment):
        # Devuelve los valores del dominio sin ordenar
        return self.dominios[var]


class Constraint:
    # Constructor de la clase Constraint
    def __init__(self, scope):
        # Inicializa el alcance de la restricción
        self.scope = scope

    # Método para verificar si la restricción se satisface con la asignación dada
    def satisfied(self, assignment):
        # Este método será implementado en subclases
        raise NotImplementedError


class AllDifferentConstraint(Constraint):
    # Método para verificar si el valor dado es diferente a los valores asignados
    def satisfied(self, value, assignment):
        # Verifica si el valor está presente en los valores asignados
        if value in assignment.values():
            return False
        return True


if __name__ == "__main__":
    # Definición de las variables y dominios
    variables = ['Jalisco', 'Nayarit', 'Zacatecas', 'Durango']  # Nombres de las variables del problema CSP.
    dominios = {
        'Jalisco': [1, 2, 3],     # Posibles valores para la variable Jalisco.
        'Nayarit': [1, 2, 3],     # Posibles valores para la variable Nayarit.
        'Zacatecas': [1, 2, 3],   # Posibles valores para la variable Zacatecas.
        'Durango': [1, 2, 3]      # Posibles valores para la variable Durango.
    }
    # Instancia un objeto CSP con las variables y los dominios definidos
    csp = CSP(variables, dominios)

    # Agrega restricciones al problema CSP
    csp.add_constraint(AllDifferentConstraint(['Jalisco', 'Nayarit']))  # Agrega una restricción entre Jalisco y Nayarit.
    csp.add_constraint(AllDifferentConstraint(['Nayarit', 'Zacatecas']))  # Agrega una restricción entre Nayarit y Zacatecas.

    # Realiza la búsqueda utilizando Salto Atrás Dirigido por Conflictos para encontrar una solución
    solution = csp.conflict_directed_backjumping()
    # Imprime la solución encontrada o un mensaje indicando que no se encontró solución
    if solution is not None:
        print("La solución encontrada es:", solution)  # Imprime la solución encontrada.
    else:
        print("No se encontró solución. :c")  # Imprime un mensaje si no se encontró solución.