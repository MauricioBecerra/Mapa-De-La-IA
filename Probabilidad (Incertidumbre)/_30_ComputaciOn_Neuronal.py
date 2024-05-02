import numpy as np  # Importa la biblioteca numpy para operaciones numéricas eficientes

def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # La función de activación sigmoide retorna el valor de la función 1 / (1 + e^(-x))

class Neurona:
    def __init__(self, pesos, sesgo):  # Método de inicialización de la clase Neurona
        self.pesos = pesos  # Inicializa los pesos de la neurona
        self.sesgo = sesgo  # Inicializa el sesgo de la neurona
    
    def feedforward(self, entrada):  # Método para calcular la salida de la neurona
        total = np.dot(self.pesos, entrada) + self.sesgo  # Calcula el total ponderado de las entradas más el sesgo
        return sigmoid(total)  # Aplica la función de activación sigmoide al total y retorna la salida de la neurona

pesos = np.array([0.2, -0.8])  # Define nuevos pesos para las conexiones sinápticas
sesgo = 0.5  # Define un nuevo sesgo para la neurona

entrada = np.array([0.6, 0.4])  # Define una nueva entrada para la neurona

neurona = Neurona(pesos, sesgo)  # Crea una instancia de la clase Neurona con los nuevos pesos y sesgo dados

salida = neurona.feedforward(entrada)  # Calcula la salida de la neurona dada la nueva entrada

print("Salida de la neurona:", salida)  # Imprime la salida de la neurona
