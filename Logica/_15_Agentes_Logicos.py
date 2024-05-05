class AgenteLogico:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento  # Inicializa la base de conocimiento del agente

    def inferir(self, consulta):
        if consulta in self.base_conocimiento:  # Comprueba si la consulta está en la base de conocimiento
            return True  # Devuelve Verdadero si la consulta está en la base de conocimiento
        else:
            return False  # Devuelve Falso si la consulta no está en la base de conocimiento

if __name__ == "__main__":
    # Definimos la base de conocimiento
    base_conocimiento = {
        "Hombre(Juan)",
        "Mujer(María)",
        "Padre(Juan, Pedro)",
        "Madre(María, Pedro)",
        "Padre(Juan, Ana)",
        "Madre(María, Ana)"
    }

    # Creamos una instancia del agente lógico con la base de conocimiento definida
    agente = AgenteLogico(base_conocimiento)

    # Definimos consultas
    consulta1 = "Hombre(Juan)"
    consulta2 = "Padre(Juan, Pedro)"
    consulta3 = "Hombre(María)"

    # Realizamos las consultas al agente y obtenemos los resultados
    resultado1 = agente.inferir(consulta1)
    resultado2 = agente.inferir(consulta2)
    resultado3 = agente.inferir(consulta3)

    # Imprimimos los resultados de las consultas
    print(f"¿{consulta1}? {resultado1}")
    print(f"¿{consulta2}? {resultado2}")
    print(f"¿{consulta3}? {resultado3}")