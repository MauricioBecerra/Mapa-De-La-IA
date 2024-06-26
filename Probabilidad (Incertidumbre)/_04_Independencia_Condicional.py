import numpy as np

def lanzar_moneda():
    # Simula el lanzamiento de una moneda. Devuelve 'Aguila' o 'Sello'.
    resultado = np.random.choice(['Aguila', 'Sello'])  # Selecciona aleatoriamente entre 'Aguila' y 'Sello'
    return resultado

def experimento():
    # Simula el experimento de lanzar dos monedas y verifica si los resultados son independientes.
    moneda1 = lanzar_moneda()  # Lanza la primera moneda
    moneda2 = lanzar_moneda()  # Lanza la segunda moneda
    return moneda1, moneda2  # Devuelve los resultados de los lanzamientos de las dos monedas

def calcular_independencia_condicional(n_experimentos):
    # Realiza n_experimentos y cuenta los casos donde los resultados son independientes.
    independientes = 0  # Inicializa el contador para contar los casos donde ambas monedas muestran 'Aguila'
    for _ in range(n_experimentos):  # Realiza un número de experimentos dado
        resultado1, resultado2 = experimento()  # Realiza un experimento de lanzar dos monedas
        if resultado1 == 'Aguila' and resultado2 == 'Aguila':  # Verifica si ambas monedas muestran 'Aguila'
            independientes += 1  # Incrementa el contador si ambas monedas muestran 'Aguila'

    probabilidad_independencia = independientes / n_experimentos  # Calcula la probabilidad de independencia condicional
    return probabilidad_independencia

def main():
    n_experimentos = 10000  # Número de experimentos a realizar
    probabilidad_independencia = calcular_independencia_condicional(n_experimentos)  # Calcula la probabilidad de independencia condicional

    print("Probabilidad de obtener Aguila en ambas monedas (Independencia Condicional):", probabilidad_independencia)  # Imprime la probabilidad de independencia condicional

if __name__ == "__main__":
    main()
