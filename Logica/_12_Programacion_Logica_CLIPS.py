class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # Asigna el nombre de la persona
        self.padres = []  # Inicializa la lista de padres como vacía

    def agregar_padre(self, padre):
        self.padres.append(padre)  # Agrega un padre a la lista de padres de la persona

    def __str__(self):
        return self.nombre  # Devuelve el nombre de la persona al imprimir el objeto

def main():
    # Creamos instancias de Persona
    juan = Persona("Juan")
    maria = Persona("Maria")

    juan.agregar_padre(maria)  # Asignamos a María como padre de Juan

    for persona in [juan, maria]:
        if len(persona.padres) > 0:  # Si la lista de padres de la persona no está vacía
            print(f"{persona} tiene padres.")  # Imprime que la persona tiene padres
        else:
            print(f"{persona} no tiene padres.")  # Imprime que la persona no tiene padres

if __name__ == "__main__":
    main()
