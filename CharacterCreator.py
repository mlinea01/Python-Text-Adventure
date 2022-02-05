from Utility import confirm_yes_or_no, get_player_choice
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
        character_types = ["Fire", "Water", "Earth", "Wind"]
        prompt = "Choose a character type.\n"
        confirm_func = lambda choice: confirm_yes_or_no("Are you sure you want " + choice + "?")
        return get_player_choice(character_types, prompt, confirm_func)

    @staticmethod
    def get_character_race():
        # Prompt player to choose a Race for his/her character
        character_races = [Gnome(), Ogre(), Elf(), Human()]
        prompt = "Choose a Race for your character.\n"
        confirm_func = lambda choice: confirm_yes_or_no("Are you sure you want " + str(choice) + "?")
        return get_player_choice(character_races, prompt, confirm_func)

    @staticmethod
    def get_character_name():
        # prompt the player for a character name
        return input("\nCreate a name for your character: ")
        
    @staticmethod
    def get_character_weapon():
        # prompt the player to choose a starting weapon
        weapons = [Sword(), WarHammer(), Staff(), BattleAxe(), Trident(), BowAndArrow()]
        prompt = "Before you go out on your adventure, grab a weapon! (Choose One)\n"
        confirm_func = lambda choice: confirm_yes_or_no("The " + choice.name + " - " + choice.desc + "\nIs this the weapon you want?")
        return get_player_choice(weapons, prompt, confirm_func)

    @staticmethod
    def get_starting_spell(character_type):
        # prompt the player to choose a starting spell
         # starting spells: fire, water, earth, wind
        spells_per_type = {
            "Fire" : [fire_twister(), Scorch(), fire_breathe()],
            "Water" : [whirl_pool(), Mist(), calming_waters()],
            "Earth" : [Earthquake(), rock_slide(), rock_throw()],
            "Wind" : [Tornado(), poison_breeze(), healing_breeze()]
        }
        starting_spells = spells_per_type[character_type]
        prompt = "You will also need an ability to protect yourself.(Choose One)\n"
        confirm_func = lambda choice: confirm_yes_or_no(choice.name + " - " + choice.desc + "\nIs this the spell you want?")
        return get_player_choice(starting_spells, prompt, confirm_func)