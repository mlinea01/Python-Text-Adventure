# This module is used to keep track of information common to all characters (including players and enemies)


# This is the base class for all characters
class Character:
    # hp: hit points, speed : determines turn order in battle, attacks : list of attacks the character knows
    def __init__(self, hp, mana, speed, attacks):
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.attacks = attacks

    def learnAttack(self, attack):
        self.attacks.append(attack)