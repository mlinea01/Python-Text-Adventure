class Water:

    def __init__(self):
        self.damage = 1
        self.spellName = "spell"

    def getName(self):
        return "Water"

    def chooseSpell(self):

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        print("You will need an ability to protect yourself.(Choose One)")
        print("1. Tidal Wave (Hurls a huge wave toward your enemy, dealing heavy damage.)")
        print("2. Whirl Pool (Surrounds your enemy in a tornado of Water, stunning them and dealing medium damage.)")
        print("3. Mist (Shoots a cloud of mist at the target, blinding them and dealing medium damage.)")
        print("")
        water_spell = int(input("Choose a starting spell:"))
        print("")

        if water_spell == 1:
            self.damage = 10
            self.spellName = "Tidal Wave"


        if water_spell == 2:
            self.damage = 7
            self.spellName = "Whirl Pool"

        if water_spell == 3:
            self.damage = 7
            self.spellName = "Mist"
