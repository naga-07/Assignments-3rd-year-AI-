class VacuumCleanerAgent:
    def __init__(self):
        self.location = "A" # starting location
        self.status = "Dirty" # starting status of the room
        self.rulebase = [
            {'condition': lambda percept, status: percept == "Dirty" and status == "Dirty", 'action': "Suck"},
            {'condition': lambda percept, status: percept == "Clean" and status == "Clean" and self.location == "A", 'action': "Right"},
            {'condition': lambda percept, status: percept == "Clean" and status == "Clean" and self.location == "B", 'action': "Left"},
            {'condition': lambda percept, status: percept == "Clean" and status == "Dirty", 'action': "Suck"}
        ]
    
    def execute_action(self, percept):
        for rule in self.rulebase:
            if rule['condition'](percept, self.status):
                if rule['action'] == "Suck":
                    self.status = "Clean"
                elif rule['action'] == "Right":
                    self.location = "B"
                elif rule['action'] == "Left":
                    self.location = "A"
                return rule['action']

agent = VacuumCleanerAgent()
percepts = ["Dirty", "Clean", "Clean", "Dirty", "Clean"]

for percept in percepts:
    action = agent.execute_action(percept)
    print("Percept: ", percept)
    print("Action: ", action)
    print("Location: ", agent.location)
    print("Status: ", agent.status)
    print()

