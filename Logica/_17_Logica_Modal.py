class Mundo:
    def __init__(self, nombre, accesible=None):
        self.nombre = nombre
        self.accesible = accesible if accesible else []  # Lista de mundos accesibles desde este mundo

    def agregar_accesible(self, mundo):
        self.accesible.append(mundo)  # Agrega un mundo accesible a la lista de accesibles

class Agente:
    def __init__(self, nombre, mundo_actual):
        self.nombre = nombre
        self.mundo_actual = mundo_actual  # Mundo en el que se encuentra el agente

    def ir_a_mundo(self, mundo):
        if mundo in self.mundo_actual.accesible:  # Verifica si el mundo al que se quiere mover es accesible desde el mundo actual
            self.mundo_actual = mundo  # Cambia el mundo actual del agente al mundo especificado
            print(f"{self.nombre} se mueve al mundo {mundo.nombre}")  # Imprime un mensaje indicando el movimiento del agente
        else:
            print(f"¡Error! {self.nombre} no puede ir al mundo {mundo.nombre}")  # Imprime un mensaje de error si el mundo no es accesible

# Creamos tres mundos
mundo1 = Mundo("Mundo 1")
mundo2 = Mundo("Mundo 2")
mundo3 = Mundo("Mundo 3")

# Establecemos las relaciones de accesibilidad entre los mundos
mundo1.agregar_accesible(mundo2)
mundo2.agregar_accesible(mundo3)
mundo3.agregar_accesible(mundo1)

# Creamos un agente y lo ubicamos en el mundo1
agente1 = Agente("Agente 1", mundo1)

# El agente se mueve a través de los mundos
agente1.ir_a_mundo(mundo2)
agente1.ir_a_mundo(mundo3)
agente1.ir_a_mundo(mundo1)
