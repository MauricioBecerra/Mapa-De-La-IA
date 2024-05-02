prob_urna1 = 0.3  # Probabilidad de elegir la urna 1
prob_urna2 = 0.7  # Probabilidad de elegir la urna 2

prob_color_dado_urna1 = {'amarillo': 0.4, 'blanco': 0.3, 'negro': 0.3}  # Probabilidad de cada color en la urna 1
prob_color_dado_urna2 = {'amarillo': 0.2, 'blanco': 0.5, 'negro': 0.3}  # Probabilidad de cada color en la urna 2

def calcular_probabilidad_bayes(color, urna):
    # Verifica la urna seleccionada y obtiene la probabilidad condicional correspondiente
    if urna == 1:
        prob_color_dado_urna = prob_color_dado_urna1[color]
        prob_urna = prob_urna1
    else:
        prob_color_dado_urna = prob_color_dado_urna2[color]
        prob_urna = prob_urna2
    
    # Aplica la regla de Bayes para calcular la probabilidad de que la bola sea de ese color y de esa urna
    prob_color = prob_color_dado_urna * prob_urna
    return prob_color

def main():
    color_elegido = 'amarillo'  # Color elegido
    urna_elegida = 2  # Urna elegida

    probabilidad = calcular_probabilidad_bayes(color_elegido, urna_elegida)

    print(f"La probabilidad de que la bola amarilla provenga de la urna {urna_elegida} es: {probabilidad}")

if __name__ == "__main__":
    main()
