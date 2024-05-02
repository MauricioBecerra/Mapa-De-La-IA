import numpy as np
from hmmlearn import hmm

# Creamos una instancia del modelo HMM con 4 estados ocultos y matriz de covarianza esférica
modelo_hmm = hmm.GaussianHMM(n_components=4, covariance_type="spherical")

# Definimos una secuencia de observaciones
secuencia_observaciones = np.array([[0.5], [1.5], [2.5], [3.5], [4.5]])

# Entrenamos el modelo HMM con la secuencia de observaciones
modelo_hmm.fit(secuencia_observaciones)

# Predecimos los estados ocultos correspondientes a la secuencia de observaciones
estados_ocultos_predichos = modelo_hmm.predict(secuencia_observaciones)

# Generamos nuevas observaciones a partir del modelo entrenado
observaciones_predichas, _ = modelo_hmm.sample(len(secuencia_observaciones))

# Imprimimos los estados ocultos y las observaciones predichas
print("Estados ocultos predichos:", estados_ocultos_predichos)
print("Observaciones predichas:", observaciones_predichas)
