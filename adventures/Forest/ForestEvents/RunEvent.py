import threading
import random
from Multiplayer import IO
from time import sleep
from attacks.AttacksInfo import Attack
from attacks.AttacksInfo import AttackTypes

class RunEvent:

    def __init__(self, player):
        print("Do you hear something? It sounds like a very large animal is coming our way!")
        self.enemies = ["Teradactyl", "Velociraptor"]
        self.teradactyl = Attack("Devour", "grabs you in its talons and rips you to shreds", damage=1000,
                                 atkType=AttackTypes.Normal, manaCost=0, statusEffects=[]),
        self.velociraptor = Attack("Devour", "Eats you alive", damage=1000, atkType=AttackTypes.Normal, manaCost=0,
                                   statusEffects=[])
        self.enemy_attacks = [self.teradactyl, self.velociraptor]
        self.hiding_place = ["Tree", "cave"]
        self.obstacles = ["fallen tree", "hole", "fence"]
        self.player = player

    def start_event(self):
        for player in self.players:
            threading.Thread(target = self.player_action, args=[player]).start()

    def player_action(self, player):
        while True:
            if self.enemies == "Teradactyl":
                print("OMG a Teradactyl is flying right toward us! Run and take cover! QUICK!")
                sleep(0.5)
                print("Watch out for obstacles! Get someplace safe!")
                self.player = player

    def player_obstacle(self, player):
        obstacle = random.randint(0,2)

        jump = input(player.name, "Theres a " + self.obstacles[obstacle]
                            + " Type 'jump' to avoid the trap!!!", time_out=50)

        if jump != "jump":
            enemy = random.randint(0,1)
            print(self.enemies[enemy] + self.enemy_attacks[enemy].desc)