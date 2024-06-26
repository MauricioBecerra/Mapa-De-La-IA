class Evento:  # Define una clase llamada Evento para representar un evento en el contexto de la toma de decisiones
    def __init__(self, probabilidad, resultado_bueno, resultado_malo):  # Define el método de inicialización con la probabilidad del evento y sus resultados buenos y malos
        self.probabilidad = probabilidad  # Asigna la probabilidad del evento al atributo probabilidad de la instancia
        self.resultado_bueno = resultado_bueno  # Asigna el resultado bueno al atributo resultado_bueno de la instancia
        self.resultado_malo = resultado_malo  # Asigna el resultado malo al atributo resultado_malo de la instancia

class Decision:  # Define una clase llamada Decision para representar una decisión en el contexto de la toma de decisiones
    def __init__(self, name):  # Define el método de inicialización con el nombre de la decisión
        self.name = name  # Asigna el nombre de la decisión al atributo name de la instancia

class Opcion:  # Define una clase llamada Opcion para representar una opción en el contexto de la toma de decisiones
    def __init__(self, name, result):  # Define el método de inicialización con el nombre de la opción y sus resultados
        self.name = name  # Asigna el nombre de la opción al atributo name de la instancia
        self.result = result  # Asigna los resultados de la opción al atributo result de la instancia

def calcular_utilidad(opcion, evento_bueno, evento_malo):  # Define una función para calcular la utilidad esperada de una opción dada un evento bueno y uno malo
    utilidad = opcion.result[0] * evento_bueno.probabilidad + opcion.result[1] * evento_malo.probabilidad  # Calcula la utilidad esperada de la opción
    return utilidad  # Devuelve la utilidad esperada de la opción

def calcular_valor_informacion(opcion_a, opcion_b, evento_bueno, evento_malo, evento_informacion):  # Define una función para calcular el valor de obtener información adicional antes de tomar una decisión
    utilidad_sin_info = max(calcular_utilidad(opcion_a, evento_bueno, evento_malo), calcular_utilidad(opcion_b, evento_bueno, evento_malo))  # Calcula la utilidad esperada sin obtener información adicional

    utilidad_con_info = calcular_utilidad(opcion_a, evento_bueno, evento_malo) * evento_informacion.probabilidad \
                        + calcular_utilidad(opcion_b, evento_bueno, evento_malo) * evento_informacion.probabilidad  # Calcula la utilidad esperada con información adicional

    return utilidad_con_info - utilidad_sin_info  # Calcula y devuelve el valor de la información como la diferencia entre la utilidad con y sin información adicional

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    evento_bueno = Evento(probabilidad=0.8, resultado_bueno=100, resultado_malo=0)  # Define un evento bueno con su probabilidad y resultados buenos y malos
    evento_malo = Evento(probabilidad=0.2, resultado_bueno=20, resultado_malo=0)  # Define un evento malo con su probabilidad y resultados buenos y malos
    evento_informacion = Evento(probabilidad=0.5, resultado_bueno=0, resultado_malo=0)  # Define un evento de información adicional con su probabilidad y resultados buenos y malos

    opcion_a = Opcion(name="Opción Maynez", result=(100, 0))  # Define la opción A con su nombre y resultados
    opcion_b = Opcion(name="Opción Xochitl", result=(50, 50))  # Define la opción B con su nombre y resultados

    valor_informacion = calcular_valor_informacion(opcion_a, opcion_b, evento_bueno, evento_malo, evento_informacion)  # Calcula el valor de obtener información adicional antes de tomar una decisión

    print("El valor de obtener información adicional es:", valor_informacion)  # Imprime el valor de la información calculado
