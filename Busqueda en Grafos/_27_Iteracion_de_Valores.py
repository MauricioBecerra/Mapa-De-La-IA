import numpy as np  # Importación de la biblioteca NumPy

# Matriz de utilidades modificada
utilidades = np.array([[10, 5],    # Acción 1: Alta
                       [7, 8],     # Acción 2: Media
                       [3, 4]])    # Acción 3: Baja

# Matriz de probabilidades de transición modificada
probabilidades_transicion = np.array([[0.9, 0.1, 0],    # Estado 1: Soleado
                                      [0.3, 0.6, 0.1],  # Estado 2: Nublado
                                      [0, 0.4, 0.6]])   # Estado 3: Lluvioso

descuento = 0.9  # Parámetro de descuento

valores = np.zeros(utilidades.shape[0])  # Inicialización de los valores de los estados

def iteracion_valores():  # Definición de la función de iteración de valores
    global valores  # Se utiliza la palabra clave global para modificar la variable valores definida fuera de la función
    valores_previos = np.copy(valores)  # Copia de los valores actuales para su uso en la actualización
    for estado in range(utilidades.shape[0]):  # Iteración sobre todos los estados
        valores[estado] = max([sum([probabilidades_transicion[estado, nuevo_estado] * (utilidades[estado, accion] + descuento * valores_previos[nuevo_estado])
                                    for nuevo_estado in range(utilidades.shape[0])])
                               for accion in range(utilidades.shape[1])])

iteracion = 0  # Inicialización del contador de iteración
epsilon = 1e-6  # Criterio de convergencia
max_iteraciones = 1000  # Número máximo de iteraciones permitidas
while True:  # Bucle infinito
    iteracion_valores()  # Llamada a la función de iteración de valores
    iteracion += 1  # Incremento del contador de iteración
    # Verificación de convergencia o máximo de iteraciones alcanzado
    if np.max(np.abs(valores - np.zeros(utilidades.shape[0]))) < epsilon or iteracion >= max_iteraciones:
        break  # Salir del bucle

print("Valores óptimos de los estados:")  # Impresión de los valores óptimos de los estados
for i, valor in enumerate(valores):  # Iteración sobre los valores óptimos de los estados
    print(f"Estado {i+1}: {valor}")  # Impresión de cada valor óptimo

# Determinación de las acciones óptimas en cada estado
acciones_optimas = np.argmax([[sum([probabilidades_transicion[estado, nuevo_estado] * (utilidades[estado, accion] + descuento * valores[nuevo_estado])
                                    for nuevo_estado in range(utilidades.shape[0])])
                               for accion in range(utilidades.shape[1])]
                             for estado in range(utilidades.shape[0])], axis=1)

print("\nAcciones óptimas en cada estado:")  # Impresión de las acciones óptimas en cada estado
for i, accion in enumerate(acciones_optimas):  # Iteración sobre las acciones óptimas
    print(f"Estado {i+1}: Acción {accion+1}")  # Impresión de cada acción óptima
