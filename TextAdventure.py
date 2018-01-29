import Adventure1
import Multiplayer
Multiplayer.MultiplayerConnection()

leaveGame = 0
xp = 0
startHealth = 25
enemyHealth = 25

fireTwister = 10
scorch = 7
fireBreath = 7

tidalWave = 10
whirlPool = 7
mist = 7

Earthquake = 10
rockThrow = 7
rockSlide = 7

Hurricane = 10
Tornado = 7
poisonBreeze = 7

enemyDamage = 5

while leaveGame != "q":

    character = int(input("Choose a character type. (1.Fire, 2.Water, 3. Earth, 4. Wind)"))

    if character == 1:
        print("You chose a fire character.")
        change = int(input("Are you sure you want Fire? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello",name)
            print("")
            print("You will need an ability to protect yourself.(Choose One)")
            print("1. Fire twister (Surrounds your enemy in a tornado of fire, dealing heavy damage.)")
            print("2. Scorch (Sets your enamy ablaze, dealing medium damage, and stunning them.)")
            print("3. Fire breathe (Shoots a breathe of fire at your enamy, blinding them and dealing medium damage.)")
            print("")
            fireSpell = int(input("Choose a starting spell:"))
            print("")

            if fireSpell == 1:
                print("You chose Fire Twister.  Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= fireTwister
                print("It was a direct hit!")
                print(name,":",startHealth, "Dummy:",enemyHealth)
                print("")
                Adventure1.step1
        
            if fireSpell == 2:
                print("You chose Scorch. Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= scorch
                print("It was a direct hit!")
                print(name,":",startHealth, "Dummy:",enemyHealth)
                print("")
                Adventure1.step1

            if fireSpell == 3:
                print("You chose Fire Breathe. let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= fireBreath
                print("It was a direct hit!")
                print(name,":",startHealth,"Dummy:",enemyHealth)
                print("")
                Adventure1.step1

        else:
            continue

    elif character == 2:
        print("You chose a water character.")
        change = int(input("Are you sure you want Water? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello",name)
            print("")
            print("You will need an ability to protect yourself.(Choose One)")
            print("1. Tidal Wave (Hurls a huge wave toward your enemy, dealing heavy damage.)")
            print("2. Whirl Pool (Surrounds your enemy in a tornado of Water, stunning them and dealing medium damage.)")
            print("3. Mist (Shoots a cloud of mist at the target, blinding them and dealing medium damage.)")
            print("")
            waterSpell = int(input("Choose a starting spell:"))
            print("")

            if waterSpell == 1:
                print("You chose Tidal Wave.  Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= tidalWave
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

            if waterSpell == 2:
                print("You chose Whirl Pool. Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= whirlPool
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

            if waterSpell == 3:
                print("You chose Mist. let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= mist
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

        else:
            continue

    elif character == 3:
        print("You chose an Earth character.")
        change = int(input("Are you sure you want Earth? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello", name)
            print("")
            print("You will need an ability to protect yourself.(Choose One)")
            print("1. Earthquake (Shakes the earth below your enemy, dealing heavy damage.)")
            print("2. Rock Throw (Hurls a boulder at your enemy, stunning them and dealing medium damage.)")
            print("3. Rock Slide (Causes rocks to fall onto your enemy, blinding them and dealing medium damage.)")
            print("")
            earthSpell = int(input("Choose a starting spell:"))
            print("")

            if earthSpell == 1:
                print("You chose Earthquake.  Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= Earthquake
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

            if earthSpell == 2:
                print("You chose Rock Throw. Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= rockThrow
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

            if earthSpell == 3:
                print("You chose Rock Slide. let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= rockSlide
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1


        else:
            continue

    else:
        print("You chose a Wind character.")
        change = int(input("Are you sure you want Wind? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello", name)
            print("")
            print("You will need an ability to protect yourself.(Choose One)")
            print("1. Hurricane (150 mile per around wind tosses your opponent, dealing heavy damage.)")
            print("2. Tornado (Surrounds your opponent in a whirling wind, stunning them and dealing medium damage.)")
            print("3. Poison Breeze (Blows a poisoness wind at your enemy, blinding them and dealing medium damage.)")
            print("")
            windSpell = int(input("Choose a starting spell:"))
            print("")

            if windSpell == 1:
                print("You chose Hurricane.  Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= Hurricane
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

            if windSpell == 2:
                print("You chose Tornado. Let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= Tornado
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

            if windSpell == 3:
                print("You chose Poison Breeze. let's practice using it.")
                print("Attack the training dummy to practice using your new ability.")
                attack = input("Press enter to attack")
                print("")
                enemyHealth -= poisonBreeze
                print("It was a direct hit!")
                print(name, ":", startHealth, "Dummy:", enemyHealth)
                print("")
                Adventure1.step1

        else:
            continue

