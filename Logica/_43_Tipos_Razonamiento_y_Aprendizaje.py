class Animal:
    def __init__(self, nombre, tipo, pelo, patas):
        # Inicializa un objeto Animal con nombre, tipo, si tiene pelo y número de patas
        self.nombre = nombre
        self.tipo = tipo
        self.pelo = pelo
        self.patas = patas

# Datos de entrenamiento
animales_entrenamiento = [
    Animal("León", "mamífero", True, 4),  # Ejemplo de mamífero: león
    Animal("Águila", "ave", False, 2),    # Ejemplo de ave: águila
    Animal("Tiburón", "pez", False, 0),   # Ejemplo de pez: tiburón
    Animal("Elefante", "mamífero", True, 4),  # Ejemplo de mamífero: elefante
    Animal("Canguro", "mamífero", True, 2),   # Ejemplo de mamífero: canguro
    Animal("Serpiente", "reptil", False, 0)   # Ejemplo de reptil: serpiente
]

# Función para determinar si un animal es un mamífero basado en características
def es_mamifero(animal):
    # Determina si el animal tiene pelo y 4 patas
    return animal.pelo and animal.patas == 4

# Algoritmo de aprendizaje inductivo
def aprendizaje_inductivo(animales):
    # Identifica los animales que son mamíferos en base a la función es_mamifero
    mamiferos_identificados = []
    for animal in animales:
        if es_mamifero(animal):
            mamiferos_identificados.append(animal.nombre)
    return mamiferos_identificados

# Función para mostrar resultados
def mostrar_resultados(mamiferos_identificados):
    # Muestra los animales identificados como mamíferos
    if len(mamiferos_identificados) > 0:
        print("Los siguientes animales son identificados como mamíferos:")
        for animal in mamiferos_identificados:
            print("- " + animal)
    else:
        print("No se identificaron mamíferos en el conjunto de datos de entrada.")

# Ejecución del programa
mamiferos_identificados = aprendizaje_inductivo(animales_entrenamiento)
mostrar_resultados(mamiferos_identificados)
