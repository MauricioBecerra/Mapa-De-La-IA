class Agente:
    def __init__(self, nombre):
        # Inicializa un agente con un nombre y una lista vacía de tareas
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Agrega una tarea a la lista de tareas del agente
        self.tareas.append(tarea)

    def imprimir_tareas(self):
        # Imprime las tareas del agente
        print(f"Tareas del agente {self.nombre}:")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")

class Entorno:
    def __init__(self, agentes):
        # Inicializa el entorno con una lista de agentes
        self.agentes = agentes

    def asignar_tarea(self, agente, tarea):
        # Asigna una tarea a un agente en el entorno
        if agente in self.agentes:
            agente.agregar_tarea(tarea)
            print(f"La tarea '{tarea}' ha sido asignada al agente '{agente.nombre}'.")
        else:
            print(f"Error: El agente '{agente.nombre}' no existe en este entorno.")

def main():
    # Función principal
    agente1 = Agente("Agente 1")
    agente2 = Agente("Agente 2")
    agente3 = Agente("Agente 3")

    # Se crea un entorno con los agentes
    entorno = Entorno([agente1, agente2, agente3])

    # Se asignan tareas a los agentes
    entorno.asignar_tarea(agente1, "Estudio de mercado")
    entorno.asignar_tarea(agente2, "Revisión de documentos")
    entorno.asignar_tarea(agente3, "Elaboración de informe")

    # Se imprimen las tareas de cada agente
    agente1.imprimir_tareas()
    agente2.imprimir_tareas()
    agente3.imprimir_tareas()

if __name__ == "__main__":
    main()
