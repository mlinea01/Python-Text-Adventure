from attacks.Spells import *


class Earth:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Earth"

    def chooseSpell(self):

        chooseSpell = [Earthquake(), rock_throw(), rock_slide()]

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        for Spell in chooseSpell:
            print(Spell.name + "\n" + Spell.desc)

        earth_spell = int(input("Choose a starting spell:"))
        return chooseSpell[earth_spell - 1]
