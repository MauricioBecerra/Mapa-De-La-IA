from pgmpy.models import BayesianModel  # Importa la clase BayesianModel desde pgmpy.models
from pgmpy.factors.discrete import TabularCPD  # Importa la clase TabularCPD desde pgmpy.factors.discrete
from pgmpy.inference import VariableElimination  # Importa la clase VariableElimination desde pgmpy.inference

model = BayesianModel([('A', 'B')])  # Define la estructura del modelo bayesiano con el nodo A influyendo en el nodo B

cpd_a = TabularCPD('A', 2, [[0.03], [0.97]])  # Define la tabla de probabilidades condicionales para el nodo A
cpd_b = TabularCPD('B', 2, [[0.95, 0.2],      # Define la tabla de probabilidades condicionales para el nodo B
                            [0.05, 0.8]],
                    evidence=['A'], evidence_card=[2])  # Indica que B depende de A y especifica el número de valores para A

model.add_cpds(cpd_a, cpd_b)  # Añade las probabilidades condicionales al modelo

model.check_model()  # Verifica si el modelo es válido

inference = VariableElimination(model)  # Crea un objeto de inferencia para hacer consultas en la red

posterior = inference.query(variables=['A'], evidence={'B': 0})  # Consulta la probabilidad de A dado B=0
print(posterior)  # Imprime el resultado de la consulta
