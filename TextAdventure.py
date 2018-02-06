from Adventure1 import *
from Fire import *
from Water import *
from Earth import *
from Wind import *
from Battle import *
from characters.Player import Player


class Game:
    leaveGame = 0
    player = Player()
    stepOne = Adventure1()

    playerTypes = [Fire(), Water(), Earth(), Wind()]
    practiceBattle = Battle()

    while leaveGame != "q":
        character = int(input("Choose a character type. (1.Fire, 2.Water, 3. Earth, 4. Wind)"))
        print("")
        if character < 1 or character > 4: continue
        playerType = playerTypes[character - 1]

        print("You chose a " + playerType.getName() + " character.")
        change = int(input("Are you sure you want " + playerType.getName() + "? (1.yes, 2.no)"))
        if change == 2: continue

        playerType.chooseSpell()
        print("You chose " + playerType.spellName + ". Let's practice using it.")
        print("Attack the training dummy to practice using your new ability.")
        practiceBattle.mainAttack(playerType)
        stepOne.step1()