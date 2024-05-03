import nltk
from nltk.util import ngrams
from collections import defaultdict
import random

nltk.download('punkt')  # Descargar el tokenizador de NLTK
nltk.download('gutenberg')  # Descargar el corpus Gutenberg de NLTK
nltk.download('averaged_perceptron_tagger')  # Descargar el etiquetador de NLTK

# Cargar el corpus de ejemplo (Libro "Orgullo y prejuicio" de Jane Austen)
corpus = nltk.corpus.gutenberg.sents('austen-persuasion.txt')

# Crear un modelo de lenguaje basado en trigramas
model = defaultdict(lambda: defaultdict(lambda: 0))

# Construir el modelo de trigramas
for sentence in corpus:  # Iterar sobre cada oración en el corpus
    trigrams = ngrams(sentence, 3, pad_left=True, pad_right=True)  # Dividir cada oración en trigramas
    for w1, w2, w3 in trigrams:  # Iterar sobre los trigramas
        model[(w1, w2)][w3] += 1  # Contar las ocurrencias de cada trigram

# Normalizar las frecuencias
for w1_w2 in model:  # Iterar sobre cada par de palabras
    total_count = float(sum(model[w1_w2].values()))  # Calcular el número total de ocurrencias de las palabras siguientes
    for w3 in model[w1_w2]:  # Iterar sobre las palabras siguientes
        model[w1_w2][w3] /= total_count  # Normalizar las frecuencias dividiendo por el total de ocurrencias

# Función para predecir la siguiente palabra
def predict_next_word(word1, word2):
    next_word_probs = model[(word1, word2)]  # Obtener las probabilidades de las palabras siguientes dado el par de palabras actual
    if not next_word_probs:  # Verificar si no hay palabras siguientes
        return None  # Devolver None si no hay palabras siguientes en el modelo
    next_words, probs = zip(*next_word_probs.items())  # Separar las palabras siguientes y sus probabilidades
    return random.choices(next_words, probs)[0]  # Devolver una palabra siguiente seleccionada aleatoriamente según sus probabilidades

# Ejemplo de uso
current_words = ('She', 'is')  # Definir las palabras iniciales
for _ in range(10):  # Generar 10 palabras más
    next_word = predict_next_word(*current_words)  # Predecir la siguiente palabra dado el par de palabras actuales
    if next_word is None:  # Verificar si no hay palabra siguiente
        break  # Salir del bucle si no hay palabra siguiente
    print(next_word, end=' ')  # Imprimir la palabra siguiente
    current_words = (current_words[1], next_word)  # Actualizar el par de palabras actuales para la siguiente iteración
