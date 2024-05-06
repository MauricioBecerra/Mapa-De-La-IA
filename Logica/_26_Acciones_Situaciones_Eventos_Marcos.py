class Marco:
    def __init__(self, nombre, atributos=None):
        # Inicializa un nuevo marco con un nombre y atributos opcionales
        self.nombre = nombre
        # Si no se especifican atributos, se crea un diccionario vacío
        self.atributos = atributos if atributos is not None else {}

    def agregar_atributo(self, clave, valor):
        # Agrega un atributo al marco
        self.atributos[clave] = valor

    def __str__(self):
        # Devuelve una representación en cadena del marco
        return f"{self.nombre}: {self.atributos}"

class BaseConocimiento:
    def __init__(self):
        # Inicializa una nueva base de conocimiento con marcos vacíos
        self.marcos = {}

    def definir_marco(self, nombre, atributos=None):
        # Define un nuevo marco y lo agrega a la base de conocimiento
        marco = Marco(nombre, atributos)
        self.marcos[nombre] = marco

    def encontrar_marco(self, nombre):
        # Busca un marco por su nombre y lo devuelve si existe
        return self.marcos.get(nombre)

    def agregar_atributo_a_marco(self, nombre_marco, clave, valor):
        # Agrega un atributo a un marco existente
        marco = self.encontrar_marco(nombre_marco)
        if marco:
            marco.agregar_atributo(clave, valor)
        else:
            print(f"Error: Marco '{nombre_marco}' no encontrado.")

    def mostrar_marcos(self):
        # Muestra todos los marcos en la base de conocimiento
        for nombre, marco in self.marcos.items():
            print(marco)

# Creación de una base de conocimiento
bc = BaseConocimiento()

# Definición de los marcos y sus atributos
bc.definir_marco("Persona", {"nombre": "", "edad": 0, "genero": ""})
bc.definir_marco("Ciudad", {"nombre": "", "pais": ""})
bc.definir_marco("Cancion", {"titulo": "", "artista": "", "album": ""})

# Agregando atributos a los marcos
bc.agregar_atributo_a_marco("Persona", "nombre", "Juan")
bc.agregar_atributo_a_marco("Persona", "edad", 30)
bc.agregar_atributo_a_marco("Persona", "genero", "Masculino")

bc.agregar_atributo_a_marco("Ciudad", "nombre", "Nueva York")
bc.agregar_atributo_a_marco("Ciudad", "pais", "Estados Unidos")

bc.agregar_atributo_a_marco("Cancion", "titulo", "Bohemian Rhapsody")
bc.agregar_atributo_a_marco("Cancion", "artista", "Queen")
bc.agregar_atributo_a_marco("Cancion", "album", "A Night at the Opera")

# Mostrando los marcos en la base de conocimiento
bc.mostrar_marcos()
