def Menu(): #Se crea una función para imprimir el menú de opciones
    print('1.-Multiplicar 2 numeros.') #Imprime la opción de multiplicar dos números
    print('2.-Dividir 2 numeros.') #Imprime la opción de dividir dos números
    print('3.-Elevar al cubo un numero.') #Imprime la opción de elevar al cubo un número
    print('4.-Salir') #Imprime la opción de salir del programa
    
def invocacion(respuesta: int): #Se define una función que asocia una respuesta numérica con una acción
    menu={ #Se crea un diccionario que mapea las opciones del menú a sus valores numéricos correspondientes
            1:1,
            2:2,
            3:3,
            4:4
        }
    return menu.get(respuesta, "Opción inválida") #Devuelve la acción asociada a la respuesta o "Opción inválida" si no existe

respuesta=0 #Se inicializa la variable 'respuesta' con 0    
while respuesta!=4: #Se inicia un bucle que se ejecutará mientras la respuesta no sea 4 (Salir)
    
    Menu() #Se llama a la función Menu para mostrar las opciones
    respuesta=int(input(print('Seleccione una opcion: '))) #Se solicita al usuario que seleccione una opción y se convierte la entrada a entero
    menu=invocacion(respuesta) #Se llama a la función invocacion para obtener la acción correspondiente a la opción seleccionada
    if menu ==1: #Si la opción seleccionada es 1 (Multiplicar)
        num1=int(input('Dame el 1er numero\n')) #Se solicita al usuario el primer número para la multiplicación
        num2=int(input('Dame el 2do numero\n')) #Se solicita al usuario el segundo número para la multiplicación
        resultado=num1*num2 #Se calcula el resultado de la multiplicación
        print('El resultado es: ',resultado) #Se imprime el resultado de la multiplicación
    elif menu==2: #Si la opción seleccionada es 2 (Dividir)
        num1=int(input('Dame el 1er numero\n')) #Se solicita al usuario el primer número para la división
        num2=int(input('Dame el 2do numero\n')) #Se solicita al usuario el segundo número para la división
        resultado=num1/num2 #Se calcula el resultado de la división
        print('El resultado es: ',resultado) #Se imprime el resultado de la división
    elif menu==3: #Si la opción seleccionada es 3 (Elevar al cubo)
        num1=int(input('Dame el numero\n')) #Se solicita al usuario un número para elevar al cubo
        resultado=num1**3 #Se calcula el cubo del número
        print('El resultado es: ',resultado) #Se imprime el resultado de elevar al cubo
