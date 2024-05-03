import nltk  # Importa la librería NLTK para el procesamiento del lenguaje natural
import numpy as np  # Importa la librería NumPy para operaciones numéricas eficientes

# Descargar los recursos necesarios de NLTK (solo si no los tienes descargados ya)
nltk.download('punkt')  # Descarga los recursos de tokenización
nltk.download('averaged_perceptron_tagger')  # Descarga los recursos de etiquetado POS

# Datos de entrenamiento (frases en dos idiomas)
sentences_fr = [  # Frases en francés
    "une chaise",
    "une table",
    "ta table",
    "ma chaise",
    "sa table",
    "et"
]

sentences_de = [  # Frases en alemán
    "ein Stuhl",
    "ein Tisch",
    "dein Tisch",
    "mein Stuhl",
    "sein Tisch",
    "und"
]

# Tokenización y etiquetado POS (Part-of-Speech) de las frases
fr_tokens = [nltk.word_tokenize(sent) for sent in sentences_fr]  # Tokeniza las frases en francés
de_tokens = [nltk.word_tokenize(sent) for sent in sentences_de]  # Tokeniza las frases en alemán

fr_tagged = [nltk.pos_tag(tokens) for tokens in fr_tokens]  # Etiqueta POS las frases en francés
de_tagged = [nltk.pos_tag(tokens) for tokens in de_tokens]  # Etiqueta POS las frases en alemán

# Crear diccionarios de palabras y etiquetas
fr_words = set(word for sent in fr_tokens for word in sent)  # Crea un conjunto de palabras en francés
de_words = set(word for sent in de_tokens for word in sent)  # Crea un conjunto de palabras en alemán

# Crear matrices de probabilidades de traducción de palabras
translation_probs = np.zeros((len(fr_words), len(de_words)))  # Crea una matriz de ceros para las probabilidades de traducción

# Calcular las probabilidades de traducción
for fr_sent, de_sent in zip(fr_tagged, de_tagged):  # Recorre las frases etiquetadas en francés y alemán
    for (fr_word, fr_tag), (de_word, de_tag) in zip(fr_sent, de_sent):  # Recorre las palabras y etiquetas en ambas frases
        fr_index = list(fr_words).index(fr_word)  # Obtiene el índice de la palabra en francés
        de_index = list(de_words).index(de_word)  # Obtiene el índice de la palabra en alemán
        translation_probs[fr_index, de_index] += 1  # Incrementa la cuenta de la traducción

# Normalizar las probabilidades
translation_probs /= translation_probs.sum(axis=1, keepdims=True)  # Normaliza las probabilidades de traducción

# Función para traducir una frase de francés a alemán
def translate(sentence):
    tokens = nltk.word_tokenize(sentence)  # Tokeniza la frase de entrada
    tagged = nltk.pos_tag(tokens)  # Etiqueta POS las palabras de la frase
    translation = []  # Inicializa la lista de traducción

    for token, tag in tagged:  # Recorre las palabras y etiquetas de la frase etiquetada
        fr_index = list(fr_words).index(token)  # Obtiene el índice de la palabra en francés
        de_index = np.argmax(translation_probs[fr_index])  # Obtiene el índice de la traducción con mayor probabilidad
        translation.append(list(de_words)[de_index])  # Agrega la palabra traducida a la lista de traducción

    return " ".join(translation)  # Devuelve la traducción como una cadena de texto

# Ejemplo de uso
input_sentence = "une chaise et une table"  # Definición de la frase de entrada en francés
output_sentence = translate(input_sentence)  # Traducción de la frase de entrada
print("Input:", input_sentence)  # Imprime la frase de entrada
print("Translated:", output_sentence)  # Imprime la traducción de la frase
