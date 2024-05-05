# Definimos las reglas en un diccionario donde la clave es el identificador de la regla y el valor es una tupla (síntoma, enfermedad)
reglas = {
    "R1": ("síntoma1", "enfermedad1"),
    "R2": ("síntoma2", "enfermedad2"),
    "R3": ("síntoma3", "enfermedad1"),
    "R4": ("enfermedad1", "tratamiento1")
}

# Función para diagnosticar las enfermedades basadas en los síntomas proporcionados
def diagnosticar(sintomas):
    enfermedades = set()  # Creamos un conjunto para almacenar las enfermedades diagnosticadas únicas
    for regla, (sintoma, enfermedad) in reglas.items():  # Iteramos sobre cada regla y su asociación de síntoma-enfermedad
        if sintoma in sintomas:  # Si el síntoma está presente en los síntomas proporcionados
            enfermedades.add(enfermedad)  # Añadimos la enfermedad asociada al conjunto de enfermedades
    return enfermedades  # Devolvemos las enfermedades diagnosticadas

# Función para encontrar el tratamiento para una enfermedad dada
def encontrar_tratamiento(enfermedad):
    for regla, (enf, trat) in reglas.items():  # Iteramos sobre cada regla y su asociación de enfermedad-tratamiento
        if enf == enfermedad:  # Si encontramos la enfermedad en las reglas
            return trat  # Devolvemos el tratamiento asociado a esa enfermedad
    return "No se encontró tratamiento"  # Si no se encuentra un tratamiento, devolvemos un mensaje indicando que no se encontró

sintomas_paciente = ["síntoma1", "síntoma3"]  # Síntomas del paciente

enfermedades_diagnosticadas = diagnosticar(sintomas_paciente)  # Realizamos el diagnóstico basado en los síntomas

print("Enfermedad(es) diagnosticada(s):", enfermedades_diagnosticadas)  # Imprimimos las enfermedades diagnosticadas

for enfermedad in enfermedades_diagnosticadas:  # Iteramos sobre cada enfermedad diagnosticada
    tratamiento = encontrar_tratamiento(enfermedad)  # Encontramos el tratamiento para la enfermedad
    print(f"Tratamiento para {enfermedad}: {tratamiento}")  # Imprimimos el tratamiento asociado a la enfermedad
