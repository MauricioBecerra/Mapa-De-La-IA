class KnowledgeBase:
    def __init__(self):
        self.beliefs = {}

    def add_belief(self, event, belief):
        self.beliefs[event] = belief

    def get_belief(self, event):
        return self.beliefs.get(event, 0.0)

    def update_belief(self, event, new_belief):
        if event in self.beliefs:
            self.beliefs[event] = new_belief
        else:
            print(f"El evento {event} no está en la base de conocimiento.")

    def print_beliefs(self):
        for event, belief in self.beliefs.items():
            print(f"{event}: {belief}")

kb = KnowledgeBase()

kb.add_belief("Exito", 0.7)
kb.add_belief("Fracaso", 0.3)

print("Creencias iniciales:")
kb.print_beliefs()
print()

kb.update_belief("Exito", 0.9)

print("Creencias actualizadas:")
kb.print_beliefs()
