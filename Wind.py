from attacks.Spells import *


class Wind:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Wind"

    def chooseSpell(self):

        chooseSpell = [Hurricane(), Tornado(), poison_breeze()]

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        for Spell in chooseSpell:
            print(Spell.name + "\n" + Spell.desc)

        wind_spell = int(input("Choose a starting spell:"))
        return chooseSpell[wind_spell - 1]
