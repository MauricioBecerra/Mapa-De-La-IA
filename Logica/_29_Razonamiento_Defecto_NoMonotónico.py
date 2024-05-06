class KnowledgeBase:
    def __init__(self):
        # Inicializa tres conjuntos para hechos, reglas por defecto y reglas no por defecto
        self.facts = set()
        self.default_rules = set()
        self.non_default_rules = set()

    def add_fact(self, fact):
        # Agrega un hecho al conjunto de hechos
        self.facts.add(fact)

    def add_default_rule(self, rule):
        # Agrega una regla por defecto al conjunto de reglas por defecto
        self.default_rules.add(rule)

    def add_non_default_rule(self, rule):
        # Agrega una regla no por defecto al conjunto de reglas no por defecto
        self.non_default_rules.add(rule)

    def infer(self, fact):
        # Verifica si un hecho es verdadero, o si puede ser inferido por las reglas por defecto
        if fact in self.facts:
            return True
        for rule in self.default_rules:
            if rule.implies(fact):
                return True
        return False

class Rule:
    def __init__(self, condition, result):
        # Inicializa una regla con una condición y un resultado
        self.condition = condition
        self.result = result

    def implies(self, fact):
        # Verifica si el resultado de la regla es el mismo que el hecho
        return self.result == fact

    def __str__(self):
        # Devuelve la representación en cadena de la regla
        return f"{self.condition} -> {self.result}"

kb = KnowledgeBase()

# Agrega dos reglas por defecto
kb.add_default_rule(Rule("bird(X)", "flies(X)"))
kb.add_default_rule(Rule("flies(X)", "bird(X)"))

# Agrega una regla no por defecto
kb.add_non_default_rule(Rule("bird(penguin)", "flies(penguin)"))

# Agrega un hecho al conjunto de hechos
kb.add_fact("bird(penguin)")

# Realiza una inferencia sobre si "flies(penguin)" es verdadero
if kb.infer("flies(penguin)"):
    print("El pingüino vuela.")
else:
    print("El pingüino no vuela.")
