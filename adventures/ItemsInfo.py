# Base class for items that can be used in the game.
class Items:

    def __init__(self, name, healthRestore, manaRestore, spdIncrease, dmgIncrease):
        self.name = name
        self.healthRestore = healthRestore
        self.manaRestore = manaRestore
        self.spdIncrease = spdIncrease
        self.dmgIncrease = dmgIncrease

    def use_health_potion(self, health):
        print("You used 1 " + self.name)
        health += 10

    def use_mana_potion(self, mana):
        print("You used 1 " + self.name)
        mana += 10

    def use_speed_potion(self, speed):
        print("You used 1 " + self.name)
        speed += 10

    def use_damage_increase(self, damage):
        print("You used 1 " + self.name)
        damage += 10
