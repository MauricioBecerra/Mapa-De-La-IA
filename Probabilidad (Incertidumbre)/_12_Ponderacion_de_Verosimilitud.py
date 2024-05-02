import random  # Importa la biblioteca random para generar números aleatorios

def lanzar_moneda(probabilidad_caras):
    # Función para simular el lanzamiento de una moneda sesgada hacia caras
    if random.random() < probabilidad_caras:  # Genera un número aleatorio en [0,1) y compara con la probabilidad de caras
        return True  # Si el número es menor, devuelve True (cara)
    else:
        return False  # Si el número es mayor o igual, devuelve False (cruz)

def calcular_verosimilitud(datos, probabilidad_caras):
    # Calcula la verosimilitud de una secuencia de lanzamientos de moneda con una cierta probabilidad de cara
    verosimilitud = 1.0  # Inicializa la verosimilitud en 1
    for resultado in datos:  # Itera sobre los resultados de los lanzamientos
        if resultado:  # Si el resultado es True (cara)
            verosimilitud *= probabilidad_caras  # Multiplica la verosimilitud por la probabilidad de cara
        else:  # Si el resultado es False (cruz)
            verosimilitud *= 1 - probabilidad_caras  # Multiplica la verosimilitud por la probabilidad de cruz
    return verosimilitud  # Devuelve la verosimilitud calculada

def actualizar_probabilidad_a_posteriori(prob_previa, verosimilitud, constante_de_normalizacion):
    # Actualiza la probabilidad a posteriori utilizando la ponderación de verosimilitud
    return (prob_previa * verosimilitud) / constante_de_normalizacion  # Calcula la probabilidad a posteriori

prob_previa = 0.5  # Probabilidad a priori de que la moneda sea justa
prob_real_caras = 0.6  # Probabilidad real de que la moneda salga cara
num_lanzamientos = 10  # Número de lanzamientos de la moneda

# Simula una secuencia de lanzamientos de la moneda
datos_observados = [lanzar_moneda(prob_real_caras) for _ in range(num_lanzamientos)]
# Calcula la verosimilitud de los datos observados
verosimilitud = calcular_verosimilitud(datos_observados, prob_real_caras)
# Calcula la constante de normalización
constante_de_normalizacion = verosimilitud * prob_previa + (1 - verosimilitud) * (1 - prob_previa)
# Actualiza la probabilidad a posteriori
prob_posteriori = actualizar_probabilidad_a_posteriori(prob_previa, verosimilitud, constante_de_normalizacion)

# Imprime los resultados
print("Secuencia de lanzamientos observada: ", datos_observados)
print("Verosimilitud de los datos observados: ", verosimilitud)
print("Probabilidad a posteriori de que la moneda sea justa: ", prob_posteriori)
