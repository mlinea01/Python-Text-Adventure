from characters.CharacterInfo import *
from attacks import BasicAttacks
from adventures.Forest.ForestAttacks import ForestAttacks


class TerrifyingTurantula(Character):
    def __init__(self):
        super().__init__("Terrifying Turantula", "", hp=20, mana=15, speed=25,
                         attacks=[ForestAttacks.StickyWeb(), ForestAttacks.StrongVenom()],
                         weapons=[], reward_xp=65, character_type= AttackTypes.Poison)


class ZombieRat(Character):
    def __init__(self):
        super().__init__("Zombie Rat", "", hp=20, mana=15, speed=20,
                         attacks=[BasicAttacks.Bite()], weapons=[],
                         reward_xp=65, character_type=AttackTypes.Normal)


class VenusFlyTrap(Character):
    def __init__(self):
        super().__init__("Venus Fly Trap", "", hp=15, mana=15, speed=20,
                         attacks=[ForestAttacks.SweetScent(), ForestAttacks.Devour(), ForestAttacks.VineWhip()],
                         weapons=[],
                         reward_xp=65, character_type= AttackTypes.Plant)


class SlappingTree(Character):
    def __init__(self):
        super().__init__("Slapping Tree", "", hp=20, mana=15, speed=25,
                         attacks=[ForestAttacks.Slap(), ForestAttacks.VineWhip()],
                         weapons=[],
                         reward_xp=65, character_type=AttackTypes.Plant)


class DeathBeetle(Character):
    def __init__(self):
        super().__init__("Death Beetle", "", hp=7, mana=15, speed=20,
                         attacks=[ForestAttacks.WeakVenom()], weapons=[],
                         reward_xp=65, character_type= AttackTypes.Poison)


class WidowWasp(Character):
    def __init__(self):
        super().__init__("Widow Wasp", "", hp=7, mana=15, speed=20,
                         attacks=[ForestAttacks.Sting()], weapons=[],
                         reward_xp=65, character_type= AttackTypes.Poison)