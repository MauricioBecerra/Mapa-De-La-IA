import math  # Importa el módulo de matemáticas para utilizar funciones matemáticas

class Nodo:
    def __init__(self, valor):
        # Inicializa un nodo con un valor y una lista vacía de hijos
        self.valor = valor
        self.hijos = {}

def calcular_entropia(data):
    # Calcula la entropía de los datos de acuerdo a las etiquetas
    etiquetas = {}
    for item in data:
        etiqueta = item[-1]
        if etiqueta not in etiquetas:
            etiquetas[etiqueta] = 0
        etiquetas[etiqueta] += 1

    entropia = 0.0
    for etiqueta in etiquetas:
        probabilidad = etiquetas[etiqueta] / len(data)
        entropia -= probabilidad * math.log2(probabilidad)

    return entropia

def dividir_data(data, atributo_idx):
    # Divide los datos según el valor del atributo en el índice dado
    data_dividida = {}
    for item in data:
        atributo_valor = item[atributo_idx]
        if atributo_valor not in data_dividida:
            data_dividida[atributo_valor] = []
        data_dividida[atributo_valor].append(item)
    return data_dividida

def encontrar_mejor_atributo(data, atributos):
    # Encuentra el mejor atributo para dividir los datos
    entropia_inicial = calcular_entropia(data)
    mejor_ganancia_info = 0.0
    mejor_atributo = None
    for i in range(len(atributos)):
        atributo_valores = set([item[i] for item in data])
        entropia_nueva = 0.0
        for valor in atributo_valores:
            data_dividida = dividir_data(data, i)
            probabilidad = len(data_dividida[valor]) / len(data)
            entropia_nueva += probabilidad * calcular_entropia(data_dividida[valor])
        ganancia_info = entropia_inicial - entropia_nueva
        if ganancia_info > mejor_ganancia_info:
            mejor_ganancia_info = ganancia_info
            mejor_atributo = i
    return mejor_atributo

def construir_arbol_decision(data, atributos, etiquetas):
    # Construye un árbol de decisión recursivamente
    etiquetas_data = [item[-1] for item in data]
    if len(set(etiquetas_data)) == 1:
        return Nodo(etiquetas_data[0])

    if len(atributos) == 0:
        etiqueta_mas_comun = max(set(etiquetas_data), key=etiquetas_data.count)
        return Nodo(etiqueta_mas_comun)

    mejor_atributo_idx = encontrar_mejor_atributo(data, atributos)
    mejor_atributo = atributos[mejor_atributo_idx]

    nodo = Nodo(mejor_atributo)
    atributos_restantes = atributos[:mejor_atributo_idx] + atributos[mejor_atributo_idx+1:]
    atributo_valores = set([item[mejor_atributo_idx] for item in data])
    for valor in atributo_valores:
        data_dividida = [item for item in data if item[mejor_atributo_idx] == valor]
        nodo.hijos[valor] = construir_arbol_decision(data_dividida, atributos_restantes, etiquetas)

    return nodo

def predecir_ejemplo(ejemplo, arbol_decision):
    # Predice la etiqueta de un ejemplo basado en el árbol de decisión
    if arbol_decision.valor in ejemplo:
        valor_atributo = ejemplo[arbol_decision.valor]
        if valor_atributo in arbol_decision.hijos:
            return predecir_ejemplo(ejemplo, arbol_decision.hijos[valor_atributo])
    return arbol_decision.valor

# Nuevos valores para atributos, etiquetas y datos de entrenamiento
atributos = ["sabor", "color", "tamaño"]
etiquetas = ["fruta", "no fruta"]
data_entrenamiento = [
    ["dulce", "rojo", "pequeño", "fruta"],     # Fresa
    ["dulce", "amarillo", "pequeño", "fruta"], # Plátano
    ["ácido", "verde", "pequeño", "fruta"],    # Limón
    ["dulce", "verde", "grande", "no fruta"],  # Sandía
    ["ácido", "amarillo", "pequeño", "fruta"], # Limón
    ["dulce", "rojo", "grande", "fruta"]       # Manzana
]

# Construye el árbol de decisión con los nuevos datos
arbol_decision = construir_arbol_decision(data_entrenamiento, atributos, etiquetas)

# Nuevos ejemplos para predecir
ejemplo1 = {"sabor": "dulce", "color": "amarillo", "tamaño": "pequeño"}  # Plátano
ejemplo2 = {"sabor": "ácido", "color": "verde", "tamaño": "pequeño"}      # Limón

# Predice y muestra los resultados de los nuevos ejemplos
print("Ejemplo 1 - Es fruta?" + ": " + predecir_ejemplo(ejemplo1, arbol_decision))
print("Ejemplo 2 - Es fruta?" + ": " + predecir_ejemplo(ejemplo2, arbol_decision))
