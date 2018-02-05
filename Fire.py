class Fire:

    def __init__(self):
        self.damage = 1
        self.spellName = ""

    def getName(self):
        return "Fire"

    def chooseSpell(self):

        name = input("Create a name for your character.")
        print("Hello", name)
        print("")
        print("You will need an ability to protect yourself.(Choose One)")
        print("1. Fire twister (Surrounds your enemy in a tornado of fire, dealing heavy damage.)")
        print("2. Scorch (Sets your enamy ablaze, dealing medium damage, and stunning them.)")
        print("3. Fire breathe (Shoots a breathe of fire at your enamy, blinding them and dealing medium damage.)")
        print("")
        fire_spell = int(input("Choose a starting spell:"))
        print("")

        if fire_spell == 1:
            print("You chose Fire Twister.  Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            self.damage = 10
            self.spellName = "Fire Twister"

        elif fire_spell == 2:
            print("You chose Scorch. Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            self.damage = 7
            self.spellName = "Scorch"

        elif fire_spell == 3:
            print("You chose Fire Breathe. let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            self.damage = 7
            self.spellName = "Fire Breathe"
