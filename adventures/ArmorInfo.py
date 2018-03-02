from characters.Player import *

# Base class for all types of armor.


class Armor:

    def __init__(self, name, armor, magResist):
        self.name = name
        self.armor = armor
        self.magResist = magResist

    def equip_armor(self, armor):
        from Multiplayer import GameSession
        server = GameSession.get_server()
        server.print_text(Player.name + "equipped" + armor.name)
