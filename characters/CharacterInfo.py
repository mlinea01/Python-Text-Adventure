# This module is used to keep track of information common to all characters (including players and enemies)

import random


# This is the base class for all characters
class Character:

    def __init__(self, name, desc, hp, mana, speed, attacks):
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.attacks = attacks
        self.name = name
        self.desc = desc
        self.weapons = []
        self.status_effects = []
        self.cannot_attack = 0

    # default behavior is to choose an attack randomly
    #   (this can be overridden in subclasses for more specific behavior)
    def choose_attack(self):
        return self.attacks[random.randint(0, len(self.attacks)-1)]

    # used to add a status effect
    def add_status_effect(self, effect):
        if random.randint(0, 100) <= effect.chance:
            print(self.name + " is " + effect.name)
            self.status_effects.append(effect)

    # called when hit by an attack
    def hit_by(self, attack):
        # subtract hp and check for defeat
        self.hp -= attack.damage
        if self.hp < 0:
            self.hp = 0
        print(self.name + " takes " + str(attack.damage) + " damage!" + "  HP: " + str(self.hp))
        if self.hp == 0:
            print(self.name + " has been defeated!")
        else:
            # if not defeated, apply status effect(s) - one or more can be applied
            try:
                for effect in attack.statusEffects:
                    self.add_status_effect(effect)
            except TypeError:
                self.add_status_effect(attack.statusEffects)
