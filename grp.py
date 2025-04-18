class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting with moderate hunger
        self.energy = 5  # Starting with moderate energy
        self.happiness = 5  # Starting with moderate happiness
        self.tricks = []  # For storing learned tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")
    
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play right now.")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'▣' * (10 - self.hunger)}{'□' * self.hunger} ({self.hunger}/10)")
        print(f"Energy: {'▣' * self.energy}{'□' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'▣' * self.happiness}{'□' * (10 - self.happiness)} ({self.happiness}/10)")
        
        # Status messages based on levels
        if self.hunger >= 8:
            print(f"{self.name} is very hungry!")
        elif self.hunger >= 5:
            print(f"{self.name} is getting peckish.")
        
        if self.energy <= 2:
            print(f"{self.name} is exhausted!")
        elif self.energy <= 5:
            print(f"{self.name} is getting sleepy.")
        
        if self.happiness >= 8:
            print(f"{self.name} is extremely happy!")
        elif self.happiness <= 2:
            print(f"{self.name} seems sad.")
    
    def train(self, trick):
        if self.energy >= 3:
            self.energy -= 1
            self.hunger = min(10, self.hunger + 1)
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to learn new tricks right now.")
    
    def show_tricks(self):
        if self.tricks:
            print(f"\n{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


            # Create a pet
my_pet = Pet("Dog")

# Interact with the pet
my_pet.play()
my_pet.eat()
my_pet.sleep()
my_pet.train("sit")
my_pet.train("roll over")

# Check status and tricks
my_pet.get_status()
my_pet.show_tricks()
