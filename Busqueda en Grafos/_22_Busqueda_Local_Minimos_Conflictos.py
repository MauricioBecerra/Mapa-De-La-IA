import random  # Importamos la biblioteca random para generar números aleatorios

class SolucionadorMinConflictos:
    def __init__(self, grafo, max_iteraciones=1000):
        self.grafo = grafo  # Guardamos el grafo proporcionado
        self.colores = {}  # Creamos un diccionario para almacenar la asignación de colores de los nodos
        self.max_iteraciones = max_iteraciones  # Establecemos el número máximo de iteraciones

    def resolver(self):
        self.asignacion_inicial()  # Llamamos al método para realizar una asignación inicial aleatoria
        for _ in range(self.max_iteraciones):  # Realizamos un bucle sobre el número máximo de iteraciones
            if self.verificar_solucion():  # Verificamos si la solución actual es válida
                return True  # Devolvemos verdadero si encontramos una solución
            nodo = self.seleccionar_nodo_conflicto()  # Seleccionamos un nodo en conflicto
            self.resolver_conflicto(nodo)  # Resolvemos el conflicto para el nodo seleccionado
        return False  # Si no encontramos una solución después del número máximo de iteraciones, devolvemos falso

    def asignacion_inicial(self):
        for nodo in self.grafo:  # Iteramos sobre cada nodo en el grafo
            self.colores[nodo] = random.choice(range(len(self.grafo)))  # Asignamos un color aleatorio a cada nodo

    def verificar_solucion(self):
        for nodo in self.grafo:  # Iteramos sobre cada nodo en el grafo
            for vecino in self.grafo[nodo]:  # Iteramos sobre cada vecino del nodo actual
                if self.colores[nodo] == self.colores[vecino]:  # Si el nodo y su vecino tienen el mismo color
                    return False  # Devolvemos falso, indicando que hay un conflicto en la solución actual
        return True  # Si no encontramos conflictos, devolvemos verdadero

    def seleccionar_nodo_conflicto(self):
        conflictos = []  # Creamos una lista para almacenar los nodos en conflicto
        for nodo in self.grafo:  # Iteramos sobre cada nodo en el grafo
            for vecino in self.grafo[nodo]:  # Iteramos sobre cada vecino del nodo actual
                if self.colores[nodo] == self.colores[vecino]:  # Si el nodo y su vecino tienen el mismo color
                    conflictos.append(nodo)  # Agregamos el nodo en conflicto a la lista
                    break  # Salimos del bucle interno para evitar duplicados
        return random.choice(conflictos)  # Seleccionamos aleatoriamente un nodo en conflicto

    def resolver_conflicto(self, nodo):
        color_conflicto_minimo = self.encontrar_color_conflicto_minimo(nodo)  # Encontramos el color que minimiza los conflictos para el nodo
        self.colores[nodo] = color_conflicto_minimo  # Asignamos el color encontrado al nodo en conflicto

    def encontrar_color_conflicto_minimo(self, nodo):
        conflictos_minimos = float('inf')  # Inicializamos el número mínimo de conflictos con infinito
        color_conflicto_minimo = None  # Inicializamos el color que minimiza los conflictos como nulo
        for color in range(len(self.grafo)):  # Iteramos sobre cada color posible
            conteo_conflictos = sum(1 for vecino in self.grafo[nodo] if self.colores[vecino] == color)  # Contamos el número de conflictos para el nodo con el color actual
            if conteo_conflictos < conflictos_minimos:  # Si encontramos un color que minimiza los conflictos
                conflictos_minimos = conteo_conflictos  # Actualizamos el número mínimo de conflictos
                color_conflicto_minimo = color  # Actualizamos el color que minimiza los conflictos
        return color_conflicto_minimo  # Devolvemos el color que minimiza los conflictos

# Ejemplo de uso
if __name__ == "__main__":
    grafo = {  # Se establece el grafo
        'Jalisco': {'Nayarit': 14, 'Zacatecas': 7},
        'Nayarit': {'Jalisco': 11, 'Durango': 10, 'Sinaloa': 1},
        'Zacatecas': {'Jalisco': 5, 'Durango': 2, 'Nuevo Leon': 14, 'Coahuila': 3},
        'Durango': {'Zacatecas': 8, 'Nayarit': 4, 'Coahuila': 15, 'Chihuahua': 6, 'Sinaloa': 12},
        'Coahuila': {'Zacatecas': 9, 'Durango': 13, 'Nuevo Leon': 1, 'Chihuahua': 7},
        'Nuevo Leon': {'Zacatecas': 10, 'Coahuila': 11},
        'Chihuahua': {'Durango': 14, 'Sinaloa': 8, 'Coahuila': 5, 'Sonora': 3},
        'Sinaloa': {'Nayarit': 13, 'Durango': 7, 'Sonora': 9, 'Chihuahua': 15},
        'Sonora': {'Sinaloa': 9, 'Chihuahua': 15, 'Baja California': 10},
        'Baja California': {'Sonora': 2}
    }
    solucionador = SolucionadorMinConflictos(grafo)
    if solucionador.resolver():
        print("Se ha encontrado una solución: ")
        print(solucionador.colores)  # Imprimimos la asignación de colores
    else:
        print("No se encontró solución en el número máximo de iteraciones. :c")
