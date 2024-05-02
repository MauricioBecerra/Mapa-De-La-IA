import numpy as np  # Importa la librería NumPy con el alias np
import matplotlib.pyplot as plt  # Importa el módulo pyplot de Matplotlib con el alias plt

def distribucion_probabilidad_lanzamiento_monedas():
    probabilidades = np.zeros(3)  # Crea un array de tamaño 3 lleno de ceros para almacenar las probabilidades
    for i in range(2):  # Itera sobre los resultados del primer lanzamiento de la moneda (0 y 1)
        for j in range(2):  # Itera sobre los resultados del segundo lanzamiento de la moneda (0 y 1)
            suma = i + j  # Calcula la suma de los resultados de los lanzamientos
            probabilidades[suma] += 1  # Incrementa la frecuencia de la suma en el array de probabilidades
    probabilidades /= 4  # Normaliza las frecuencias dividiendo por el número total de casos posibles
    return probabilidades  # Devuelve el array de probabilidades

def main():
    valores = np.arange(0, 3)  # Crea un array con los valores posibles de la suma de los lanzamientos (0, 1, 2)
    probabilidades = distribucion_probabilidad_lanzamiento_monedas()  # Calcula la distribución de probabilidad

    # Crea un gráfico de barras con los valores y probabilidades
    plt.bar(valores, probabilidades)
    plt.title('Distribución de Probabilidad del Lanzamiento de Dos Monedas')  # Título del gráfico
    plt.xlabel('Suma de los Resultados')  # Etiqueta del eje x
    plt.ylabel('Probabilidad')  # Etiqueta del eje y
    plt.xticks(valores)  # Establece los ticks del eje x en los valores posibles de la suma
    plt.show()  # Muestra el gráfico

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta directamente
