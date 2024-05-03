import speech_recognition as sr  # Importa la biblioteca SpeechRecognition para el reconocimiento de voz
import pygame  # Importa la biblioteca Pygame para gráficos
import sys  # Importa la biblioteca sys para interactuar con el sistema operativo

pygame.init()  # Inicializa Pygame
screen = pygame.display.set_mode((800, 600))  # Crea una ventana de 800x600 píxeles
pygame.display.set_caption('Speech Recognition Graphics')  # Establece el título de la ventana

# Función para dibujar un triángulo en la posición (x, y)
def draw_triangle(x, y):
    pygame.draw.polygon(screen, (0, 0, 255), [(x, y-50), (x-50, y+50), (x+50, y+50)])  # Dibuja un triángulo azul

# Función para dibujar un rectángulo en la posición (x, y)
def draw_rectangle(x, y):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x-50, y-50, 100, 200))  # Dibuja un rectángulo rojo

# Función principal
def main():
    recognizer = sr.Recognizer()  # Crea un objeto para el reconocimiento de voz
    command_recognized = False  # Bandera para indicar si se ha reconocido un comando

    running = True  # Bandera para indicar si el programa está en ejecución
    while running:  # Bucle principal del programa
        for event in pygame.event.get():  # Itera sobre los eventos de Pygame
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                running = False  # Establece la bandera de ejecución en False
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_ESCAPE:  # Si la tecla presionada es 'Esc'
                    running = False  # Establece la bandera de ejecución en False

        if not command_recognized:  # Si no se ha reconocido un comando
            with sr.Microphone() as source:  # Abre el micrófono
                print("Diga un comando ('triángulo' o 'rectángulo'):")  # Solicita al usuario que hable un comando
                audio = recognizer.listen(source)  # Escucha el audio del micrófono

            try:  # Intenta reconocer el audio
                command = recognizer.recognize_google(audio)  # Reconoce el comando usando Google Speech Recognition
                print("Comando reconocido:", command)  # Imprime el comando reconocido
                
                if "triángulo" in command:  # Si el comando es "triángulo"
                    draw_triangle(400, 300)  # Dibuja un triángulo en la posición especificada
                elif "rectángulo" in command:  # Si el comando es "rectángulo"
                    draw_rectangle(400, 300)  # Dibuja un rectángulo en la posición especificada
                else:  # Si el comando no es reconocido
                    print("Comando no reconocido")  # Imprime un mensaje indicando que el comando no es reconocido
                
                pygame.display.flip()  # Actualiza la pantalla después de dibujar
                command_recognized = True  # Establece la bandera de comando reconocido en True

            except sr.UnknownValueError:  # Si no se puede entender el audio
                print("No se pudo entender el audio")  # Imprime un mensaje indicando que no se pudo entender el audio
            except sr.RequestError as e:  # Si hay un error en la solicitud
                print("Error al solicitar resultados; {0}".format(e))  # Imprime el error de la solicitud

    pygame.quit()  # Cierra Pygame
    sys.exit()  # Sale del programa

if __name__ == "__main__":  # Si este script es el programa principal
    main()  # Llama a la función principal
