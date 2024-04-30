import project

class ClearingScene(project.Scene):
    def __init__(self):
        super().__init__(
            description="You emerge into a small clearing. Sunlight bathes the area in a warm glow. A lone bandit stands in the center, blocking your path.",
            exits={"south": "forest"},
            actions={
                "look": lambda p: print("You see a bandit guarding the southern path."),
                "enemy": Bandit(),  # Enemy object defined in actions
            },
        )


class Bandit:
    def __init__(self):
        self.name = "Bandit"
        self.health = 50
        self.attack = 15

    def attack(self, player):
        player.take_damage(self.attack)
        print(f"The {self.name} swings a club at you, dealing {self.attack} damage!")


class ForestScene(project.Scene):
    def __init__(self):
        super().__init__(
            description="You stand in a dense forest. Sunlight struggles to penetrate the thick canopy of leaves above. The air is filled with the chirping of birds and the rustling of unseen creatures.",
            exits={"north": "clearing"},
            actions={
                "look": lambda p: print(
                    "You see towering trees and a faint path leading north."
                ),
                "enemy": Goblin(),  # Enemy object defined in actions
            },
        )


class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.health = 30
        self.attack = 10

    def attack(self, player):
        player.take_damage(self.attack)
        print(f"The {self.name} scratches you, dealing {self.attack} damage!")