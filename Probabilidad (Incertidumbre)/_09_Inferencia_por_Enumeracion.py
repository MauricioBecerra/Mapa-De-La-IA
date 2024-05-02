from pgmpy.models import BayesianModel  # Importa la clase BayesianModel del módulo models de pgmpy
from pgmpy.factors.discrete import TabularCPD  # Importa la clase TabularCPD del módulo discrete de pgmpy
from pgmpy.inference import VariableElimination  # Importa la clase VariableElimination del módulo inference de pgmpy

model = BayesianModel([('E', 'T')])  # Crea un objeto BayesianModel con una estructura de un nodo E que influye en un nodo T

cpd_enfermedad = TabularCPD('E', 2, [[0.02], [0.98]])  # Crea una TabularCPD para el nodo E (enfermedad)
cpd_tratamiento = TabularCPD('T', 2, [[0.85, 0.3], [0.15, 0.7]], evidence=['E'], evidence_card=[2])  # Crea una TabularCPD para el nodo T (tratamiento) dependiente de E

model.add_cpds(cpd_enfermedad, cpd_tratamiento)  # Añade las CPD al modelo

model.check_model()  # Verifica la validez del modelo

inference = VariableElimination(model)  # Crea un objeto de inferencia VariableElimination para el modelo

posterior = inference.query(variables=['E'], evidence={'T': 0})  # Realiza una consulta para calcular la probabilidad de E dada T=0

print(posterior)  # Imprime el resultado de la inferencia
