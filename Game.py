from adventures.Forest.ForestAdventure import *
from Battle import *
from characters.Enemies import *
from attacks.Spells import *
from equipment.Weapons import *
from characters.CharacterRace import *
from characters.Player import Player
import time
import threading
from Multiplayer import IO,Server
from functools import partial

class Game:
    players = []
    player_backup = []

    def __init__(self):

        levels = [Adventure1]
        self.adventure_intro()
        
        print("Well done in your training!")
        time.sleep(1)

        game_restart = True
        level_num = 0
        # start of new game

        # if there is a backup version of players, restore from backup
        if len(Game.player_backup) > 0:
            player_num = 0
            while player_num < len(Game.players):
                Game.players[player_num].character = Game.player_backup[player_num]
                player_num += 1

        # play each level
        while level_num < len(levels):
            Game.player_backup = []
            for player in Game.players:
                if player is not None:
                    Game.player_backup.append(deepcopy(player.character))
            levels[level_num](Game.players)

            # check if all players are dead after each level
            sumHp = 0
            for player in Game.players:
                sumHp += player.hp
            if sumHp == 0:
                break

            level_num = level_num + 1


    def adventure_intro(self):
        
        leaveGame = 0

        # starting spells: fire, water, earth, wind
        startingSpells = [[fire_twister(), Scorch(), fire_breathe()],
                          [whirl_pool(), Mist(), calming_waters()],
                          [Earthquake(), rock_slide(), rock_throw()],
                          [Tornado(), poison_breeze(), healing_breeze()]]
        characterTypes = ["Fire", "Water", "Earth", "Wind"]

        characterRaces = [Gnome(), Ogre(), Elf(), Human()]

        weapons = [Sword(), WarHammer(), Staff(), BattleAxe(), Trident(), BowAndArrow()]

        while leaveGame != "q":

            # prompt player to choose a starting character type which will determine starting spell choices
            print("Choose a character type.\n")
            typeNum = 1
            for charType in characterTypes:
                print(str(typeNum) + ". " + charType)
                typeNum += 1

            characterType = int(input("\nYour choice: "))
            print("")

            # confirm character type choice
            print("You chose a " + characterTypes[characterType - 1] + " character.")
            change = int(input("Are you sure you want " + characterTypes[characterType - 1] + "? (1.yes, 2.no)"))

            if change == 2:
                continue

            # Prompt player to choose a Race for his/her character
            print("Choose a Race for your character.\n")
            raceNum = 1
            for raceType in characterRaces:
                print(str(raceNum) + ". " + raceType.name)
                raceNum += 1

            characterRace = int(input("\nYour choice: "))
            char = characterRaces[characterRace - 1]
            print("")
            print("You chose " + char.name)
            print(char.desc)

            # prompt the player for a character name
            name = input("\nCreate a name for your character: ")
            player = Player(name, char, 0, characterTypes[characterType - 1])
            player.desc = input("Describe your character in one word: ").split(' ', 1)[0]
            print("Hello " + player.name + " the " + player.desc + " " + characterTypes[characterType - 1]
                              + " " + player.race)

            # prompt the player to choose a starting weapon
            player_weapon = None
            while True:
                print("\nBefore you go out on your adventure, grab a weapon! (Choose One)\n")
                weaponNum = 1
                for weapon in weapons:
                    print(str(weaponNum) + ". " + weapon.name)
                    weaponNum += 1
                player_weapon = weapons[int(input("\nYour choice: ")) - 1]
                print("")
                print("The " + player_weapon.name + " - " + player_weapon.desc)
                if int(input("Is this the weapon you want? (1.yes 2.no)")) != 1:
                    continue
                else:
                    player.equip_weapon(player_weapon, False)
                    break

            # prompt the player to choose a starting spell
            while True:
                print("\nYou will also need an ability to protect yourself.(Choose One)\n")
                spellNum = 1
                for spell in startingSpells[characterType - 1]:
                    print(str(spellNum) + ". " + spell.name)
                    spellNum += 1
                chosenSpell = startingSpells[characterType - 1][
                    int(input("\nYour choice: ")) - 1]
                print(chosenSpell.name + " - " + chosenSpell.desc)
                if int(input("Is this the spell you want? (1.yes 2.no)")) != 1:
                    continue
                else:
                    player.learn_attack(chosenSpell)
                    break

            # practice battle
            print("\nYou'll need to learn how to fight out there. Let's see what ya got!")
            print("Attack this training dummy to practice.\n")

            leaveGame = "q"
            Battle().start([player], TrainingDummy())

            print("Waiting for other players to finish their training...")
