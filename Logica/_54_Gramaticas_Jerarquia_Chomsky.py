import re

# Definición de tokens utilizando expresiones regulares
tokens = [
    ('NUMERO', r'\d+'),            # Token para números enteros
    ('SUMA', r'\+'),                # Token para suma
    ('RESTA', r'\-'),               # Token para resta
    ('MULTIPLICACION', r'\*'),      # Token para multiplicación
    ('DIVISION', r'\/'),            # Token para división
    ('ESPACIO', r'\s+'),            # Token para espacios en blanco
]

# Función para realizar el análisis léxico
def lexico(cadena):
    indice = 0               # Índice para recorrer la cadena
    resultado = []           # Lista para almacenar los tokens encontrados
    while indice < len(cadena):
        coincidencia = None              # Almacena la coincidencia
        for token in tokens:
            tipo, patron = token         # Se obtiene el tipo y el patrón del token
            regex = re.compile(patron)  # Se crea una expresión regular a partir del patrón
            coincidencia = regex.match(cadena, indice)  # Se intenta hacer match con la cadena
            if coincidencia:             # Si hay coincidencia
                valor = coincidencia.group(0)  # Se obtiene el valor del token encontrado
                if tipo != 'ESPACIO':    # Si no es un espacio, se agrega a los resultados
                    resultado.append((tipo, valor))
                break
        if not coincidencia:            # Si no hay coincidencia, se informa y se detiene el análisis
            print("Caracter no reconocido:", cadena[indice])
            break
        else:
            indice = coincidencia.end()  # Se actualiza el índice para continuar desde donde se quedó
    return resultado

# Ejemplo de uso
entrada = "3 + 4 * 2"
resultado = lexico(entrada)
print(resultado)
