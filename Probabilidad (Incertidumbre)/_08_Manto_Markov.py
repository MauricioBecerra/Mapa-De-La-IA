import numpy as np  # Importa la librería numpy

matriz_transicion = np.array([[0.7, 0.2, 0.1],  # Definimos la matriz de transición de estados
                               [0.3, 0.5, 0.2], 
                               [0.4, 0.4, 0.2]]) 

estados = ['Bandera Roja', 'Bandera Amarilla', 'Bandera Azul']  # Definimos los estados posibles

def predecir_clima_actual(estado_actual):
    estado_futuro = np.random.choice(estados, p=matriz_transicion[estado_actual])  # Predice el estado futuro
    return estado_futuro

def main():
    estado_actual = np.random.randint(0, 3)  # Selecciona un estado inicial aleatorio
    print("Bandera actual:", estados[estado_actual])  # Imprime el estado actual
    
    for i in range(1, 6):  # Predice y muestra la bandera a futuro para los próximos 5 vueltas
        print(f"Vuelta {i}: {predecir_clima_actual(estado_actual)}")
        estado_actual = estados.index(predecir_clima_actual(estado_actual))  # Actualiza el estado actual

if __name__ == "__main__":
    main()