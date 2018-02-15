# Base class for items that can be used in the game.
class Items:

    def __init__(self, name, healthRestore, manaRestore, spdIncrease, dmgIncrease):
        self.name = name
        self.healthRestore = healthRestore
        self.manaRestore = manaRestore
        self.spdIncrease = spdIncrease
        self.dmgIncrease = dmgIncrease
