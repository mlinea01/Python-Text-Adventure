class Earth:

    def getName(self):
        return "Earth"

    def useSpell(self):
        earthquake = 10
        rock_throw = 7
        rock_slide = 7

        health = 25
        enemy_health = 25

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
            input("Press enter to attack")
            print("")
            enemy_health -= earthquake
            print("It was a direct hit!")
            print(name, ":", health, "Dummy:", enemy_health)
            print("")

        if earth_spell == 2:
            print("You chose Rock Throw. Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            print("")
            enemy_health -= rock_throw
            print("It was a direct hit!")
            print(name, ":", health, "Dummy:", enemy_health)
            print("")

        if earth_spell == 3:
            print("You chose Rock Slide. let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            input("Press enter to attack")
            print("")
            enemy_health -= rock_slide
            print("It was a direct hit!")
            print(name, ":", health, "Dummy:", enemy_health)
            print("")