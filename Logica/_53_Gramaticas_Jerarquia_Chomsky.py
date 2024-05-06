import re
import random

class RegularGrammar:
    def __init__(self, productions):
        self.productions = productions

    def generate_random_string(self, start_symbol, max_length=10):
        string = ""
        current_symbol = start_symbol

        while len(string) < max_length:
            if current_symbol not in self.productions:
                break
            production = random.choice(self.productions[current_symbol])
            string += production[1]
            current_symbol = production[0]

        return string

    def is_valid(self, string, start_symbol):
        stack = [(start_symbol, 0)]

        while stack:
            symbol, index = stack.pop()
            if index == len(string):
                if symbol == start_symbol:
                    return True
                continue

            if symbol in self.productions:
                productions = self.productions[symbol]
                for production in productions:
                    if string[index:].startswith(production[1]):
                        for char in reversed(production[0]):
                            stack.append((char, index))
                        stack.append((symbol, index + len(production[1])))
                        break
                else:
                    continue
            elif symbol == string[index]:
                stack.append((start_symbol, index + 1))

        return False

# Nuevo ejemplo de gramática regular
productions = {
    'S': [('A', '0'), ('B', '1')],
    'A': [('A', '0'), ('B', '1')],
    'B': [('S', '0'), ('B', '1')]
}

grammar = RegularGrammar(productions)

print("Producciones de la gramática:")
for symbol, productions in productions.items():
    print(f"{symbol} -> {' | '.join([f'{x[0]}{x[1]}' for x in productions])}")

# Generar una cadena aleatoria
random_string = grammar.generate_random_string('S')
print("\nCadena generada aleatoriamente:", random_string)

# Comprobar si una cadena es válida
test_string = "001110"
if grammar.is_valid(test_string, 'S'):
    print("\nLa cadena es válida.")
else:
    print("\nLa cadena no es válida.")
