import cv2
import numpy as np 

img = cv2.imread('_48_Preprocesado_Filtros_imagen.jpg')



# Si la imagen no se carga, es posible que la ruta sea incorrecta o la imagen no exista
if img is None:
    print("No se pudo cargar la imagen. Verifica la ruta y asegúrate de que la imagen exista.")
else:
    # Convertir la imagen a HSV
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir el rango de color azul en HSV
    b_low = np.array([100, 50, 50], np.uint8)
    b_high = np.array([120, 255, 255], np.uint8)


    # Aplicar la máscara para detectar el color amarillo
    mascara2 = cv2.inRange(img2, b_low, b_high)

    # Mostrar la imagen original
    cv2.imshow('Imagen Original', img)

    # Mostrar la máscara amarilla
    cv2.imshow('Amarillo', mascara2)

    # Esperar a que se presione una tecla y cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

