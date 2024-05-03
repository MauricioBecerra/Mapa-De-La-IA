from collections import defaultdict
import random

class PCFG:  # Definición de la clase PCFG (Gramática Probabilística Independiente del Contexto)
    def __init__(self):  # Método de inicialización de la clase
        self.rules = defaultdict(list)  # Diccionario para almacenar las reglas de producción con listas vacías por defecto
        self.start_symbol = None  # Símbolo inicial de la gramática

    def add_rule(self, left, right, probability):  # Método para agregar una regla de producción
        self.rules[left].append((right, probability))  # Agrega la regla de producción al diccionario

    def set_start_symbol(self, start_symbol):  # Método para establecer el símbolo inicial
        self.start_symbol = start_symbol  # Asigna el símbolo inicial

    def generate_sentence(self):  # Método para generar una oración aleatoria
        return self.expand(self.start_symbol)  # Llama al método expandir con el símbolo inicial como argumento

    def expand(self, symbol):  # Método para expandir un símbolo en una oración
        expansions = self.rules.get(symbol, [])  # Obtiene las expansiones posibles del símbolo
        if not expansions:  # Si no hay expansiones posibles
            return [symbol]  # Retorna el símbolo como una palabra terminal
        right, probabilities = zip(*expansions)  # Separa las reglas de producción y las probabilidades en listas
        chosen_right = random.choices(right, probabilities)[0]  # Elige una regla de producción según las probabilidades
        return sum((self.expand(s) for s in chosen_right), [])  # Expande recursivamente cada símbolo en la regla

pcfg = PCFG()  # Crea una instancia de la clase PCFG
pcfg.add_rule('S', ['NP', 'VP'], 0.7)  # Agrega una regla de producción para S
pcfg.add_rule('S', ['Aux', 'NP', 'VP'], 0.3)  # Agrega otra regla de producción para S
pcfg.add_rule('NP', ['Det', 'N'], 0.6)  # Agrega una regla de producción para NP
pcfg.add_rule('NP', ['Det', 'Adj', 'N'], 0.4)  # Agrega otra regla de producción para NP
pcfg.add_rule('VP', ['V', 'NP'], 0.8)  # Agrega una regla de producción para VP
pcfg.add_rule('VP', ['V', 'NP', 'PP'], 0.2)  # Agrega otra regla de producción para VP
pcfg.add_rule('PP', ['P', 'NP'], 1.0)  # Agrega una regla de producción para PP
pcfg.add_rule('Det', ['the'], 0.6)  # Agrega una regla de producción para Det
pcfg.add_rule('Det', ['a'], 0.4)  # Agrega otra regla de producción para Det
pcfg.add_rule('N', ['man'], 0.5)  # Agrega una regla de producción para N
pcfg.add_rule('N', ['woman'], 0.5)  # Agrega otra regla de producción para N
pcfg.add_rule('Adj', ['big'], 0.7)  # Agrega una regla de producción para Adj
pcfg.add_rule('Adj', ['small'], 0.3)  # Agrega otra regla de producción para Adj
pcfg.add_rule('V', ['ate'], 0.4)  # Agrega una regla de producción para V
pcfg.add_rule('V', ['saw'], 0.3)  # Agrega otra regla de producción para V
pcfg.add_rule('V', ['walked'], 0.3)  # Agrega otra regla de producción para V
pcfg.add_rule('P', ['with'], 0.6)  # Agrega una regla de producción para P
pcfg.add_rule('P', ['in'], 0.4)  # Agrega otra regla de producción para P

pcfg.set_start_symbol('S')  # Establece el símbolo inicial como 'S'
sentence = pcfg.generate_sentence()  # Genera una oración aleatoria
print(' '.join(sentence))  # Imprime la oración generada como una cadena de texto
