import speech_recognition as sr  # Importamos la biblioteca para el reconocimiento de voz
import pygame  # Importamos la biblioteca para gráficos por computadora
import sys  # Importamos la biblioteca para interactuar con el sistema operativo

pygame.init()  # Inicializamos Pygame
screen = pygame.display.set_mode((600, 400))  # Creamos una ventana de 600x400 píxeles
pygame.display.set_caption('Speech Recognition Graphics')  # Establecemos el título de la ventana

def draw_circle(x, y):
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 40)  # Dibujamos un círculo azul

def draw_square(x, y):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x-50, y-50, 100, 100))  # Dibujamos un cuadrado rojo

def main():
    recognizer = sr.Recognizer()  # Creamos un objeto para el reconocimiento de voz
    command_recognized = False  # Bandera para indicar si se ha reconocido un comando

    running = True  # Bandera para indicar si el programa está en ejecución
    while running:  # Bucle principal del programa
        for event in pygame.event.get():  # Iteramos sobre los eventos de Pygame
            if event.type == pygame.QUIT:  # Si se presiona el botón de cierre de la ventana
                running = False  # Establecemos la bandera de ejecución en False
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_ESCAPE:  # Si la tecla presionada es 'Esc'
                    running = False  # Establecemos la bandera de ejecución en False

        if not command_recognized:  # Si no se ha reconocido un comando
            with sr.Microphone() as source:  # Abrimos el micrófono
                print("Diga un comando ('círculo' o 'cuadrado'):")  # Pedimos al usuario que diga un comando
                audio = recognizer.listen(source)  # Escuchamos el audio del micrófono

            try:  # Intentamos reconocer el audio
                command = recognizer.recognize_google(audio)  # Reconocemos el comando usando Google Speech Recognition
                print("Comando reconocido:", command)  # Imprimimos el comando reconocido

                if "círculo" in command:  # Si el comando es "círculo"
                    draw_circle(300, 200)  # Dibujamos un círculo en la posición especificada
                elif "cuadrado" in command:  # Si el comando es "cuadrado"
                    draw_square(300, 200)  # Dibujamos un cuadrado en la posición especificada
                else:  # Si el comando no es reconocido
                    print("Comando no reconocido")  # Imprimimos un mensaje indicando que el comando no es reconocido

                pygame.display.flip()  # Actualizamos la pantalla después de dibujar
                command_recognized = True  # Establecemos la bandera de comando reconocido en True

            except sr.UnknownValueError:  # Si no se puede entender el audio
                print("No se pudo entender el audio")  # Imprimimos un mensaje indicando que no se pudo entender el audio
            except sr.RequestError as e:  # Si hay un error en la solicitud
                print("Error al solicitar resultados; {0}".format(e))  # Imprimimos el error de la solicitud

    pygame.quit()  # Cerramos Pygame
    sys.exit()  # Salimos del programa

if __name__ == "__main__":  # Si este script es el programa principal
    main()  # Llamamos a la función principal
