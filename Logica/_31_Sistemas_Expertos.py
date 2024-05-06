class KnowledgeBase:
    def __init__(self):
        self.rules = {}  # Inicializa un diccionario para almacenar las reglas de enfermedades y sus síntomas asociados

    def add_rule(self, disease, symptoms):
        self.rules[disease] = symptoms  # Agrega una nueva regla de enfermedad con sus síntomas asociados al diccionario de reglas

    def infer_disease(self, symptoms):
        matched_diseases = []  # Inicializa una lista para almacenar las enfermedades que coinciden con los síntomas proporcionados
        for disease, symptoms_list in self.rules.items():  # Itera sobre cada regla en el diccionario de reglas
            # Verifica si los síntomas coinciden con los síntomas de una enfermedad
            if set(symptoms).issubset(set(symptoms_list)):
                matched_diseases.append(disease)  # Agrega la enfermedad a la lista si los síntomas coinciden
        if matched_diseases:  # Si se encontraron enfermedades que coinciden con los síntomas
            return matched_diseases  # Retorna todas las enfermedades que coinciden con los síntomas
        else:
            return "No se puede diagnosticar la enfermedad"  # Retorna un mensaje si no se encuentra ninguna enfermedad que coincida

kb = KnowledgeBase()

# Agregamos reglas para diferentes enfermedades con sus síntomas asociados
kb.add_rule("Resfriado", ["Congestión nasal", "Estornudos", "Garganta irritada"])
kb.add_rule("Gripe", ["Fiebre", "Dolor de cabeza", "Dolor muscular"])
kb.add_rule("Alergia", ["Estornudos", "Picazón en los ojos", "Secreción nasal"])
kb.add_rule("Resfrío", ["Estornudos", "Dolor de garganta"])

# Síntomas de un paciente
symptoms = ["Estornudos", "Garganta irritada"]

print("Diagnóstico para síntomas:", symptoms)
print("Enfermedades diagnosticadas:", kb.infer_disease(symptoms))  # Imprime las enfermedades que coinciden con los síntomas
