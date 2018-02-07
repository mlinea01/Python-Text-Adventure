from attacks.Spells import *


class Water:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Water"

    def chooseSpell(self):

        chooseSpell = [tidal_wave(), whirl_pool(), Mist()]

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        for Spell in chooseSpell:
            print(Spell.name + "\n" + Spell.desc)

        water_spell = int(input("Choose a starting spell:"))
        return chooseSpell[water_spell - 1]
