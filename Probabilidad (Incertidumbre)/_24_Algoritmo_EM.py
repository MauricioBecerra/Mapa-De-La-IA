import numpy as np
from sklearn.datasets import make_moons
from sklearn.mixture import GaussianMixture

# Genera datos de ejemplo con dos formas de luna
X, _ = make_moons(n_samples=150, noise=0.1, random_state=42)
# La función make_moons genera datos de puntos en forma de luna.

# Inicializa el modelo de mezcla de Gaussianas con tres componentes
modelo_em = GaussianMixture(n_components=3, random_state=42)
# Crea una instancia del modelo de mezcla de Gaussianas con 3 componentes.

# Entrena el modelo utilizando el algoritmo EM
modelo_em.fit(X)
# Entrena el modelo de mezcla de Gaussianas utilizando los datos X.

# Obtiene las etiquetas de cluster asignadas a cada muestra
etiquetas = modelo_em.predict(X)
# Predice el cluster al que pertenece cada muestra en X.

# Obtiene las medias y matrices de covarianza de los clusters
medias = modelo_em.means_
covarianzas = modelo_em.covariances_
# Obtiene las medias y matrices de covarianza de los clusters identificados por el modelo.

print("Medias de los clusters:")
print(medias)
print("\nMatrices de covarianza de los clusters:")
print(covarianzas)
