class MundoTemporal:
    def __init__(self, nombre, eventos=None):
        self.nombre = nombre
        self.eventos = eventos if eventos else []  # Inicializa la lista de eventos del mundo

    def agregar_evento(self, evento):
        self.eventos.append(evento)  # Agrega un evento a la lista de eventos del mundo

class AgenteTemporal:
    def __init__(self, nombre, mundo_actual):
        self.nombre = nombre
        self.mundo_actual = mundo_actual  # Establece el mundo actual del agente

    def ejecutar_evento(self, evento):
        if evento in self.mundo_actual.eventos:  # Verifica si el evento está en los eventos del mundo actual
            print(f"{self.nombre} ejecuta el evento {evento}")  # Si el evento está, lo ejecuta
        else:
            print(f"¡Error! {self.nombre} no puede ejecutar el evento {evento}")  # Si no está, imprime un error

# Creamos dos instancias de MundoTemporal
mundo_actual = MundoTemporal("Mundo Actual", ["evento1", "evento2"])
mundo_futuro = MundoTemporal("Mundo Futuro")

# Creamos una instancia de AgenteTemporal y lo ubicamos en el mundo_actual
agente_temporal = AgenteTemporal("Agente Temporal", mundo_actual)

# El agente ejecuta algunos eventos
agente_temporal.ejecutar_evento("evento1")  # El evento "evento1" está en el mundo actual, entonces se ejecuta
agente_temporal.ejecutar_evento("evento3")  # El evento "evento3" no está en el mundo actual, entonces se muestra un error
