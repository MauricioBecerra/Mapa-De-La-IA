class FormulaLogica:
    def __init__(self, formula):
        self.formula = formula  # Almacena la fórmula lógica

    def __str__(self):
        return self.formula  # Devuelve la representación de la fórmula como string

    def equivalente(self, otra_formula):
        return self.formula == otra_formula.formula  # Comprueba si dos fórmulas son equivalentes

    def es_valida(self):
        return self.evaluar(True) and self.evaluar(False)  # Verifica si la fórmula es válida

    def es_satisfacible(self):
        return self.evaluar(True) or self.evaluar(False)  # Verifica si la fórmula es satisfacible

    def evaluar(self, valor):
        if self.formula == "¬P":
            return not valor  # Si la fórmula es "¬P", devuelve el valor opuesto
        elif self.formula == "P":
            return valor  # Si la fórmula es "P", devuelve el valor

# Crear instancias de fórmulas lógicas
formula_1 = FormulaLogica("P")
formula_2 = FormulaLogica("Q")

# Comprobar equivalencia entre fórmulas
print(f"Las fórmulas son equivalentes: {formula_1.equivalente(formula_2)}")

# Comprobar validez de las fórmulas
print(f"La fórmula 1 es válida: {formula_1.es_valida()}")
print(f"La fórmula 2 es válida: {formula_2.es_valida()}")

# Comprobar satisfactibilidad de las fórmulas
print(f"La fórmula 1 es satisfacible: {formula_1.es_satisfacible()}")
print(f"La fórmula 2 es satisfacible: {formula_2.es_satisfacible()}")
