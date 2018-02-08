from characters.Player import *
from attacks import BasicAttacks


class Gnome(CharacterInfo.Character):
    def __init__(self):
        super().__init__("Gnome", hp=10, mana=10, speed=15, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()])


class Ogre(CharacterInfo.Character):
    def __init__(self):
        super().__init__("Ogre", hp=20, mana=10, speed=5, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()])


class Elf(CharacterInfo.Character):
    def __init__(self):
        super().__init__("Elf", hp=10, mana=20, speed=5, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()])
