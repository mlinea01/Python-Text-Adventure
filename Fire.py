from attacks.Spells import *


class Fire:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Fire"

    def chooseSpell(self):

        chooseSpell = [fire_twister(), Scorch(), fire_breathe()]

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        for Spell in chooseSpell:
            print(Spell.name + "\n" + Spell.desc)

        fire_spell = int(input("Choose a starting spell:"))
        return chooseSpell[fire_spell - 1]
