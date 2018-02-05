from Adventure1 import *
from Fire import *
from Water import *
from Earth import *
from Wind import *


class Game:
    leaveGame = 0

    while leaveGame != "q":

        stepOne = Adventure1()
        earthSpell = Earth()
        fireSpell = Fire()
        waterSpell = Water()
        windSpell = Wind()

        character = int(input("Choose a character type. (1.Fire, 2.Water, 3. Earth, 4. Wind)"))
        print("")

        if character == 1:
            print("You chose a fire character.")
            change = int(input("Are you sure you want Fire? (1.yes, 2.no)"))

            if change == 1:
                fireSpell.fire_spell()
                stepOne.step1()

            else:
                continue

        elif character == 2:
            print("You chose a water character.")
            change = int(input("Are you sure you want Water? (1.yes, 2.no)"))

            if change == 1:
                waterSpell.water_spell()
                stepOne.step1()

            else:
                continue

        elif character == 3:
            print("You chose an Earth character.")
            change = int(input("Are you sure you want Earth? (1.yes, 2.no)"))

            if change == 1:
                earthSpell.earth_spell()
                stepOne.step1()

            else:
                continue

        else:
            print("You chose a Wind character.")
            change = int(input("Are you sure you want Wind? (1.yes, 2.no)"))

            if change == 1:
                windSpell.wind_spell()
                stepOne.step1()

            else:
                continue
