from characters.Player import *
# Base class for all types of armor.


class Armor:

    def __init__(self, name, armor, magResist):
        self.name = name
        self.armor = armor
        self.magResist = magResist

    def equip_armor(self, armor):
        print("You equipped" + armor.name)
