from collections import defaultdict

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class PartialOrderPlanner:
    def __init__(self):
        # Creamos un diccionario para almacenar las restricciones de orden
        self.order_constraints = defaultdict(list)

    def add_order_constraint(self, before, after):
        # Añadimos una restricción de orden. 'before' debe ejecutarse antes de 'after'
        self.order_constraints[after].append(before)

    def plan(self, tasks):
        planned = set()  # Almacenamos las tareas ya planificadas
        total_duration = 0  # Duración total de las tareas planificadas
        while len(planned) < len(tasks):  # Mientras queden tareas por planificar
            for task in tasks:  # Iteramos sobre todas las tareas
                if task in planned:  # Si la tarea ya está planificada, pasamos a la siguiente
                    continue
                # Verificamos si todas las tareas previas de 'task' ya están planificadas
                if all(pre in planned for pre in self.order_constraints[task]):
                    planned.add(task)  # Si todas las tareas previas están planificadas, añadimos 'task' a las planificadas
                    total_duration += task.duration  # Incrementamos la duración total
                    yield task, total_duration  # Devolvemos la tarea y la duración acumulada

planner = PartialOrderPlanner()

# Creamos tareas con distintos nombres y duraciones
task_X = Task('X', 1)
task_Y = Task('Y', 2)
task_Z = Task('Z', 3)
task_W = Task('W', 2)
task_V = Task('V', 3)

# Establecemos restricciones de orden entre las tareas
planner.add_order_constraint(task_X, task_Y)
planner.add_order_constraint(task_Y, task_Z)
planner.add_order_constraint(task_Z, task_W)
planner.add_order_constraint(task_Z, task_V)

# Lista de tareas a planificar
tasks = [task_X, task_Y, task_Z, task_W, task_V]
# Planificamos las tareas
plan = planner.plan(tasks)

print("El plan es:")
# Mostramos las tareas y su duración acumulada en el plan
for task, total_duration in plan:
    print(f"Tarea: {task.name}, Duración acumulada: {total_duration}")
