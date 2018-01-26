leaveGame = 0
xp = 0
startHealth = 25
enemyHealth = 25
damage = 10
enemyDamage = 10

while leaveGame != "q":

    character = int(input("Choose a character type. (1.Fire, 2.Water, 3. Earth, 4. Wind)"))

    if character == 1:
        print("You chose a fire character.")
        change = int(input("Are you sure you want Fire? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello",name)

        else:
            continue

        print("You will need an ability to protect yourself.(Choose One)")
        print("1. Fire twister (Surrounds your enemy in a tornado of fire, dealing heavy damage.)")
        print("2. Scorch (Sets your enamy ablaze, dealing medium damage, and stunning them.)")
        print("3. Fire breathe (Shoots a breathe of fire at your enamy, blinding them and dealing medium damage.)")
        fireSpell = int(input("Choose a starting spell:"))

        if fireSpell == 1:
            print("You chose Fire Twister.  Let's practice using it.")
            print("Attack the training dummy to practice using your new ability.")
            attack = input("Press enter to attack")

    elif character == 2:
        print("You chose a water character.")
        change = int(input("Are you sure you want Water? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello",name)

        else:
            continue

    elif character == 3:
        print("You chose an Earth character.")
        change = int(input("Are you sure you want Earth? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello", name)

        else:
            continue

    else:
        print("You chose a Wind character.")
        change = int(input("Are you sure you want Wind? (1.yes, 2.no)"))

        if change == 1:
            name = input("Create a name for your character.")
            print("Hello", name)

        else:
            continue

