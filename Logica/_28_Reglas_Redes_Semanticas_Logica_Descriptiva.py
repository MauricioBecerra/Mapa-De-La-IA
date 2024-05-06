class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

class RedSemantica:
    def __init__(self):
        self.relaciones = {}

    def agregar_relacion(self, objeto1, relacion, objeto2):
        if objeto1 not in self.relaciones:
            self.relaciones[objeto1] = {}
        self.relaciones[objeto1][relacion] = objeto2

    def buscar_relacion(self, objeto1, relacion):
        if objeto1 in self.relaciones and relacion in self.relaciones[objeto1]:
            return self.relaciones[objeto1][relacion]
        else:
            return None

red_semantica = RedSemantica()

red_semantica.agregar_relacion("gato", "es", "felino")
red_semantica.agregar_relacion("perro", "es", "canino")
red_semantica.agregar_relacion("animal", "es", "organismo vivo")
red_semantica.agregar_relacion("cachorro", "es", "joven canino")
red_semantica.agregar_relacion("cachorro", "tiene", "dientes afilados")

reglas = [
    Regla(["gato"], ["es", "felino"]),
    Regla(["perro"], ["es", "canino"]),
    Regla(["animal"], ["es", "organismo vivo"]),
    Regla(["cachorro"], ["es", "joven canino"]),
    Regla(["cachorro"], ["tiene", "dientes afilados"])
]

def consultar(red_semantica, reglas, objeto):
    resultado = []
    for regla in reglas:
        if regla.antecedente[0] == objeto:
            resultado.append((regla.consecuente[0], regla.consecuente[1]))
    return resultado

objeto_consultado = "cachorro"
resultado_consulta = consultar(red_semantica, reglas, objeto_consultado)
print(f"Propiedades de '{objeto_consultado}': {resultado_consulta}")
