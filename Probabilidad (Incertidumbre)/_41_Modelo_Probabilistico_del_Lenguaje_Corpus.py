from collections import defaultdict

class ModeloLenguajeNgram:
    def __init__(self, corpus, n):
        self.n = n  # Define el tamaño del n-grama
        self.contadores = defaultdict(int)  # Diccionario para contar frecuencias de n-gramas
        self.contadores_contexto = defaultdict(int)  # Diccionario para contar frecuencias de contextos
        self.entrenar(corpus)  # Entrenar el modelo con el corpus proporcionado

    def entrenar(self, corpus):
        for oracion in corpus:  # Iterar sobre cada oración en el corpus
            tokens = ['<s>'] * (self.n - 1) + oracion + ['</s>']  # Agregar marcadores de inicio y fin de oración
            for i in range(self.n - 1, len(tokens)):  # Iterar sobre los índices del corpus
                contexto = tuple(tokens[i - self.n + 1:i])  # Definir el contexto del n-grama actual
                palabra = tokens[i]  # Obtener la palabra actual del corpus
                self.contadores[(contexto, palabra)] += 1  # Incrementar el contador del n-grama específico
                self.contadores_contexto[contexto] += 1  # Incrementar el contador del contexto

    def probabilidad(self, contexto, palabra):
        return self.contadores[(contexto, palabra)] / self.contadores_contexto[contexto]  # Calcular la probabilidad de la palabra dado el contexto

# Ejemplo de corpus de texto
corpus = [
    ['la', 'casa', 'es', 'grande'],  # Primera oración del corpus
    ['el', 'árbol', 'es', 'verde'],  # Segunda oración del corpus
    ['el', 'sol', 'es', 'brillante']  # Tercera oración del corpus
]

# Crear y entrenar el modelo de lenguaje con trigramas
modelo = ModeloLenguajeNgram(corpus, n=3)  # Crear una instancia del modelo de lenguaje N-gram con n=3

# Calcular la probabilidad de una palabra dado un contexto
contexto = ('el', 'árbol')  # Definir el contexto
palabra = 'es'  # Definir la palabra
probabilidad = modelo.probabilidad(contexto, palabra)  # Calcular la probabilidad de la palabra dado el contexto
print(f"La probabilidad de '{palabra}' dado '{' '.join(contexto)}' es: {probabilidad:.4f}")  # Imprimir la probabilidad calculada
