from Adventure1 import *
from Fire import *
from Water import *
from Earth import *
from Wind import *
from Battle import *


class Game:
    leaveGame = 0
    stepOne = Adventure1()

    spells = [Fire(), Water(), Earth(), Wind()]
    practiceBattle = Battle()

    while leaveGame != "q":
        character = int(input("Choose a character type. (1.Fire, 2.Water, 3. Earth, 4. Wind)"))
        print("")
        if character < 1 or character > 4: continue
        playerSpell = spells[character-1]

        print("You chose a " + playerSpell.getName() + " character.")
        change = int(input("Are you sure you want " + playerSpell.getName() + "? (1.yes, 2.no)"))
        if change == 2: continue

        playerSpell.chooseSpell()
        print("You chose " + playerSpell.spellName + ". Let's practice using it.")
        print("Attack the training dummy to practice using your new ability.")
        practiceBattle.mainAttack(playerSpell)
        stepOne.step1()