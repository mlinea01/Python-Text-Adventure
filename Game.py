from adventures.Adventure1 import *
from Battle import *
from characters.Enemies import *
from attacks.Spells import *
from attacks.Weapons import *
from characters.CharacterRace import *
from characters.Player import Player
import time
import threading
from Multiplayer import IO
from functools import partial
from adventures.Adventures import Adventure


class Game:
    players = []

    def __init__(self):

        IO.print_text("Game has started!")

        p_num = 0
        while p_num < IO.get_num_players():
            intro_thread = threading.Thread(target=self.adventure_intro, args=[p_num])
            intro_thread.start()
            p_num += 1
            Game.players.append(None)

        players_ready = False
        while not players_ready:
            time.sleep(0.1)
            players_ready = True
            for player in Game.players:
                if player is None:
                    players_ready = False

        IO.print_text("Well done in your training everyone!")
        p_num = 0
        for player in Game.players:
            time.sleep(0.5)
            IO.print_text(player.name + " the " + player.desc + " " + player.character_type + " " + player.race +
                              " has joined the party!")
            p_num += 1

        time.sleep(1)
        Adventure(Game.players)

        stepOne = Adventure1(Game.players)
        stepOne.step1()

    def adventure_intro(self, player_num):

        from Multiplayer import IO

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
            IO.print_text("Choose a character type.\n", [player_num])
            typeNum = 1
            for charType in characterTypes:
                IO.print_text(str(typeNum) + ". " + charType, [player_num])
                typeNum += 1

            characterType = int(IO.get_input(player_num, "\nYour choice: ",
                                             partial(IO.check_num_in_range,minimum=1, maximum=len(characterTypes))))
            IO.print_text("", [player_num])

            # confirm character type choice
            IO.print_text("You chose a " + characterTypes[characterType - 1] + " character.", [player_num])
            change = int(IO.get_input(player_num,
                                      "Are you sure you want " + characterTypes[characterType - 1] + "? (1.yes, 2.no)",
                                      partial(IO.check_num_in_range, minimum=1, maximum=2)))
            if change == 2:
                continue

            # Prompt player to choose a Race for his/her character
            IO.print_text("Choose a Race for your character.\n", [player_num])
            raceNum = 1
            for raceType in characterRaces:
                IO.print_text(str(raceNum) + ". " + raceType.name, [player_num])
                raceNum += 1

            characterRace = int(IO.get_input(player_num, "\nYour choice: ",
                                             partial(IO.check_num_in_range,minimum=1, maximum=len(characterRaces))))
            char = characterRaces[characterRace - 1]
            IO.print_text("", [player_num])
            IO.print_text("You chose " + char.name, [player_num])
            IO.print_text(char.desc, [player_num])

            # prompt the player for a character name
            name = IO.get_input(player_num, "\nCreate a name for your character: ", partial(IO.check_not_null))
            player = Player(name, char, player_num, characterTypes[characterType - 1])
            player.desc = IO.get_input(player_num, "Describe your character in one word: ",
                                       partial(IO.check_not_null)).split(' ', 1)[0]
            IO.print_text("Hello " + player.name + " the " + player.desc + " " + characterTypes[characterType - 1]
                              + " " + player.race, [player_num])

            # prompt the player to choose a starting weapon
            player_weapon = None
            while True:
                IO.print_text("\nBefore you go out on your adventure, grab a weapon! (Choose One)\n", [player_num])
                weaponNum = 1
                for weapon in weapons:
                    IO.print_text(str(weaponNum) + ". " + weapon.name, [player_num])
                    weaponNum += 1
                player_weapon = weapons[int(IO.get_input(player_num, "\nYour choice: ",
                                                         partial(IO.check_num_in_range, minimum=1,
                                                                 maximum=len(weapons)))) - 1]
                IO.print_text("", [player_num])
                IO.print_text("The " + player_weapon.name + " - " + player_weapon.desc, [player_num])
                if int(IO.get_input(player_num, "Is this the weapon you want? (1.yes 2.no)",
                                    partial(IO.check_num_in_range, minimum=1, maximum=2))) != 1:
                    continue
                else:
                    player.equip_weapon(player_weapon, False)
                    break

            # prompt the player to choose a starting spell
            while True:
                IO.print_text("\nYou will also need an ability to protect yourself.(Choose One)\n", [player_num])
                spellNum = 1
                for spell in startingSpells[characterType - 1]:
                    IO.print_text(str(spellNum) + ". " + spell.name, [player_num])
                    spellNum += 1
                chosenSpell = startingSpells[characterType - 1][
                    int(IO.get_input(player_num, "\nYour choice: ",
                                     partial(IO.check_num_in_range,minimum=1, maximum=len(startingSpells)))) - 1]
                IO.print_text(chosenSpell.name + " - " + chosenSpell.desc, [player_num])
                if int(IO.get_input(player_num, "Is this the spell you want? (1.yes 2.no)",
                                    partial(IO.check_num_in_range, minimum=1, maximum=2))) != 1:
                    continue
                else:
                    player.learn_attack(chosenSpell)
                    break

            # practice battle
            IO.print_text("\nYou'll need to learn how to fight out there. Let's see what ya got!", [player_num])
            IO.print_text("Attack this training dummy to practice.\n", [player_num])

            leaveGame = "q"
            Battle([player], TrainingDummy())

            Game.players[player_num] = player
            IO.print_text("Waiting for other players to finish their training...", [player_num])
