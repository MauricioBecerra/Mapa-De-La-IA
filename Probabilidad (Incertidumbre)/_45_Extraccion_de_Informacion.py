import nltk  # Importa la biblioteca NLTK
from nltk import word_tokenize  # Importa la función word_tokenize de NLTK para dividir el texto en palabras
from nltk.corpus import stopwords  # Importa la lista de stopwords de NLTK
from nltk.stem import SnowballStemmer  # Importa SnowballStemmer de NLTK para realizar stemming
from nltk.probability import FreqDist  # Importa FreqDist de NLTK para calcular la frecuencia de las palabras

nltk.download('punkt')  # Descarga el tokenizador de NLTK
nltk.download('stopwords')  # Descarga la lista de stopwords de NLTK en español

# Define el texto de ejemplo
texto = "El aprendizaje automático está revolucionando diversos campos. En la actualidad, muchas empresas utilizan técnicas de ML para mejorar sus procesos."

# Tokeniza el texto en palabras
tokens = word_tokenize(texto.lower())

# Crea un conjunto de stopwords en español
stop_words = set(stopwords.words('spanish'))

# Filtra las stopwords y los caracteres no alfanuméricos
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

# Inicializa un objeto SnowballStemmer para realizar el stemming
stemmer = SnowballStemmer('spanish')

# Realiza stemming en las palabras filtradas
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Calcula la frecuencia de cada palabra
freq_dist = FreqDist(stemmed_tokens)

# Imprime las 5 palabras más frecuentes
print(freq_dist.most_common(5))
