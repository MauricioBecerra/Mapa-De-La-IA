class GrammarInduction:  
    def __init__(self):  
        self.examples = []  
        # Inicializa una lista para almacenar los ejemplos.

    def add_example(self, example):  
        self.examples.append(example)  
        # Agrega un nuevo ejemplo a la lista.

    def induce_grammar(self):  
        if not self.examples:  
            return "No hay ejemplos para inducir la gramática."  
        # Verifica si hay ejemplos. Si no hay, devuelve un mensaje indicando que no hay ejemplos.

        grammar = {}  
        # Inicializa un diccionario para almacenar la gramática.

        for example in self.examples:  
            # Itera sobre cada ejemplo.

            words = example.split()  
            # Divide el ejemplo en palabras.

            for i in range(len(words) - 1):  
                # Itera sobre cada par de palabras en el ejemplo.

                current_word = words[i]  
                next_word = words[i + 1]  
                # Obtiene la palabra actual y la siguiente.

                if current_word not in grammar:  
                    grammar[current_word] = []  
                    # Si la palabra actual no está en la gramática, la agrega.

                if next_word not in grammar[current_word]:  
                    grammar[current_word].append(next_word)  
                    # Si la siguiente palabra no está en la lista de palabras siguientes de la palabra actual, la agrega.

        return grammar  
        # Devuelve la gramática inducida.

# Ejemplo de uso
inductor = GrammarInduction()  
# Crea una instancia de GrammarInduction.

inductor.add_example("El perro corre rápidamente")
inductor.add_example("La niña juega felizmente")

grammar = inductor.induce_grammar()
# Induce la gramática a partir de los ejemplos.

print("Gramática Inducida:")
for key, value in grammar.items():
    print(f"{key} -> {' | '.join(value)}")
    # Imprime la gramática inducida.
