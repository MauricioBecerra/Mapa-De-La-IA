import random

def es_estado_objetivo(estado, estado_objetivo):
    # Comprueba si todos los elementos del estado objetivo están presentes en el estado actual
    return all(objetivo in estado for objetivo in estado_objetivo)

def aplicar_accion(estado, accion):
    # Crea un nuevo estado aplicando los efectos de la acción al estado actual
    nuevo_estado = estado.copy()
    nuevo_estado.extend(accion['efecto'])  # Agrega los efectos de la acción al nuevo estado
    return nuevo_estado

def satplan(estado_inicial, estado_objetivo, acciones):
    max_iteraciones = 1000  # Máximo número de iteraciones
    for _ in range(max_iteraciones):
        estado_actual = estado_inicial.copy()  # Estado actual es el estado inicial
        plan = []  # Lista para almacenar el plan encontrado

        for _ in range(len(acciones)):
            satisfecho = False

            random.shuffle(acciones)  # Reorganiza aleatoriamente las acciones para explorar diferentes caminos

            for accion in acciones:
                nuevo_estado = aplicar_accion(estado_actual, accion)  # Aplica la acción al estado actual
                if es_estado_objetivo(nuevo_estado, estado_objetivo):  # Comprueba si el nuevo estado es el objetivo
                    plan.append(accion)  # Añade la acción al plan
                    satisfecho = True  # Indica que se encontró una acción que satisface el objetivo
                    break

                estado_actual = nuevo_estado  # Actualiza el estado actual con el nuevo estado

            if satisfecho:  # Si se encontró una acción que satisface el objetivo, sale del bucle
                break

        if satisfecho:  # Si se encontró un plan, imprime las acciones en el plan y termina la función
            print("Plan encontrado:")
            for accion in plan:
                print(f"Ejecutar acción {accion['nombre']}")
            return
        else:
            print("No se encontró un plan")  # Si no se encontró un plan, indica que no se encontró y termina la función
            return

if __name__ == "__main__":
    estado_inicial = ['A']  # Estado inicial
    estado_objetivo = ['C', 'D']  # Estado objetivo
    acciones = [
        {'nombre': 'Accion1', 'efecto': ['B', 'D']},  # Acción 1 con efectos B y D
        {'nombre': 'Accion2', 'efecto': ['C']}  # Acción 2 con efecto C
    ]

    satplan(estado_inicial, estado_objetivo, acciones)  # Llama a la función satplan con los estados y acciones dados
