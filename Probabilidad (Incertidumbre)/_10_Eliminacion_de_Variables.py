from pgmpy.models import BayesianModel  # Importa la clase BayesianModel del módulo pgmpy.models
from pgmpy.factors.discrete import TabularCPD  # Importa la clase TabularCPD del módulo pgmpy.factors.discrete
from pgmpy.inference import VariableElimination  # Importa la clase VariableElimination del módulo pgmpy.inference

model = BayesianModel([('I', 'S'), ('I', 'R')])  # Define la estructura del modelo bayesiano

cpd_infeccion = TabularCPD('I', 2, [[0.02], [0.98]])  # Define la TabularCPD para la variable 'I' (Infección)

cpd_sintoma = TabularCPD('S', 2, [[0.7, 0.1], [0.3, 0.9]], evidence=['I'], evidence_card=[2])  # Define la TabularCPD para la variable 'S' (Síntoma)

cpd_recuperacion = TabularCPD('R', 2, [[0.8, 0.4], [0.2, 0.6]], evidence=['I'], evidence_card=[2])  # Define la TabularCPD para la variable 'R' (Recuperación)

model.add_cpds(cpd_infeccion, cpd_sintoma, cpd_recuperacion)  # Añade las CPDs al modelo

model.check_model()  # Verifica la validez del modelo

inference = VariableElimination(model)  # Crea un objeto VariableElimination para realizar la inferencia

marginal_infeccion = inference.query(variables=['I'])  # Consulta la distribución marginal de 'I' (Infección)

print(marginal_infeccion)  # Imprime la distribución marginal de 'I'
