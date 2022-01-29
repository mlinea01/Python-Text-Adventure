import threading
import random
from Multiplayer import IO
from time import sleep
from attacks.AttacksInfo import Attack
from attacks.AttacksInfo import AttackTypes

class RunEvent:

    def __init__(self, players):
        IO.print_text("Do you hear something? It sounds like a very large animal is coming our way!")
        self.enemies = ["Teradactyl", "Velociraptor"]
        self.teradactyl = Attack("Devour", "grabs you in its talons and rips you to shreds", damage=1000,
                                 atkType=AttackTypes.Normal, manaCost=0, statusEffects=[]),
        self.velociraptor = Attack("Devour", "Eats you alive", damage=1000, atkType=AttackTypes.Normal, manaCost=0,
                                   statusEffects=[])
        self.enemy_attacks = [self.teradactyl, self.velociraptor]
        self.hiding_place = ["Tree", "cave"]
        self.obstacles = ["fallen tree", "hole", "fence"]
        self.players = players

    def start_event(self):
        for player in self.players:
            threading.Thread(target = self.player_action, args=[player]).start()

    def player_action(self, player):
        while True:
            if self.enemies == "Teradactyl":
                IO.print_text("OMG a Teradactyl is flying right toward us! Run and take cover! QUICK!")
                sleep(0.5)
                IO.print_text("Watch out for obstacles! Get someplace safe!")

    def player_obstacle(self, player):
        obstacle = random.randint(0,2)

        jump = IO.get_input(player.player_num, "Theres a " + self.obstacles[obstacle]
                            + " Type 'jump' to avoid the trap!!!", time_out=50)

        if jump != "jump":
            enemy = random.randint(0,1)
            print(self.enemies[enemy] + self.enemy_attacks[enemy].desc)