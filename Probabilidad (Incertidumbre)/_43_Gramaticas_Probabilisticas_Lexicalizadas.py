import nltk  # Importa la biblioteca NLTK (Natural Language Toolkit)
from nltk import PCFG  # Importa la clase PCFG para crear Gramáticas Probabilísticas Independientes del Contexto
from nltk import ViterbiParser  # Importa el parser Viterbi para el análisis sintáctico

# Define a probabilistic context-free grammar
pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.8] | VP PP [0.2]
    PP -> P NP [1.0]
    V -> "saw" [0.3] | "ate" [0.7]
    NP -> "John" [0.4] | "Mary" [0.5] | "Bob" [0.1]
    P -> "with" [0.8] | "in" [0.2]
""")

# Create a Viterbi parser with the grammar
parser = ViterbiParser(pcfg_grammar)

# Example sentence to parse
sentence = "Mary saw John with Bob"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform syntactic parsing
trees = parser.parse(tokens)

# Print the possible syntactic analysis trees
for tree in trees:
    print(tree)
