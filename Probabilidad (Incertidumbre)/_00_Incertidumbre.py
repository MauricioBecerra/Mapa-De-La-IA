import random  # Importa el módulo random para generar números aleatorios

def lanzamiento_moneda():
    resultado = random.choice(['Aguila', 'Sello'])  # Elige aleatoriamente entre 'Aguila' y 'Sello'
    return resultado

def calcular_probabilidad(n_lanzamientos, resultado_deseado):
    conteo_resultado_deseado = 0  # Inicializa el conteo de resultados deseados
    for _ in range(n_lanzamientos):
        resultado = lanzamiento_moneda()  # Realiza un lanzamiento de moneda
        if resultado == resultado_deseado:  # Comprueba si el resultado es el deseado
            conteo_resultado_deseado += 1  # Incrementa el conteo de resultados deseados
    
    probabilidad = conteo_resultado_deseado / n_lanzamientos  # Calcula la probabilidad
    return probabilidad

# Parámetros del juego
n_lanzamientos = 1000  # Número de lanzamientos
resultado_deseado = 'Aguila'  # Resultado deseado ('Aguila' en este caso)

# Calcula la probabilidad de obtener 'Aguila' en n_lanzamientos
probabilidad_cara = calcular_probabilidad(n_lanzamientos, resultado_deseado)

# Imprime el resultado
print(f"Después de {n_lanzamientos} lanzamientos, la probabilidad de obtener '{resultado_deseado}' es: {probabilidad_cara}")
