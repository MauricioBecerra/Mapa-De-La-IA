class BaseConocimiento:
    def __init__(self):
        self.hechos = []  # Inicializa una lista para almacenar los hechos

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)  # Agrega un hecho a la lista de hechos

    def consultar_hecho(self, hecho):
        return hecho in self.hechos  # Verifica si el hecho está presente en la lista de hechos

class Agente:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento  # Establece la base de conocimiento del agente

    def realizar_accion(self, accion):
        if self.base_conocimiento.consultar_hecho(accion):  # Consulta si la acción está en la base de conocimiento
            print(f"Realizando la acción: {accion}")  # Si está, se realiza la acción
        else:
            print(f"No se realiza la acción {accion} debido a la incertidumbre.")  # Si no está, se muestra un mensaje de incertidumbre

# Creamos una instancia de BaseConocimiento y agregamos algunos hechos
base_conocimiento = BaseConocimiento()
base_conocimiento.agregar_hecho("Accion1")
base_conocimiento.agregar_hecho("Accion2")

# Creamos una instancia de Agente y le asignamos la base de conocimiento
agente = Agente(base_conocimiento)

# El agente realiza algunas acciones
agente.realizar_accion("Accion1")  # La acción "Accion1" está en la base de conocimiento, entonces se realiza
agente.realizar_accion("Accion3")  # La acción "Accion3" no está en la base de conocimiento, entonces muestra un mensaje de incertidumbre
