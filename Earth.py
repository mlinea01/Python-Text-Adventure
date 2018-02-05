class Earth:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Earth"

    def chooseSpell(self):

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        print("You will need an ability to protect yourself.(Choose One)")
        print("1. Earthquake (Shakes the earth below your enemy, dealing heavy damage.)")
        print("2. Rock Throw (Hurls a boulder at your enemy, stunning them and dealing medium damage.)")
        print("3. Rock Slide (Causes rocks to fall onto your enemy, blinding them and dealing medium damage.)")
        print("")
        earth_spell = int(input("Choose a starting spell:"))
        print("")

        if earth_spell == 1:
            print("You chose Earthquake.  Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            self.damage = 10
            self.spellName = "Earthquake"

        if earth_spell == 2:
            print("You chose Rock Throw. Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            self.damage = 7
            self.spellName = "Rock Throw"

        if earth_spell == 3:
            print("You chose Rock Slide. let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            self.damage = 7
            self.spellName = "Rock Slide"
