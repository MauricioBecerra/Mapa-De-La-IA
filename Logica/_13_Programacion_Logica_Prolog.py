from pyDatalog import pyDatalog

# Definimos los términos 'padre', 'abuelo', 'X', 'Y' y 'Z' utilizando pyDatalog
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

# Definimos los hechos de la relación 'padre'
+padre('Juan', 'Pedro')
+padre('Pedro', 'Pablo')
+padre('Pedro', 'María')

# Definimos la regla de inferencia para la relación 'abuelo'
abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)

# Consultamos quién es el abuelo de Pablo
print(abuelo(X, 'Pablo'))

# Consultamos quién es el abuelo de María
print(abuelo(X, 'María'))
