import cv2  # Importa la biblioteca OpenCV para el procesamiento de imágenes
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas

# Lee la imagen desde el archivo "_48_Preprocesado_Filtros_imagen.jpg"
img = cv2.imread('_48_Preprocesado_Filtros_imagen.jpg')

# Convierte la imagen de BGR (rojo, verde, azul) a HSV (matiz, saturación, valor)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Muestra la imagen original en una ventana llamada 'Imagen Original'
cv2.imshow('Imagen Original', img)

# Define el rango de colores bajo y alto para identificar el fondo en HSV
fondo_bajo = np.array([100, 100, 100], np.uint8)
fondo_alto = np.array([140, 255, 255], np.uint8)

# Define un rango de colores que incluya todos los colores posibles
todos_low = np.array([0, 100, 100], np.uint8)
todos_high = np.array([255, 255, 255], np.uint8)

# Crea una máscara para el fondo utilizando el rango de colores definido
mascara_fondo = cv2.inRange(img2, fondo_bajo, fondo_alto)

# Invierte la máscara del fondo para obtener una máscara de todos los píxeles que no son del fondo
mascara_todos = cv2.bitwise_not(mascara_fondo)

# Aplica la máscara de todos los píxeles a la imagen HSV original
mascara = cv2.bitwise_and(img2, img2, mask=mascara_todos)

# Muestra la imagen resultante en una ventana llamada 'Todo'
cv2.imshow('Todo', mascara)

# Espera a que se presione cualquier tecla y luego cierra todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
