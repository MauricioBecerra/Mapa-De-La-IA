class SemanticAnalyzer:  
    def __init__(self):  
        self.keywords = {  
            'leer': 'acción de comprender texto escrito',  
            'dormir': 'estado de reposo del organismo',  
            'pintar': 'aplicar color o pigmento sobre una superficie',  
            'felicidad': 'estado emocional positivo',  
            'tristeza': 'estado emocional negativo'  
        }

    def analyze_sentence(self, sentence):  
        found_keywords = []  

        for word in sentence.split():  
            if word.lower() in self.keywords:  
                found_keywords.append((word, self.keywords[word.lower()]))

        return found_keywords  

# Ejemplo de uso
analyzer = SemanticAnalyzer()  
sentence = "Me gusta leer antes de dormir porque me da felicidad."  
analysis_result = analyzer.analyze_sentence(sentence)  

print("Análisis Semántico:")  
for keyword, meaning in analysis_result:  
    print(f"Palabra clave: {keyword}, Significado: {meaning}")  
