from Adventure1 import *
from Battle import *
from characters.Player import Player
from attacks.Spells import *
from attacks.Weapons import *
from characters.CharacterRace import *


class Game:
    leaveGame = 0
    stepOne = Adventure1()

    # starting spells: fire, water, earth, wind
    startingSpells = [[fire_twister(), Scorch(), fire_breathe()],
                      [tidal_wave(), whirl_pool(), Mist()],
                      [Earthquake(), rock_slide(), rock_throw()],
                      [Hurricane(), Tornado(), poison_breeze()]]
    characterTypes = ["Fire", "Water", "Earth", "Wind"]

    characterRaces = [Gnome(), Ogre(), Elf()]

    weapons = [Sword(), war_hammer(), Staff()]

    practiceBattle = Battle()

    while leaveGame != "q":

        # prompt player to choose a starting character type which will determine starting spell choices
        print("Choose a character type.\n")
        typeNum = 1
        for charType in characterTypes:
            print(str(typeNum)+". "+charType)
            typeNum += 1

        characterType = int(input("\nYour choice: "))
        print("")
        if characterType < 1 or characterType > 4:
            continue

        # confirm character type choice
        print("You chose a " + characterTypes[characterType-1] + " character.")
        change = int(input("Are you sure you want " + characterTypes[characterType-1] + "? (1.yes, 2.no)"))
        if change == 2:
            continue

        # Prompt player to choose a Race for his/her character
        print("Choose a Race for your character.\n")
        raceNum = 1
        for raceType in characterRaces:
            print(str(raceNum)+". "+raceType.name)
            raceNum+=1

        characterRace = int(input("\nYour choice: "))
        print("")
        print("You chose " + characterRaces[characterRace-1].name)
        print(characterRaces[characterRace-1].desc)

        # prompt the player for a character name
        name = input("\nCreate a name for your character: ")
        print("Hello", name, "the almighty " + characterTypes[characterType-1]+" "+characterRaces[characterRace-1].name)

        # prompt the player to choose a starting weapon
        print("\nBefore you go out on your adventure, grab a weapon! (Choose One)\n")
        weaponNum = 1
        for weapon in weapons:
            print(str(weaponNum) + ". " + weapon.name)
            weaponNum += 1
        weapon = int(input("\nYour choice: "))
        print("")
        print("You chose a " + weapons[weapon - 1].name)

        # prompt the player to choose a starting spell
        print("\nYou will also need an ability to protect yourself.(Choose One)\n")
        spellNum = 1
        for spell in startingSpells[characterType-1]:
            print(str(spellNum)+". "+spell.name)
            spellNum += 1
        chosenSpell = startingSpells[characterType-1][int(input("\nYour choice: "))-1]

        # practice battle
        print("\nYou chose " + chosenSpell.name + ". Let's practice using it.")
        print("Attack the training dummy to practice using your new ability.")
        practiceBattle.mainAttack(chosenSpell)

        stepOne.step1()
