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

    def learnAttack(self, attack):
        self.attacks.append(attack)

    # default behavior is to choose an attack randomly
    #   (this can be overridden in subclasses for more specific behavior)
    def chooseAttack(self):
        return self.attacks[random.randint(0, len(self.attacks)-1)]

    def equip_weapon(self, weapon):
        self.weapons.append(weapon)
        self.learnAttack(weapon.attack)
