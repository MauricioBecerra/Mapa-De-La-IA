class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Precondiciones necesarias para aplicar la acción
        self.efectos = efectos  # Efectos de la acción sobre el estado

    def es_aplicable(self, estado):
        """
        Verifica si la acción es aplicable en el estado actual.

        Args:
        - estado: Un diccionario que representa el estado actual.

        Returns:
        - True si todas las precondiciones de la acción están presentes en el estado actual, False de lo contrario.
        """
        return all(item in estado.items() for item in self.precondiciones.items())

    def aplicar(self, estado):
        """
        Aplica la acción al estado actual.

        Args:
        - estado: Un diccionario que representa el estado actual.

        Returns:
        - Un nuevo estado después de aplicar la acción, o None si la acción no es aplicable.
        """
        if self.es_aplicable(estado):
            nuevo_estado = estado.copy()  # Crea una copia del estado actual
            nuevo_estado.update(self.efectos)  # Actualiza el estado con los efectos de la acción
            return nuevo_estado
        else:
            return None

class PlanificadorSTRIPS:
    def __init__(self, estado_inicial, estado_objetivo, acciones):
        self.estado_inicial = estado_inicial  # Estado inicial del plan
        self.estado_objetivo = estado_objetivo  # Estado objetivo del plan
        self.acciones = acciones  # Lista de acciones disponibles

    def planificar(self):
        plan = []  # Inicializa el plan como una lista vacía
        estado_actual = self.estado_inicial.copy()  # Copia el estado inicial

        # Continúa planificando hasta que el estado actual satisfaga el estado objetivo
        while not self.satisface(estado_actual, self.estado_objetivo):
            # Encuentra las acciones aplicables en el estado actual
            acciones_aplicables = [accion for accion in self.acciones if accion.es_aplicable(estado_actual)]
            # Si no hay acciones aplicables, no se puede alcanzar el estado objetivo
            if not acciones_aplicables:
                print("No se puede alcanzar el estado objetivo desde el estado inicial.")
                return None
            # Elige la primera acción aplicable y la agrega al plan
            accion_elegida = acciones_aplicables[0]
            plan.append(accion_elegida)
            # Aplica la acción al estado actual
            estado_actual = accion_elegida.aplicar(estado_actual)

        return plan

    def satisface(self, estado, estado_objetivo):
        """
        Verifica si el estado actual satisface el estado objetivo.

        Args:
        - estado: Un diccionario que representa el estado actual.
        - estado_objetivo: Un diccionario que representa el estado objetivo.

        Returns:
        - True si el estado actual contiene todos los elementos del estado objetivo, False de lo contrario.
        """
        return all(item in estado.items() for item in estado_objetivo.items())

# Definición de los estados inicial y objetivo, y las acciones disponibles
estado_inicial = {"casa": True, "puerta_abierta": False}
estado_objetivo = {"casa": True, "puerta_abierta": True}
acciones = [
    Accion("abrir_puerta", {"casa": True, "puerta_abierta": False}, {"puerta_abierta": True}),
    Accion("entrar_casa", {"casa": True, "puerta_abierta": True}, {})  # No hay efecto sobre la puerta
]

# Crea un planificador y planifica
planificador = PlanificadorSTRIPS(estado_inicial, estado_objetivo, acciones)
plan = planificador.planificar()

# Si se encontró un plan, imprime las acciones del plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion.nombre)
