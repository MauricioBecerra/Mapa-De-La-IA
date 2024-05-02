import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas eficientes

def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Define la función de activación sigmoide

def sigmoid_derivative(x):
    return x * (1 - x)  # Calcula la derivada de la función sigmoide

# Datos de entrada y salida
X = np.array([[1, 0], [1, 1], [0, 0], [0, 1]])  # Matriz de entrada: características
y = np.array([[1], [1], [0], [0]])  # Matriz de salida: etiquetas

np.random.seed(42)  # Fija la semilla aleatoria para reproducibilidad
input_size = 2  # Número de características de entrada
hidden_size = 3  # Número de neuronas en la capa oculta
output_size = 1  # Número de neuronas en la capa de salida
learning_rate = 0.01  # Tasa de aprendizaje para ajustar los pesos

# Pesos y sesgos iniciales
weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))  # Pesos para la capa oculta
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))  # Pesos para la capa de salida

bias_hidden = np.random.uniform(size=(1, hidden_size))  # Sesgos para la capa oculta
bias_output = np.random.uniform(size=(1, output_size))  # Sesgos para la capa de salida

epochs = 15000  # Número de épocas de entrenamiento
for epoch in range(epochs):  # Para cada época de entrenamiento
    # Forward propagation (propagación hacia adelante)
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden  # Entrada ponderada a la capa oculta
    hidden_output = sigmoid(hidden_input)  # Salida de la capa oculta
    output = np.dot(hidden_output, weights_hidden_output) + bias_output  # Entrada ponderada a la capa de salida
    predicted_output = sigmoid(output)  # Salida de la capa de salida
    
    # Cálculo del error
    error = y - predicted_output  # Error entre la salida deseada y la salida predicha
    
    # Backpropagation (retropropagación)
    output_delta = error * sigmoid_derivative(predicted_output)  # Delta de error en la capa de salida
    hidden_error = output_delta.dot(weights_hidden_output.T)  # Error en la capa oculta
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)  # Delta de error en la capa oculta
    
    # Actualización de pesos y sesgos
    weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate  # Actualización de pesos de la capa de salida
    weights_input_hidden += X.T.dot(hidden_delta) * learning_rate  # Actualización de pesos de la capa oculta
    bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate  # Actualización del sesgo de la capa de salida
    bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate  # Actualización del sesgo de la capa oculta

# Imprimir los resultados finales
print("Pesos de la capa oculta:")
print(weights_input_hidden)  # Imprimir los pesos de la capa oculta
print("\nPesos de la capa de salida:")
print(weights_hidden_output)  # Imprimir los pesos de la capa de salida
print("\nSesgo de la capa oculta:")
print(bias_hidden)  # Imprimir el sesgo de la capa oculta
print("\nSesgo de la capa de salida:")
print(bias_output)  # Imprimir el sesgo de la capa de salida

# Predicción final
print("\nPredicciones finales:")
print(predicted_output)  # Imprimir las predicciones finales
