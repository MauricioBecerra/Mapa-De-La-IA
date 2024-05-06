# Definición de tokens
tokens = [
    ('VALOR', r'\d+'),             # Token para valores numéricos
    ('SUMA', r'\+'),                # Token para la operación de suma
    ('RESTA', r'\-'),               # Token para la operación de resta
    ('PRODUCTO', r'\*'),            # Token para la operación de multiplicación
    ('DIVISION', r'\/'),            # Token para la operación de división
    ('PARENTESIS_IZQ', r'\('),      # Token para el paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),      # Token para el paréntesis derecho
]

# Función para realizar el análisis sintáctico
def parse(tokens):
    # Función interna para manejar los factores
    def factor():
        token = tokens.pop(0)                # Toma el primer token
        if token[0] == 'VALOR':              # Si el token es un valor numérico
            return float(token[1])           # Convierte y devuelve el valor numérico
        elif token[0] == 'PARENTESIS_IZQ':   # Si el token es un paréntesis izquierdo
            resultado = expression()         # Evalúa la expresión dentro de los paréntesis
            tokens.pop(0)                    # Remueve el paréntesis derecho
            return resultado

    # Función interna para manejar los términos
    def term():
        resultado = factor()                   # Obtiene el primer factor
        while tokens and tokens[0][0] in ('PRODUCTO', 'DIVISION'):  # Mientras hay tokens de multiplicación o división
            operador = tokens.pop(0)           # Toma el operador
            if operador[0] == 'PRODUCTO':     # Si es multiplicación
                resultado *= factor()          # Multiplica por el siguiente factor
            else:                              # Si es división
                divisor = factor()             # Toma el divisor
                if divisor != 0:               # Evita la división por cero
                    resultado /= divisor       # Realiza la división
                else:
                    raise ValueError("División por cero no permitida")
        return resultado

    # Función interna para manejar las expresiones
    def expression():
        resultado = term()                # Obtiene el primer término
        while tokens and tokens[0][0] in ('SUMA', 'RESTA'):  # Mientras hay tokens de suma o resta
            operador = tokens.pop(0)      # Toma el operador
            if operador[0] == 'SUMA':     # Si es suma
                resultado += term()       # Suma el siguiente término
            else:                          # Si es resta
                resultado -= term()       # Resta el siguiente término
        return resultado

    return expression()  

# Ejemplo de uso
entrada = "5 * (7 - 2) / 2"   # Nueva expresión matemática
tokens = [('VALOR', '5'), ('PRODUCTO', '*'), ('PARENTESIS_IZQ', '('), 
          ('VALOR', '7'), ('RESTA', '-'), ('VALOR', '2'), ('PARENTESIS_DER', ')'),
          ('DIVISION', '/'), ('VALOR', '2')]
resultado = parse(tokens)     # Parsea la expresión
print("El resultado de la expresión es:", resultado)  # Imprime el resultado
