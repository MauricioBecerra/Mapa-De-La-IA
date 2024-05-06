class Task:
    def __init__(self, name, subtasks=None):
        # Inicializa una tarea con un nombre y una lista de subtareas (opcional)
        self.name = name
        self.subtasks = subtasks if subtasks else []  # Si no se proporcionan subtareas, crea una lista vacía

    def add_subtask(self, subtask):
        # Añade una subtarea a la lista de subtareas de la tarea actual
        self.subtasks.append(subtask)

    def __repr__(self):
        # Representación de cadena de la tarea, para fines de depuración
        return f"Task({self.name}, {self.subtasks})"

def execute_task(task):
    # Función para ejecutar una tarea y sus subtareas de forma recursiva
    print(f"Ejecutando tarea: {task.name}")  # Imprime el nombre de la tarea
    for subtask in task.subtasks:  # Itera sobre las subtareas de la tarea actual
        execute_task(subtask)  # Ejecuta la subtarea de forma recursiva

if __name__ == "__main__":
    # Ejemplo principal
    tarea_principal = Task("Tarea Principal")
    sub_tarea1 = Task("Subtarea 1")
    sub_tarea2 = Task("Subtarea 2")
    sub_sub_tarea1 = Task("Sub-Subtarea 1")
    sub_sub_tarea2 = Task("Sub-Subtarea 2")

    sub_tarea1.add_subtask(sub_sub_tarea1)
    sub_tarea1.add_subtask(sub_sub_tarea2)

    tarea_principal.add_subtask(sub_tarea1)
    tarea_principal.add_subtask(sub_tarea2)

    execute_task(tarea_principal)
