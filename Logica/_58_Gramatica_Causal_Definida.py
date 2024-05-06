import random  

class CausalGrammar:  
    def __init__(self):  
        self.subjects = ['El estudiante', 'La maestra', 'El científico', 'El músico', 'El artista']
        self.verbs = ['leyó', 'escribió', 'creó', 'descubrió', 'interpretó']
        self.objects = ['el libro', 'la partitura', 'la fórmula', 'el experimento', 'la obra']

    def generate_sentence(self):  
        subject = random.choice(self.subjects)  
        verb = random.choice(self.verbs)  
        obj = random.choice(self.objects)  

        return f"{subject} {verb} {obj} porque {self._generate_cause()}."  

    def _generate_cause(self):  
        causes = [
            "quería aprender más",
            "buscaba inspiración",
            "necesitaba una respuesta",
            "sintió curiosidad",
            "se sintió motivado"
        ]
        return random.choice(causes)  

# Ejemplo de uso
grammar = CausalGrammar()  

for _ in range(5):  
    sentence = grammar.generate_sentence()  
    print(sentence)  
