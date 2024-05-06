class Taxonomy:
    def __init__(self):
        # Inicializa una nueva taxonomía vacía
        self.categories = {}

    def add_category(self, category, parent=None):
        # Agrega una categoría a la taxonomía, opcionalmente especificando su padre
        if category not in self.categories:
            # Si la categoría no existe, crea un nuevo conjunto vacío para ella
            self.categories[category] = set()
        if parent:
            # Si se especifica un padre, agrega la categoría como subcategoría del padre
            if parent not in self.categories:
                # Si el padre no existe, crea un nuevo conjunto vacío para él
                self.categories[parent] = set()
            # Agrega la categoría como subcategoría del padre
            self.categories[parent].add(category)

    def get_subcategories(self, category):
        # Obtiene las subcategorías de una categoría dada
        if category in self.categories:
            # Si la categoría existe, devuelve sus subcategorías
            return self.categories[category]
        else:
            # Si la categoría no existe, devuelve un conjunto vacío
            return set()

# Creación de la taxonomía
taxonomy = Taxonomy()

# Agregar categorías a la taxonomía
taxonomy.add_category("Animal")
taxonomy.add_category("Mamífero", parent="Animal")
taxonomy.add_category("Reptil", parent="Animal")
taxonomy.add_category("Perro", parent="Mamífero")
taxonomy.add_category("Gato", parent="Mamífero")
taxonomy.add_category("Lagarto", parent="Reptil")

# Consultas de subcategorías
print("Subcategorías de Animal:", taxonomy.get_subcategories("Animal"))
print("Subcategorías de Mamífero:", taxonomy.get_subcategories("Mamífero"))
print("Subcategorías de Reptil:", taxonomy.get_subcategories("Reptil"))
