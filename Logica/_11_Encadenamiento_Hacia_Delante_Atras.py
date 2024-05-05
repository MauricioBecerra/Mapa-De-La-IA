class KnowledgeBase:
    def __init__(self):
        self.facts = []  # Lista para almacenar hechos
        self.rules = []  # Lista para almacenar reglas

    def tell_fact(self, fact):
        self.facts.append(fact)  # Agrega un hecho a la base de conocimiento

    def tell_rule(self, rule):
        self.rules.append(rule)  # Agrega una regla a la base de conocimiento

    # Realiza el encadenamiento hacia adelante para inferir nuevos hechos a partir de la base de conocimiento
    def forward_chain(self, query):
        inferred_facts = set()  # Conjunto para almacenar hechos inferidos
        agenda = [query]  # Lista de metas para ser procesadas

        while agenda:
            current_fact = agenda.pop(0)  # Toma una meta de la agenda
            if current_fact in self.facts:  # Si la meta ya es un hecho conocido, pasa a la siguiente
                continue

            inferred_facts.add(current_fact)  # Agrega la meta a los hechos inferidos

            for rule in self.rules:  # Itera sobre las reglas en la base de conocimiento
                if all(p in inferred_facts for p in rule.antecedents):  # Si todas las antecedentes de la regla son inferidas
                    agenda.append(rule.consequent)  # Agrega el consecuente de la regla a la agenda

        return inferred_facts  # Devuelve los hechos inferidos

    # Realiza el encadenamiento hacia atrás para encontrar un camino para alcanzar una meta desde la base de conocimiento
    def backward_chain(self, query):
        agenda = [(query, [])]  # Lista de metas para ser procesadas, cada elemento también incluye un camino

        while agenda:
            current_fact, path = agenda.pop(0)  # Toma una meta y su camino asociado de la agenda
            if current_fact in self.facts:  # Si la meta ya es un hecho conocido, pasa a la siguiente
                continue

            path = path + [current_fact]  # Agrega la meta actual al camino

            for rule in self.rules:  # Itera sobre las reglas en la base de conocimiento
                if rule.consequent == current_fact:  # Si la meta coincide con el consecuente de la regla
                    sub_goals = rule.antecedents  # Obtiene los antecedentes de la regla
                    new_path = path.copy()  # Copia el camino actual para no modificarlo
                    new_path.append(rule)  # Agrega la regla al camino
                    agenda.extend([(p, new_path) for p in sub_goals])  # Agrega los antecedentes a la agenda con el nuevo camino

        return path  # Devuelve el camino encontrado


class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents  # Antecedentes de la regla
        self.consequent = consequent  # Consecuente de la regla


if __name__ == "__main__":
    kb = KnowledgeBase()

    # Se definen algunos hechos y reglas
    kb.tell_fact("padre(juan, pepe)")
    kb.tell_fact("padre(pepe, maria)")
    kb.tell_rule(Rule(["padre(X, Y)"], "abuelo(X, Z)"))

    query = "abuelo(juan, maria)"  # Meta a ser probada

    # Realiza encadenamiento hacia adelante e imprime los hechos inferidos
    inferred_facts = kb.forward_chain(query)
    print("Hechos inferidos con encadenamiento hacia adelante:", inferred_facts)

    # Realiza encadenamiento hacia atrás e imprime el camino encontrado
    path = kb.backward_chain(query)
    print("Camino encontrado con encadenamiento hacia atrás:")
    for step in path:
        if isinstance(step, Rule):
            print("Aplicar regla:", step.antecedents, "->", step.consequent)  # Imprime la regla aplicada
        else:
            print("Hecho:", step)  # Imprime el hecho
