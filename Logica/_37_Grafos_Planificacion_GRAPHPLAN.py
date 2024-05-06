import networkx as nx

def graphplan(estado_inicial, estado_objetivo, acciones):
    G = nx.DiGraph()  # Creamos un grafo dirigido

    G.add_node('estado_inicial', tipo='estado')  # Añadimos el nodo para el estado inicial
    G.add_node('estado_objetivo', tipo='estado')  # Añadimos el nodo para el estado objetivo

    for accion in acciones:  # Añadimos nodos para las acciones
        G.add_node(accion, tipo='accion')

    for accion in acciones:  # Añadimos arcos desde el estado inicial a las acciones aplicables
        if all(pre in estado_inicial for pre in acciones[accion]['precondiciones']):
            G.add_edge('estado_inicial', accion)

    for accion in acciones:  # Añadimos arcos desde las acciones a sus efectos
        for efecto in acciones[accion]['efectos']:
            G.add_edge(accion, efecto)

    for estado in estado_objetivo:  # Añadimos arcos desde los efectos al estado objetivo
        G.add_edge(estado, 'estado_objetivo')

    try:
        # Intentamos encontrar el camino más corto desde el estado inicial al estado objetivo
        return nx.shortest_path(G, source='estado_inicial', target='estado_objetivo')
    except nx.NetworkXNoPath:  # Si no hay camino, devolvemos None
        return None

# Definimos un nuevo estado inicial y objetivo, y modificamos las acciones
estado_inicial = ['En(A)', 'Libre(B)', 'ManoVacia']
estado_objetivo = ['Sobre(B, A)', 'Libre(A)', 'ManoVacia']
acciones = {
    'Recoger(A)': {
        'precondiciones': ['En(A)', 'Libre(A)', 'ManoVacia'],
        'efectos': ['Sosteniendo(A)', 'Libre(A)', 'ManoVacia']
    },
    'Soltar(A)': {
        'precondiciones': ['Sosteniendo(A)'],
        'efectos': ['En(A)', 'Libre(A)', 'ManoVacia']
    },
    'Apilar(A, B)': {
        'precondiciones': ['Sosteniendo(A)', 'Libre(B)'],
        'efectos': ['Sobre(A, B)', 'Libre(A)', 'ManoVacia']
    },
    'Desapilar(A, B)': {
        'precondiciones': ['Sobre(A, B)', 'Libre(A)', 'ManoVacia'],
        'efectos': ['Sosteniendo(A)', 'Libre(B)']
    }
}

plan = graphplan(estado_inicial, estado_objetivo, acciones)

if plan:
    print("Plan encontrado:")
    for paso in plan[1:]:  # Excluimos el primer paso que es el estado inicial
        print(paso)
else:
    print("No se encontró un plan.")
