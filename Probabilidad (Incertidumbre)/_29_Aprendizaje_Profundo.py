import tensorflow as tf  # Importa TensorFlow
from tensorflow.keras import Sequential  # Importa la clase Sequential de Keras
from tensorflow.keras.layers import Dense  # Importa la capa Dense de Keras

# Definición del modelo de red neuronal
modelo = Sequential([  # Crea un modelo secuencial
    Dense(128, activation='relu', input_shape=(20,)),  # Capa de entrada con 128 neuronas y activación ReLU
    Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y activación ReLU
    Dense(1, activation='sigmoid')  # Capa de salida con 1 neurona y activación sigmoide
])

# Compilación del modelo
modelo.compile(optimizer='adam',  # Optimizador Adam
               loss='binary_crossentropy',  # Función de pérdida binary_crossentropy
               metrics=['accuracy'])  # Métrica de precisión

# Generación de datos de ejemplo
X_train = tf.random.normal(shape=(1500, 20))  # Genera datos de entrada aleatorios
y_train = tf.random.uniform(shape=(1500, 1), minval=0, maxval=3, dtype=tf.int32)  # Genera etiquetas aleatorias

# Entrenamiento del modelo
modelo.fit(X_train, y_train, epochs=15, batch_size=64)  # Entrena el modelo durante 15 épocas con lotes de tamaño 64

# Evaluación del modelo
loss, accuracy = modelo.evaluate(X_train, y_train)  # Evalúa el modelo con los datos de entrenamiento
print("Precisión del modelo:", accuracy)  # Imprime la precisión del modelo
