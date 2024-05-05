# Definimos la base de conocimiento que mapea diferentes tipos de clima a actividades recomendadas
base_conocimiento = {
    "soleado": ["jugar al tenis", "ir a la playa"],  # Para clima soleado, se recomiendan actividades al aire libre
    "lluvioso": ["ver una película", "leer un libro"],  # Para clima lluvioso, se recomiendan actividades en interiores
    "nublado": ["salir a caminar", "ir de compras"]  # Para clima nublado, se recomiendan actividades variadas
}

# Función para recomendar actividades basadas en el clima proporcionado
def recomendar_actividad(clima):
    if clima in base_conocimiento:  # Verificamos si el clima está presente en la base de conocimiento
        return base_conocimiento[clima]  # Devolvemos las actividades recomendadas para ese clima
    else:
        return ["No se encontraron actividades recomendadas para este clima."]  # Si no hay actividades para el clima proporcionado, devolvemos un mensaje de error

clima_actual = "soleado"  # Definimos el clima actual

recomendaciones = recomendar_actividad(clima_actual)  # Obtenemos las recomendaciones para el clima actual

print("Actividades recomendadas para el clima", clima_actual + ":")  # Imprimimos el clima actual
for actividad in recomendaciones:  # Iteramos sobre cada actividad recomendada
    print("- " + actividad)  # Imprimimos cada actividad recomendada
