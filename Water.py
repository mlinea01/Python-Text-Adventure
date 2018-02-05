from Battle import *

class Water:

    def getName(self):
        return "Water"

    def useSpell(self):

        Attack = Battle()

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
            print("You chose Tidal Wave.  Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            Attack.mainAttack()

        if water_spell == 2:
            print("You chose Whirl Pool. Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            Attack.secondaryAttack()

        if water_spell == 3:
            print("You chose Mist. let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            Attack.secondaryAttack()