# from config import OPENAI_API_KEY
# from openai import OpenAI

# client = OpenAI(api_key=OPENAI_API_KEY)


class Player:
    def __init__(self, health=100, sword=None):
        self.health = health
        self.sword = sword  # Starts the game with no weapons

    def equip_sword(self):
        self.sword = "sword"
        self.sword_damage = 40

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You have died.")

    def attack_melee(self):
        if self.sword:
            return self.sword_damage
        else:
            print("You don't have a melee weapon equipped!")
            return 0  # Indicate no damage


class Scene:
    def __init__(self, description, exits, actions):
        self.description = description
        self.exits = exits  # Dictionary: {"north": next_scene, ...}
        self.actions = actions  # Dictionary: {"look": method, ...}

    def enter(self):
        print(self.description)

    def get_exits(self):
        return self.exits.keys()

    def move(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        else:
            print("You can't go that way.")

    def do_action(self, action, player):
        if action == "attack":
            if "enemy" in self.actions:  # Check if scene has an enemy
                enemy = self.actions["enemy"]  # Get enemy object from scene actions
                player_damage = player.attack_melee()  # Or player.attack_ranged()
                enemy.take_damage(player_damage)
                print(f"You attack the {enemy.name}, dealing {player_damage} damage!")
                if enemy.health > 0:  # Enemy survives, retaliates
                    enemy_damage = (
                        enemy.attack
                    )  # Assuming enemy has an 'attack' attribute
                    player.take_damage(enemy_damage)
                    print(
                        f"The {enemy.name} retaliates, dealing {enemy_damage} damage!"
                    )
            else:
                print("There is no enemy here to attack.")
        elif action in self.actions:
            self.actions[action](
                player
            )  # Call the action method with player as argument
        else:
            print("You can't do that here.")


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, player):
        player.take_damage(self.attack)
        print(f"The {self.name} attacks you, dealing {self.attack} damage!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The {self.name} is defeated!")


class ClearingScene(Scene):
    def __init__(self):
        super().__init__(
            description="You emerge into a small clearing. Sunlight bathes the area in a warm glow. A lone bandit stands in the center, blocking your path.",
            exits={"south": "forest"},
            actions={
                "look": lambda p: print("You see a bandit guarding the southern path."),
                "enemy": Bandit(),  # Enemy object defined in actions
            },
        )


class Bandit(Enemy):
    def __init__(self):
        super().__init__("Bandit", 50, 15)


class ForestScene(Scene):
    def __init__(self):
        super().__init__(
            description="You stand in a dense forest. Sunlight struggles to penetrate the thick canopy of leaves above. The air is filled with the chirping of birds and the rustling of unseen creatures. You see a glinting object on the ground.",
            exits={"north": "clearing"},
            actions={
                "look": lambda p: print(p.description),  # Use player description method
                "take sword": self.take_sword,  # New action to take the sword
                "enemy": Goblin(),  # Enemy object defined in actions
            },
        )

    def take_sword(self, player):
        # Check if player doesn't have a weapon equipped
        if not player.sword:
            print("You pick up the sword.")
            player.equip_sword()  # Call player's equip_sword method
        else:
            print("You are already wielding a weapon.")

    def enter(self):
        print(self.description)
        # Update description to remove sword message after it's picked up
        if self.actions.get("take sword"):  # Check if "take sword" action exists
            self.description = self.description.replace(
                ". You see a glinting object on the ground.", ""
            )
        super().enter()  # Call the parent class enter method


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 30, 10)


class Game:
    def __init__(self):
        super().__init__()
        self.current_scene = ForestScene()

    def run(self):
        player = Player()

        while True:
            self.current_scene.enter()

            exits = self.current_scene.get_exits()
            options = [f"Go {exit}" for exit in exits]
            options.append("Attack")
            print("\n".join(options))

            while True:
                try:
                    choice = int(input("Enter your choice: ")) - 1
                    if 0 <= choice < len(options):
                        break
                    else:
                        print(
                            "Invalid choice. Please enter a number between 1 and",
                            len(options),
                        )
                except ValueError:
                    print("Invalid input. Please enter a number.")

            action = options[choice].lower().split()[0]
            self.current_scene = self.current_scene.do_action(action, player)

            if player.health <= 0:
                break

        print("Game Over!")


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
