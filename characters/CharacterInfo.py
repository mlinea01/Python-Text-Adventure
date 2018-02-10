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
        self.character = self

    def learn_attack(self, attack, show_message=True):
        if show_message:
            print(self.name + " learned " + attack.name + "!")
        self.attacks.append(attack)

    # default behavior is to choose an attack randomly
    #   (this can be overridden in subclasses for more specific behavior)
    def choose_attack(self):
        return self.attacks[random.randint(0, len(self.attacks)-1)]

    def equip_weapon(self, weapon, show_message=True):
        if show_message:
            print(self.name + " equipped " + weapon.name + "!")
        self.weapons.append(weapon)
        self.learn_attack(weapon.attack, False)

    def hit_by(self, attack):
        self.hp -= attack.damage
        if self.hp < 0:
            self.hp = 0
        print(self.name + " takes " + str(attack.damage) + " damage!" + "  HP: " + str(self.hp))
        if self.hp == 0:
            print(self.name + " has been defeated!")