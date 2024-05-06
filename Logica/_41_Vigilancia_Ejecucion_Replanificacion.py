class Tarea:
    def __init__(self, nombre, duracion):
        # Inicializa una tarea con un nombre y una duración
        self.nombre = nombre
        self.duracion = duracion

class Agenda:
    def __init__(self):
        # Inicializa una agenda vacía
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Agrega una tarea a la agenda
        self.tareas.append(tarea)

    def imprimir_agenda(self):
        # Imprime todas las tareas en la agenda
        print("Agenda:")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea.nombre} - Duración: {tarea.duracion} horas")

class Planificador:
    def __init__(self):
        # Inicializa un planificador con una agenda vacía
        self.agenda = Agenda()

    def agregar_tarea(self, nombre, duracion):
        # Agrega una tarea a la agenda del planificador
        tarea = Tarea(nombre, duracion)
        self.agenda.agregar_tarea(tarea)

    def replanificar(self, tarea, nueva_duracion):
        # Replanifica una tarea con una nueva duración
        for t in self.agenda.tareas:
            if t.nombre == tarea:
                t.duracion = nueva_duracion
                print(f"La tarea '{tarea}' ha sido replanificada a {nueva_duracion} horas.")

def main():
    # Función principal
    planificador = Planificador()

    # Agrega nuevas tareas al planificador
    planificador.agregar_tarea("Lectura de libro", 3)
    planificador.agregar_tarea("Ejercicio", 1)
    planificador.agregar_tarea("Redacción de artículo", 4)

    # Imprime la agenda actual
    planificador.agenda.imprimir_agenda()

    # Replanifica una tarea existente
    planificador.replanificar("Redacción de artículo", 6)

    # Imprime la agenda actualizada
    planificador.agenda.imprimir_agenda()

if __name__ == "__main__":
    main()
