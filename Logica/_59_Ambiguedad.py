class AmbiguityResolver:  
    def __init__(self):  
        pass  
    # Define la clase AmbiguityResolver con un método constructor que no hace nada.

    def resolve_ambiguity(self, sentence):  
        interpretations = []  
        # Inicializa una lista para almacenar las interpretaciones de la oración.

        interpretation_1 = "Vi a la mujer con el sombrero rojo."
        interpretations.append(interpretation_1)  
        # Define la primera interpretación y la agrega a la lista de interpretaciones.

        interpretation_2 = "Vi a la mujer que estaba hablando por teléfono."
        interpretations.append(interpretation_2)  
        # Define la segunda interpretación y la agrega a la lista de interpretaciones.

        return interpretations  
        # Devuelve la lista de interpretaciones.

# Ejemplo de uso
resolver = AmbiguityResolver()  
# Crea una instancia de la clase AmbiguityResolver.

ambiguous_sentence = "Vi a la mujer con el teléfono."  
# Define una oración ambigua.

interpretations = resolver.resolve_ambiguity(ambiguous_sentence)  
# Resuelve la ambigüedad de la oración y obtiene las interpretaciones.

print("Frase ambigua:", ambiguous_sentence)  
# Imprime la oración ambigua.

print("Interpretaciones:")  
# Imprime la lista de interpretaciones.

for i, interpretation in enumerate(interpretations, start=1):  
    # Itera sobre cada interpretación enumerándola desde 1.

    print(f"Interpretación {i}: {interpretation}")  
    # Imprime cada interpretación con su número correspondiente.
