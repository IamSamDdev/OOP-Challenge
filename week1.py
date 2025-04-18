

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5        # Moderate hunger to start
        self.energy = 5        # Moderate energy
        self.happiness = 5     # Moderately happy
        self.tricks = []       # Empty list for learned tricks

    def eat(self):
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} eats happily. 🍽️")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} takes a nap. 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} plays and has fun! 🎾")
        else:
            print(f"{self.name} is too tired to play. 😓")

    def get_status(self):
        print(f"📋 {self.name}'s Status:")
        print(f"   Hunger: {self.hunger}/10")
        print(f"   Energy: {self.energy}/10")
        print(f"   Happiness: {self.happiness}/10")
        print("-" * 30)

    # Bonus Methods
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}! 🐕‍🦺")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Example usage:
if __name__ == "__main__":
    tommy = Pet("jerry")

    jerry.get_status()
    jerry.eat()
    jerry.sleep()
    jerry.play()
    jerry.train("roll over")
    jerry.train("shake hands")
    jerry.show_tricks()
    jerry.get_status()
