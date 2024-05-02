def probabilidad_conjunta(prob_X, prob_Y_dado_X, prob_Z_dado_Y):
    # Calcula la probabilidad conjunta de los eventos X, Y y Z utilizando la regla de la cadena.
    prob_Y = prob_Y_dado_X * prob_X  # Calcula la probabilidad de Y dado X
    prob_Z = prob_Z_dado_Y * prob_Y  # Calcula la probabilidad de Z dado Y
    return prob_Z  # Devuelve la probabilidad conjunta de Z

prob_X = 0.3  # Probabilidad del evento X
prob_Y_dado_X = 0.8  # Probabilidad de Y dado X
prob_Z_dado_Y = 0.6  # Probabilidad de Z dado Y

prob_conjunta = probabilidad_conjunta(prob_X, prob_Y_dado_X, prob_Z_dado_Y)  # Calcula la probabilidad conjunta de X, Y y Z

print("La probabilidad conjunta de los eventos X, Y y Z es:", prob_conjunta)  # Imprime la probabilidad conjunta de X, Y y Z