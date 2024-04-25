import random  # Importa el módulo random

def funcion_objetivo(numero_buscar, numero_aleatorio):  # Define una función objetivo para determinar si el número aleatorio es igual al número buscado
    if numero_aleatorio == numero_buscar:
        return True  # Devuelve True si el número aleatorio coincide con el número buscado
    else:
        return False  # Devuelve False si el número aleatorio no coincide con el número buscado

def busqueda_online(numero_buscar, max_intent):  # Define una función para realizar una búsqueda en línea
    intentos = 0  # Inicializa el contador de intentos
    encontrado = False  # Inicializa la bandera de encontrado
    
    while intentos < max_intent and not encontrado:  # Realiza un bucle mientras no se alcance el máximo de intentos y el número no se haya encontrado
        numero_aleatorio = random.randint(1, 30)  # Genera un número aleatorio entre 1 y 30
        encontrado = funcion_objetivo(numero_buscar, numero_aleatorio)  # Verifica si el número aleatorio coincide con el número buscado
        intentos += 1  # Incrementa el contador de intentos
    
    return encontrado, intentos  # Devuelve si se encontró el número y el número de intentos realizados

numero_a_buscar = int(input("Ingrese el numero a buscar: "))  # Solicita al usuario que ingrese el número a buscar
max_intent = int(input("Ingrese el numero a maximo de intentos: "))  # Solicita al usuario que ingrese el número máximo de intentos

resultado, intentos_realizados = busqueda_online(numero_a_buscar, max_intent)  # Realiza la búsqueda en línea

if resultado:  # Si se encontró el número
    print(f"¡El número {numero_a_buscar} fue encontrado en {intentos_realizados} intentos!")  # Imprime un mensaje indicando que el número fue encontrado y el número de intentos realizados
else:  # Si no se encontró el número
    print(f"El número {numero_a_buscar} no fue encontrado después de {intentos_realizados} intentos.")  # Imprime un mensaje indicando que el número no fue encontrado y el número de intentos realizados
