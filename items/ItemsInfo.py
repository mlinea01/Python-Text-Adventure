# Base class for items that can be used in the game.
class Items:

    def __init__(self, name, desc, itemAttack):
        self.name = name
        self.desc = desc
        self.itemAttack = itemAttack