class Water:

    def water_spell(this):
        tidal_wave = 10
        whirl_pool = 7
        mist = 7

        health = 25
        enemy_health = 25

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
            attack = input("Press enter to attack")
            print("")
            enemy_health -= tidal_wave
            print("It was a direct hit!")
            print(name, ":", health, "Dummy:", enemy_health)
            print("")

        if water_spell == 2:
            print("You chose Whirl Pool. Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            attack = input("Press enter to attack")
            print("")
            enemy_health -= whirl_pool
            print("It was a direct hit!")
            print(name, ":", health, "Dummy:", enemy_health)
            print("")

        if water_spell == 3:
            print("You chose Mist. let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            attack = input("Press enter to attack")
            print("")
            enemy_health -= mist
            print("It was a direct hit!")
            print(name, ":", health, "Dummy:", enemy_health)
            print("")