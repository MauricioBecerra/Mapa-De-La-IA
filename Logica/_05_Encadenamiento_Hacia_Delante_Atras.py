def encadenamiento_hacia_adelante(base_hechos, reglas):
    while True:
        algo_cambiado = False  # Bandera para indicar si algo ha cambiado en esta iteración
        for regla in reglas:  # Itera sobre todas las reglas
            antecedentes_verdaderos = all(premisa in base_hechos for premisa in regla[0])  # Verifica si todas las premisas de la regla están en la base de hechos
            consecuente = regla[1]  # Obtiene el consecuente de la regla
            if antecedentes_verdaderos and consecuente not in base_hechos:  # Si todos los antecedentes son verdaderos y el consecuente no está en la base de hechos
                base_hechos.append(consecuente)  # Agrega el consecuente a la base de hechos
                algo_cambiado = True  # Marca que algo ha cambiado
        if not algo_cambiado:  # Si no ha habido cambios en esta iteración, termina el bucle
            break
    return base_hechos

def encadenamiento_hacia_atras(meta, reglas, base_hechos):
    if meta in base_hechos:  # Si la meta ya está en la base de hechos, devuelve True
        return True
    for regla in reglas:  # Itera sobre todas las reglas
        consecuente = regla[1]  # Obtiene el consecuente de la regla
        if meta == consecuente:  # Si la meta es igual al consecuente de la regla
            antecedentes = regla[0]  # Obtiene los antecedentes de la regla
            if all(encadenamiento_hacia_atras(premisa, reglas, base_hechos) for premisa in antecedentes):  # Si todos los antecedentes pueden ser demostrados
                return True  # Retorna True
    return False  # Si no se puede demostrar la meta

# Cambio de los valores para base_hechos y reglas
base_hechos = ['A', 'B']  # Nueva base de hechos
reglas = [(['A'], 'C'),  # Nuevas reglas
          (['C'], 'D'),
          (['B'], 'E'),
          (['D', 'E'], 'F')]

print("Encadenamiento hacia adelante:")
resultado_adelante = encadenamiento_hacia_adelante(base_hechos, reglas)  # Realiza el encadenamiento hacia adelante
print("Base de hechos final:", resultado_adelante)

print("\nEncadenamiento hacia atrás:")
meta = 'F'  # Nueva meta
resultado_atras = encadenamiento_hacia_atras(meta, reglas, base_hechos)  # Realiza el encadenamiento hacia atrás
print("¿Se puede demostrar la meta?", resultado_atras)
