class AccionCondicional:
    def __init__(self, condicion, accion):
        # Inicializa una acción condicional con una condición y una acción a realizar
        self.condicion = condicion  # La condición que debe cumplirse para ejecutar la acción
        self.accion = accion  # La acción a ejecutar si se cumple la condición

class Entorno:
    def __init__(self, estado_inicial):
        # Inicializa el entorno con un estado inicial
        self.estado = estado_inicial

    def aplicar_accion(self, accion):
        # Aplica una acción al estado actual del entorno
        if accion.condicion(self.estado):  # Verifica si se cumple la condición de la acción
            self.estado = accion.accion(self.estado)  # Ejecuta la acción si la condición se cumple
            return True  # Indica que se aplicó la acción
        else:
            return False  # Indica que la acción no se pudo aplicar porque la condición no se cumplió

if __name__ == "__main__":
    # Definición de las condiciones y acciones
    def condicion_soleado(estado):
        return estado['clima'] == 'soleado'  # La condición se cumple si el clima es soleado

    def condicion_lluvioso(estado):
        return estado['clima'] == 'lluvioso'  # La condición se cumple si el clima es lluvioso

    def accion_salir_exterior(estado):
        print("¡Sal al exterior!")  # Acción: Salir al exterior
        return estado  # Retorna el estado sin cambios

    def accion_quedarse_adentro(estado):
        print("Quédate en casa.")  # Acción: Quedarse en casa
        return estado  # Retorna el estado sin cambios

    estado_inicial = {'clima': 'soleado'}  # Estado inicial: Soleado
    entorno = Entorno(estado_inicial)  # Crea un entorno con el estado inicial

    # Definición de acciones condicionales
    accion_si_soleado = AccionCondicional(condicion_soleado, accion_salir_exterior)
    accion_si_lluvioso = AccionCondicional(condicion_lluvioso, accion_quedarse_adentro)

    # Aplicar acciones al entorno
    entorno.aplicar_accion(accion_si_soleado)  # Intenta aplicar la acción si está soleado
    entorno.aplicar_accion(accion_si_lluvioso)  # Intenta aplicar la acción si está lluvioso
