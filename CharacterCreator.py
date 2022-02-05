from adventures.Forest.ForestAdventure import *
from Battle import *
from characters.Enemies import *
from attacks.Spells import *
from equipment.Weapons import *
from characters.CharacterRace import *
from characters.Player import Player

class CharacterCreator:
    @staticmethod
    def make_character():
        character_type = CharacterCreator.get_character_type()
        character_race = CharacterCreator.get_character_race()
        print("")
        print("You chose " + character_race.name)
        print(character_race.desc)
        character_name = CharacterCreator.get_character_name()
        player = Player(character_name, character_race, 0, character_type)
        player.desc = input("Describe your character in one word: ").split(' ', 1)[0]
        print("Hello " + player.name + " the " + player.desc + " " + character_type + " " + player.race)
        player.equip_weapon(CharacterCreator.get_character_weapon(), False)
        player.learn_attack(CharacterCreator.get_starting_spell(character_type))
        return player

    @staticmethod
    def get_character_type():
        characterTypes = ["Fire", "Water", "Earth", "Wind"]
        selected_type = None
        while selected_type is None:
            print("Choose a character type.\n")
            typeNum = 1
            for charType in characterTypes:
                print(str(typeNum) + ". " + charType)
                typeNum += 1

            character_type_idx = int(input("\nYour choice: "))
            selected_type = characterTypes[character_type_idx - 1]
            print("")

            # confirm character type choice
            print("You chose a " + selected_type + " character.")
            confirmed = int(input("Are you sure you want " + selected_type + "? (1.yes, 2.no)")) == 1
            if not confirmed:
                selected_type = None
        return selected_type

    @staticmethod
    def get_character_race():
        # Prompt player to choose a Race for his/her character
        characterRaces = [Gnome(), Ogre(), Elf(), Human()]
        print("Choose a Race for your character.\n")
        raceNum = 1
        for raceType in characterRaces:
            print(str(raceNum) + ". " + raceType.name)
            raceNum += 1

        characterRace = int(input("\nYour choice: "))
        return characterRaces[characterRace - 1]


    @staticmethod
    def get_character_name():
        # prompt the player for a character name
        return input("\nCreate a name for your character: ")
        
    @staticmethod
    def get_character_weapon():
        # prompt the player to choose a starting weapon
        weapons = [Sword(), WarHammer(), Staff(), BattleAxe(), Trident(), BowAndArrow()]
        selected_weapon = None
        while selected_weapon is None:
            print("\nBefore you go out on your adventure, grab a weapon! (Choose One)\n")
            weaponNum = 1
            for weapon in weapons:
                print(str(weaponNum) + ". " + weapon.name)
                weaponNum += 1
            selected_weapon = weapons[int(input("\nYour choice: ")) - 1]
            print("")
            print("The " + selected_weapon.name + " - " + selected_weapon.desc)
            if int(input("Is this the weapon you want? (1.yes 2.no)")) != 1:
                selected_weapon = None
        return selected_weapon

    @staticmethod
    def get_starting_spell(character_type):
        # prompt the player to choose a starting spell
         # starting spells: fire, water, earth, wind
        startingSpells = {
            "Fire" : [fire_twister(), Scorch(), fire_breathe()],
            "Water" : [whirl_pool(), Mist(), calming_waters()],
            "Earth" : [Earthquake(), rock_slide(), rock_throw()],
            "Wind" : [Tornado(), poison_breeze(), healing_breeze()]
        }
        chosen_spell = None
        while chosen_spell is None:
            print("\nYou will also need an ability to protect yourself.(Choose One)\n")
            spellNum = 1
            for spell in startingSpells[character_type]:
                print(str(spellNum) + ". " + spell.name)
                spellNum += 1
            chosen_spell = startingSpells[character_type][int(input("\nYour choice: ")) - 1]
            print(chosen_spell.name + " - " + chosen_spell.desc)
            if int(input("Is this the spell you want? (1.yes 2.no)")) != 1:
                chosen_spell = None
        return chosen_spell