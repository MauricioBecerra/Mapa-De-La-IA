def membership_temperature_cold(temp):
    if temp <= 50:
        return 1  # Máxima membresía si la temperatura es menor o igual a 50
    elif temp > 50 and temp < 70:
        return (70 - temp) / (70 - 50)  # Calcula la membresía linealmente decreciente
    else:
        return 0  # Si la temperatura es mayor o igual a 70, la membresía es cero

def membership_temperature_medium(temp):
    if temp <= 50 or temp >= 90:
        return 0  # Si la temperatura es menor o igual a 50 o mayor o igual a 90, la membresía es cero
    elif temp > 50 and temp < 70:
        return (temp - 50) / (70 - 50)  # Calcula la membresía linealmente creciente
    elif temp >= 70 and temp <= 90:
        return 1  # Máxima membresía si la temperatura está entre 70 y 90
    else:
        return 0  # Si la temperatura es menor a 50 o mayor a 90, la membresía es cero

def membership_temperature_hot(temp):
    if temp <= 70:
        return 0  # Si la temperatura es menor o igual a 70, la membresía es cero
    elif temp > 70 and temp < 90:
        return (temp - 70) / (90 - 70)  # Calcula la membresía linealmente creciente
    else:
        return 1  # Máxima membresía si la temperatura es mayor o igual a 90

def membership_fan_speed_low(speed):
    if speed <= 50:
        return 1  # Máxima membresía si la velocidad es menor o igual a 50
    elif speed > 50 and speed < 70:
        return (70 - speed) / (70 - 50)  # Calcula la membresía linealmente decreciente
    else:
        return 0  # Si la velocidad es mayor o igual a 70, la membresía es cero

def membership_fan_speed_medium(speed):
    if speed <= 50 or speed >= 90:
        return 0  # Si la velocidad es menor o igual a 50 o mayor o igual a 90, la membresía es cero
    elif speed > 50 and speed < 70:
        return (speed - 50) / (70 - 50)  # Calcula la membresía linealmente creciente
    elif speed >= 70 and speed <= 90:
        return 1  # Máxima membresía si la velocidad está entre 70 y 90
    else:
        return 0  # Si la velocidad es menor a 50 o mayor a 90, la membresía es cero

def membership_fan_speed_high(speed):
    if speed <= 70:
        return 0  # Si la velocidad es menor o igual a 70, la membresía es cero
    elif speed > 70 and speed < 90:
        return (speed - 70) / (90 - 70)  # Calcula la membresía linealmente creciente
    else:
        return 1  # Máxima membresía si la velocidad es mayor o igual a 90

def fuzzy_inference(temp):
    # Calcula la membresía para las tres velocidades del ventilador
    low_speed = min(membership_temperature_cold(temp), membership_fan_speed_low(temp))
    medium_speed = min(membership_temperature_medium(temp), membership_fan_speed_medium(temp))
    high_speed = min(membership_temperature_hot(temp), membership_fan_speed_high(temp))

    # Calcula el numerador y el denominador para obtener la velocidad del ventilador
    numerator = low_speed * 25 + medium_speed * 60 + high_speed * 85
    denominator = low_speed + medium_speed + high_speed
    if denominator == 0:
        return 0
    return numerator / denominator

temperature = 75
fan_speed = fuzzy_inference(temperature)
print("Fan speed:", fan_speed)
