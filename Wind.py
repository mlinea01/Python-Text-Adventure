class Wind:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Wind"

    def chooseSpell(self):

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        print("You will need an ability to protect yourself.(Choose One)")
        print("1. Hurricane (150 mile per around wind tosses your opponent, dealing heavy damage.)")
        print("2. Tornado (Surrounds your opponent in a whirling wind, stunning them and dealing medium damage.)")
        print("3. Poison Breeze (Blows a poison wind at your enemy, blinding them and dealing medium damage.)")
        print("")
        wind_spell = int(input("Choose a starting spell:"))
        print("")

        if wind_spell == 1:
            self.damage = 10
            self.spellName = "Hurricane"

        if wind_spell == 2:
            self.damage = 7
            self.spellName = "Tornado"

        if wind_spell == 3:
            self.damage = 7
            self.spellName = "Poison Breeze"
