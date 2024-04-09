import os #importamos os
from collections import deque #Importamos deque desde collections
class Grafo:#inciamos una clase de Grafos que contiene los metodos necesarios para trabajar
    def __init__(self):#constructor de la clase
        self.vertices = {}#incializamos los el diccionario para vertices y aristas
        
    def add_vertice(self, vertice): #funcion para agregar vertices a nuestro diccionario
        if vertice not in self.vertices: #condicion que verifica que el vertice no exista en el diccionario
            self.vertices[vertice] = [] #agrega el vertice
    
    def add_arista(self, vertice1, vertice2): #funcion para agregar aristas a nuestro diccionario
        if vertice1 in self.vertices and vertice2 in self.vertices: #condicion que verifica que ambos vertices existan en el grafo
            self.vertices[vertice1].append(vertice2) #agrega el vertice2 a la listta del vertice1
            self.vertices[vertice2].append(vertice1) #agrega el vertice1 a la listta del vertice2
    
    def bfs(self, est_inicio, est_objetivo): #metodo de busqueda del grafo BFS
        if est_inicio not in self.vertices or est_objetivo not in self.vertices: #Verifica si los estados de inicio y objetivo están en el grafo
            return None #Devuelve None si alguno no está presente
        
        visitados = set() #Conjunto de estados o vertices visitados
        cola = deque() #Conjunto de estados o vertices por visitar
        cola.append((est_inicio, [est_inicio])) #Agrega el punto de incio a la cola
        
        while cola: #Bucle que se repetira mientras existan elementos el la cola
            nodo_actual, ruta = cola.popleft() #Obtine el nodo actual y la ruta desde el inicio de la ruta
            visitados.add(nodo_actual) #Marca el nodo actual como visitado
            if nodo_actual == est_objetivo: #Condicional que si llegamos al nodo objetivo devollvera la ruta
                return ruta
            
            for vecino in self.vertices[nodo_actual]:#Itera sobre los vecinos del estado o vertice actual
                if vecino not in visitados:#Verifica si el vecino no ha sido visitado
                    cola.append((vecino, ruta + [vecino]))  #Agrega el vecino a la cola con la ruta actualizada
                    visitados.add(vecino) #Marca el vecino como visitado
        
        return None

grafo = Grafo()
grafo.add_vertice('Jalisco')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Nayarit')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Zacatecas')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Durango')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Coahuila')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Nuevo Leon')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Chihuahua')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Sinaloa')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Sonora')#Agregamos un vertice o nodo a nuestro grafo
grafo.add_vertice('Baja California')#Agregamos un vertice o nodo a nuestro grafo

grafo.add_arista('Jalisco', 'Nayarit')#Agregamos las aristas de los vertices
grafo.add_arista('Jalisco', 'Zacatecas')#Agregamos las aristas de los vertices
grafo.add_arista('Zacatecas', 'Durango')#Agregamos las aristas de los vertices
grafo.add_arista('Zacatecas', 'Nuevo Leon')#Agregamos las aristas de los vertices
grafo.add_arista('Zacatecas', 'Coahuila')#Agregamos las aristas de los vertices
grafo.add_arista('Nayarit', 'Durango')#Agregamos las aristas de los vertices
grafo.add_arista('Nayarit', 'Sinaloa')#Agregamos las aristas de los vertices
grafo.add_arista('Durango', 'Coahuila')#Agregamos las aristas de los vertices
grafo.add_arista('Durango', 'Chihuahua')#Agregamos las aristas de los vertices
grafo.add_arista('Durango', 'Sinaloa')#Agregamos las aristas de los vertices
grafo.add_arista('Sinaloa', 'Sonora')#Agregamos las aristas de los vertices
grafo.add_arista('Sinaloa', 'Chihuahua')#Agregamos las aristas de los vertices
grafo.add_arista('Coahuila', 'Nuevo Leon')#Agregamos las aristas de los vertices
grafo.add_arista('Coahuila', 'Chihuahua')#Agregamos las aristas de los vertices
grafo.add_arista('Chihuahua', 'Sonora')#Agregamos las aristas de los vertices
grafo.add_arista('Sonora', 'Baja California')#Agregamos las aristas de los vertices

print("Estados: \nJalisco, Nayarit, Zacatecas, Durango, Coahuila, Nuevo Leon, Chihuahua, Sinaloa, Sonora, Baja California")
est_inicio = input("Ingrese el estado de partida: ")
est_objetivo = input("Ingrese el estado est_objetivo: ")
ruta = grafo.bfs(est_inicio, est_objetivo)
if ruta: #Si la ruta es verdadera imprimos la ruta
    print(f"Se encontró un ruta de {est_inicio} a {est_objetivo}: {' -> '.join(ruta)}")
else:
    print(f"No se encontró un ruta de {est_inicio} a {est_objetivo}.")#Si no se encuentra la ruta imprime el msg

os.system("pause")#pausa de la consola