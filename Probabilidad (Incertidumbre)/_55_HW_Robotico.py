import time
import random

# Clase del sensor de proximidad ficticio
class SensorProximidad:
    def __init__(self):  # Método constructor de la clase
        pass  # No realiza ninguna acción

    def leer_proximidad(self):  # Método para simular la lectura de proximidad
        # Simular lectura de proximidad
        return random.randint(0, 200)  # Devuelve un valor aleatorio entre 0 y 200 (mm)

# Clase del actuador de motor ficticio
class Motor:
    def __init__(self):  # Método constructor de la clase
        pass  # No realiza ninguna acción

    def mover(self, direccion):  # Método para simular el movimiento del motor
        # Simular movimiento del motor
        print(f'Moviendo motor en dirección {direccion}')  # Imprime la dirección del movimiento

# Función principal que simula el comportamiento del robot
def simular_robot(sensor, motor, movimientos=10):  # Define la función con los parámetros sensor, motor y movimientos (valor predeterminado: 10)
    movimientos_realizados = 0  # Inicializa el contador de movimientos realizados
    while movimientos_realizados < movimientos:  # Bucle while que se ejecuta mientras se hayan realizado menos movimientos que el total
        # Leer la proximidad del sensor
        proximidad = sensor.leer_proximidad()  # Llama al método leer_proximidad del sensor
        print(f'Proximidad leída: {proximidad} mm')  # Imprime la proximidad leída

        # Tomar decisiones basadas en la proximidad
        if proximidad > 100:  # Si la proximidad es mayor que 100 mm
            motor.mover('adelante')  # Llama al método mover del motor con la dirección 'adelante'
        else:  # Si la proximidad es menor o igual a 100 mm
            motor.mover('atras')  # Llama al método mover del motor con la dirección 'atras'

        movimientos_realizados += 1  # Incrementa el contador de movimientos realizados

        time.sleep(1)  # Pausa el programa durante 1 segundo entre cada iteración

# Crear instancia del sensor y del motor
sensor_proximidad = SensorProximidad()  # Crea una instancia de la clase SensorProximidad
motor = Motor()  # Crea una instancia de la clase Motor

# Simular comportamiento del robot con 10 movimientos
simular_robot(sensor_proximidad, motor, movimientos=10)  # Llama a la función simular_robot con los objetos sensor_proximidad y motor, y 10 movimientos como parámetro
