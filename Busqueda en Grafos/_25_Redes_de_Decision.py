class Evento:  # Define una clase llamada Evento
    def __init__(self, probabilidad, resultado_bueno, resultado_malo):  # Define el método de inicialización
        self.probabilidad = probabilidad  # Asigna la probabilidad del evento
        self.resultado_bueno = resultado_bueno  # Asigna el resultado bueno del evento
        self.resultado_malo = resultado_malo  # Asigna el resultado malo del evento

class Decision:  # Define una clase llamada Decision
    def __init__(self, nombre):  # Define el método de inicialización
        self.nombre = nombre  # Asigna el nombre de la decisión

class Opcion:  # Define una clase llamada Opcion
    def __init__(self, nombre, resultados):  # Define el método de inicialización
        self.nombre = nombre  # Asigna el nombre de la opción
        self.resultados = resultados  # Asigna los resultados de la opción

def calcular_utilidad(opcion, evento_bueno, evento_malo):  # Define una función para calcular la utilidad esperada
    utilidad = opcion.resultados[0] * evento_bueno.probabilidad + opcion.resultados[1] * evento_malo.probabilidad  # Calcula la utilidad
    return utilidad  # Devuelve la utilidad esperada

def tomar_decision(opcion_a, opcion_b, evento_bueno, evento_malo):  # Define una función para tomar una decisión entre dos opciones
    utilidad_opcion_a = calcular_utilidad(opcion_a, evento_bueno, evento_malo)  # Calcula la utilidad esperada de la opción A
    utilidad_opcion_b = calcular_utilidad(opcion_b, evento_bueno, evento_malo)  # Calcula la utilidad esperada de la opción B

    if utilidad_opcion_a > utilidad_opcion_b:  # Compara la utilidad esperada de las opciones
        return opcion_a.nombre  # Devuelve el nombre de la opción A si tiene mayor utilidad
    elif utilidad_opcion_b > utilidad_opcion_a:
        return opcion_b.nombre  # Devuelve el nombre de la opción B si tiene mayor utilidad
    else:
        return "Ambas opciones tienen la misma utilidad esperada."  # Devuelve un mensaje si las utilidades son iguales

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    evento_bueno = Evento(probabilidad=0.8, resultado_bueno=100, resultado_malo=0)  # Crea un evento bueno
    evento_malo = Evento(probabilidad=0.2, resultado_bueno=20, resultado_malo=0)  # Crea un evento malo

    opcion_a = Opcion(nombre="Opción Maynez", resultados=(100, 0))  # Define la opción A
    opcion_b = Opcion(nombre="Opción Xochitl", resultados=(50, 50))  # Define la opción B

    decision = tomar_decision(opcion_a, opcion_b, evento_bueno, evento_malo)  # Llama a la función para tomar una decisión
    print("La mejor opción es:", decision)  # Imprime la mejor opción encontrada
