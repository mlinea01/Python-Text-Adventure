from Battle import *

class Wind:

    def getName(self):
        return "Wind"

    def useSpell(self):

        Attack = Battle()

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
            print("You chose Hurricane.  Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            Attack.mainAttack()

        if wind_spell == 2:
            print("You chose Tornado. Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            Attack.secondaryAttack()

        if wind_spell == 3:
            print("You chose Poison Breeze. let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            Attack.secondaryAttack()