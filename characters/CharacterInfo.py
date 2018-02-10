# This module is used to keep track of information common to all characters (including players and enemies)

import random


# This is the base class for all characters
class Character:
    # hp: hit points, speed : determines turn order in battle, attacks : list of attacks the character knows
    def __init__(self, name, desc, hp, mana, speed, attacks):
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.attacks = attacks
        self.name = name
        self.desc = desc
        self.weapons = []

    # default behavior is to choose an attack randomly
    #   (this can be overridden in subclasses for more specific behavior)
    def choose_attack(self):
        return self.attacks[random.randint(0, len(self.attacks)-1)]

    def hit_by(self, attack):
        self.hp -= attack.damage
        if self.hp < 0:
            self.hp = 0
        print(self.name + " takes " + str(attack.damage) + " damage!" + "  HP: " + str(self.hp))
        if self.hp == 0:
            print(self.name + " has been defeated!")