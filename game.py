import random  
 
print("ADVENTURE TEXT GAME")
ans = "Y"
 
class Skill:
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description
 
    def use(self, user, target):
        print(f"{user.name} uses {self.name}! {self.description}")
        target.take_damage(self.damage)
 
class Player:
    def __init__(self, name, role, health):
        self.name = name
        self.role = role
        self.health = health
        self.isAlive = True
        self.skills = []
 
    def choose_skill(self):
        print("\nChoose a skill to use:")
        for i, skill in enumerate(self.skills, start=1):
            print(f"[{i}] {skill.name} - {skill.description}")
        choice = int(input("Enter the number of the skill: "))
        if 1 <= choice <= len(self.skills):
            return self.skills[choice - 1]
        else:
            print("Invalid choice. Using first skill by default.")
            return self.skills[0]
 
    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} has {self.health} health remaining.")
        else:
            print(f"{self.name} has been defeated!")
            self.isAlive = False
 
class Knight(Player):
    def __init__(self, name):
        super().__init__(name, "Knight", health=100)
        self.skills = [
            Skill("Slash", 20, "A mighty sword attack!"),
            Skill("Shield Bash", 20, "Bashes the enemy with a shield to stun.")
        ]
 
class BowMaster(Player):
    def __init__(self, name):
        super().__init__(name, "Bow Master", health=100)
        self.skills = [
            Skill("Arrow Shot", 20, "Shoots a precise arrow!"),
            Skill("Poison Arrow", 20, "Fires a toxic arrow that saps health.")
        ]
 
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.isAlive = True
 
    def attack(self, player):
        print(f"{self.name} attacks {player.name}!")
        player.take_damage(self.attack_power)
 
    def take_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            print(f"{self.name} has {self.health} health remaining.")
        else:
            print(f"{self.name} has been defeated!")
            self.isAlive = False
 
print("[1]Knight [2]Bow Master")
char = int(input("Please choose your character [1]Knight [2]Bow Master: "))
 
if char == 1:
    player = Knight(input("Enter your Knight's name: "))
    print(f"You picked Knight, {player.name}")
elif char == 2:
    player = BowMaster(input("Enter your Bow Master's name: "))
    print(f"You picked Bow Master, {player.name}")
else:
    print("INVALID CHARACTER")
    exit()
 
lvl = int(input("Please choose level of difficulty [1]Easy [2]Medium [3]Hard: "))
 
if lvl == 1:
    enemy_health = 40
    print("You selected Easy level.")
elif lvl == 2:
    enemy_health = 60
    print("You selected Medium level.")
elif lvl == 3:
    enemy_health = 80
    print("You selected Hard level.")
else:
    print("INVALID LEVEL OF DIFFICULTY")
    exit()
 
enemies = ["Wild Boar", "Goblin", "Wyvern", "Golem"]
 
while ans.upper() == "YES" or ans.upper() == "Y":
    enemy_name = random.choice(enemies)
    enemy = Enemy(enemy_name, enemy_health, 10)
    print(f"\nA wild {enemy.name} appears with {enemy.health} health!\n")
 
    while player.isAlive and enemy.isAlive:
        skill = player.choose_skill()
        skill.use(player, enemy)
        if enemy.isAlive:
            enemy.attack(player)
 
    if not player.isAlive:
        print("\nGame Over!")
        break
    ans = input("Do you want to fight again? (Y/N): ").strip().upper()
 
print("\nThank you for playing!")
