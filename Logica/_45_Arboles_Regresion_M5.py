import numpy as np  # Importa numpy para operaciones numéricas

class Nodo:
    def __init__(self, atributo=None, umbral=None, valor=None, hijos=None):
        # Inicializa un nodo del árbol con atributo, umbral, valor y lista de hijos
        self.atributo = atributo
        self.umbral = umbral
        self.valor = valor
        self.hijos = hijos

def calcular_error_cuadratico_medio(y_true, y_pred):
    # Calcula el error cuadrático medio entre las predicciones y los valores reales
    return np.mean((y_true - y_pred) ** 2)

def dividir_datos(X, y, atributo, umbral):
    # Divide los datos según un atributo y un umbral dados
    izquierda = np.where(X[:, atributo] <= umbral)
    derecha = np.where(X[:, atributo] > umbral)
    return izquierda, derecha

def ajustar_modelo_regresion(X, y):
    # Ajusta un modelo de regresión lineal a los datos de entrada
    return np.linalg.lstsq(X, y, rcond=None)[0]

def construir_arbol_regresion(X, y, max_profundidad, min_muestras_split):
    # Construye un árbol de regresión recursivamente
    if max_profundidad == 0 or len(X) < min_muestras_split:
        return Nodo(valor=np.mean(y))

    mejor_atributo = None
    mejor_umbral = None
    mejor_error = np.inf
    mejor_izquierda = None
    mejor_derecha = None

    # Itera sobre todos los atributos y umbrales para encontrar la mejor división
    for atributo in range(X.shape[1]):
        for umbral in np.unique(X[:, atributo]):
            izquierda, derecha = dividir_datos(X, y, atributo, umbral)

            # Si hay pocas muestras en alguna división, continúa con la siguiente iteración
            if len(izquierda[0]) < min_muestras_split or len(derecha[0]) < min_muestras_split:
                continue

            y_izquierda = y[izquierda]
            y_derecha = y[derecha]

            modelo_izquierda = ajustar_modelo_regresion(X[izquierda], y_izquierda)
            modelo_derecha = ajustar_modelo_regresion(X[derecha], y_derecha)

            y_pred_izquierda = np.dot(X[izquierda], modelo_izquierda)
            y_pred_derecha = np.dot(X[derecha], modelo_derecha)

            # Calcula el error combinado de ambas divisiones
            error = calcular_error_cuadratico_medio(y[izquierda], y_pred_izquierda) + calcular_error_cuadratico_medio(y[derecha], y_pred_derecha)
            if error < mejor_error:
                mejor_atributo = atributo
                mejor_umbral = umbral
                mejor_error = error
                mejor_izquierda = izquierda
                mejor_derecha = derecha

    # Si no hay mejor división, devuelve el nodo con el valor medio de los datos
    if mejor_error == np.inf:
        return Nodo(valor=np.mean(y))

    # Construye recursivamente los nodos hijos
    nodo_izquierda = construir_arbol_regresion(X[mejor_izquierda], y[mejor_izquierda], max_profundidad - 1, min_muestras_split)
    nodo_derecha = construir_arbol_regresion(X[mejor_derecha], y[mejor_derecha], max_profundidad - 1, min_muestras_split)

    return Nodo(atributo=mejor_atributo, umbral=mejor_umbral, hijos=[nodo_izquierda, nodo_derecha])

def predecir_valor_regresion(ejemplo, arbol):
    # Predice el valor de un ejemplo utilizando el árbol de regresión
    if arbol.valor is not None:
        return arbol.valor

    if ejemplo[arbol.atributo] <= arbol.umbral:
        return predecir_valor_regresion(ejemplo, arbol.hijos[0])
    else:
        return predecir_valor_regresion(ejemplo, arbol.hijos[1])

# Nuevos datos de entrada y salida para el modelo de regresión
X = np.array([[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
y = np.array([6, 7, 8, 9, 10])  # Modificamos los valores de salida

# Construye el árbol de regresión con los nuevos datos
arbol_regresion = construir_arbol_regresion(X, y, max_profundidad=2, min_muestras_split=2)

# Nuevo ejemplo para predecir
ejemplo = [4, 6]  # Cambiamos el ejemplo

# Predice y muestra el valor predicho para el nuevo ejemplo
valor_predicho = predecir_valor_regresion(ejemplo, arbol_regresion)
print("Valor predicho para el ejemplo {}: {}".format(ejemplo, valor_predicho))
