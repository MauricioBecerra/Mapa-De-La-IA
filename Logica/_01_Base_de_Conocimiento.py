class BaseConocimiento:
    def __init__(self):
        self.hechos = set()  # Conjunto para almacenar los hechos conocidos
        self.reglas = []      # Lista para almacenar las reglas de inferencia

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)  # Agrega un hecho al conjunto de hechos

    def agregar_regla(self, premisas, conclusion):
        self.reglas.append((premisas, conclusion))  # Agrega una regla a la lista de reglas

    def consultar(self, proposicion):
        return self._evaluar(proposicion)  # Llama al método privado _evaluar para evaluar una proposición

    def _evaluar(self, proposicion):
        if proposicion in self.hechos:  # Si la proposición está en los hechos conocidos
            return True

        for premisas, conclusion in self.reglas:  # Itera sobre todas las reglas
            if all(p in self.hechos for p in premisas):  # Si todas las premisas están en los hechos conocidos
                self.hechos.add(conclusion)  # Agrega la conclusión a los hechos conocidos
                return conclusion == proposicion  # Retorna verdadero si la conclusión coincide con la proposición buscada

        return False  # Si no se encuentra la proposición

if __name__ == "__main__":
    base_conocimiento = BaseConocimiento()  # Instancia de la base de conocimiento

    base_conocimiento.agregar_hecho("a")  # Agrega el hecho "a"
    base_conocimiento.agregar_hecho("b")  # Agrega el hecho "b"
    base_conocimiento.agregar_regla(["a", "b"], "c")  # Agrega la regla "Si a y b, entonces c"

    print(base_conocimiento.consultar("c"))  # Consulta si "c" es verdadero (debería serlo)
    print(base_conocimiento.consultar("a"))  # Consulta si "a" es verdadero (debería serlo)
    print(base_conocimiento.consultar("d"))  # Consulta si "d" es verdadero (debería ser falso)
