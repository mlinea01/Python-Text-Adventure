from adventures.Adventure1 import *
from Battle import *
from characters.Enemies import *
from attacks.Spells import *
from attacks.Weapons import *
from characters.CharacterRace import *
from characters.Player import Player
import time
import threading


class Game:
    players = []

    def __init__(self):

        from Multiplayer import GameSession
        server = GameSession.get_server()
        server.print_text("Game has started!")

        p_num = 0
        while p_num < server.get_num_players():
            intro_thread = threading.Thread(target=self.adventure_intro, args=(p_num, server))
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

        server.print_text("Well done in your training everyone!")
        p_num = 0
        for player in Game.players:
            time.sleep(0.5)
            server.print_text(player.name + " the " + player.desc + " has joined the party!")
            p_num += 1

        time.sleep(1)
        stepOne = Adventure1(Game.players)
        stepOne.step1()

    def adventure_intro(self, player_num, server):

        from Multiplayer import IO

        leaveGame = 0

        # starting spells: fire, water, earth, wind
        startingSpells = [[fire_twister(), Scorch(), fire_breathe()],
                          [tidal_wave(), whirl_pool(), Mist()],
                          [Earthquake(), rock_slide(), rock_throw()],
                          [Hurricane(), Tornado(), poison_breeze()]]
        characterTypes = ["Fire", "Water", "Earth", "Wind"]

        characterRaces = [Gnome(), Ogre(), Elf()]

        weapons = [Sword(), WarHammer(), Staff(), BattleAxe(), Trident(), BowAndArrow()]

        while leaveGame != "q":

            # prompt player to choose a starting character type which will determine starting spell choices
            server.print_text("Choose a character type.\n", [player_num])
            typeNum = 1
            for charType in characterTypes:
                server.print_text(str(typeNum) + ". " + charType, [player_num])
                typeNum += 1

            characterType = int(IO.get_input(server, player_num, "\nYour choice: "))
            server.print_text("", [player_num])
            if characterType < 1 or characterType > 4:
                continue

            # confirm character type choice
            server.print_text("You chose a " + characterTypes[characterType - 1] + " character.", [player_num])
            change = int(IO.get_input(server, player_num,
                                      "Are you sure you want " + characterTypes[characterType - 1] + "? (1.yes, 2.no)"))
            if change == 2:
                continue

            # Prompt player to choose a Race for his/her character
            server.print_text("Choose a Race for your character.\n", [player_num])
            raceNum = 1
            for raceType in characterRaces:
                server.print_text(str(raceNum) + ". " + raceType.name, [player_num])
                raceNum += 1

            characterRace = int(IO.get_input(server, player_num, "\nYour choice: "))
            char = characterRaces[characterRace - 1]
            server.print_text("", [player_num])
            server.print_text("You chose " + char.name, [player_num])
            server.print_text(char.desc, [player_num])

            # prompt the player for a character name
            name = IO.get_input(server, player_num, "\nCreate a name for your character: ")
            player = Player(name, char, player_num)
            player.desc = IO.get_input(server, player_num, "Describe your character in one word: ").split(' ', 1)[0]
            server.print_text(
                "Hello " + player.name + " the " + player.desc + " " + characterTypes[characterType - 1] + " " + player.race,
                [player_num])

            # prompt the player to choose a starting weapon
            player_weapon = None
            while True:
                server.print_text("\nBefore you go out on your adventure, grab a weapon! (Choose One)\n", [player_num])
                weaponNum = 1
                for weapon in weapons:
                    server.print_text(str(weaponNum) + ". " + weapon.name, [player_num])
                    weaponNum += 1
                player_weapon = weapons[int(IO.get_input(server, player_num, "\nYour choice: ")) - 1]
                server.print_text("", [player_num])
                server.print_text("The " + player_weapon.name + " - " + player_weapon.desc, [player_num])
                if int(IO.get_input(server, player_num, "Is this the weapon you want? (1.yes 2.no)")) != 1:
                    continue
                else:
                    player.equip_weapon(player_weapon, False)
                    break

            # prompt the player to choose a starting spell
            while True:
                server.print_text("\nYou will also need an ability to protect yourself.(Choose One)\n", [player_num])
                spellNum = 1
                for spell in startingSpells[characterType - 1]:
                    server.print_text(str(spellNum) + ". " + spell.name, [player_num])
                    spellNum += 1
                chosenSpell = startingSpells[characterType - 1][
                    int(IO.get_input(server, player_num, "\nYour choice: ")) - 1]
                server.print_text(chosenSpell.name + " - " + chosenSpell.desc, [player_num])
                if int(IO.get_input(server, player_num, "Is this the spell you want? (1.yes 2.no)")) != 1:
                    continue
                else:
                    player.learn_attack(chosenSpell)
                    break

            # practice battle
            server.print_text("\nYou'll need to learn how to fight out there. Let's see what ya got!", [player_num])
            server.print_text("Attack this training dummy to practice.\n", [player_num])

            leaveGame = "q"
            Battle([player], TrainingDummy())

            Game.players[player_num] = player
            server.print_text("Waiting for other players to finish their training...", [player_num])
