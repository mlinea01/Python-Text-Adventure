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
                         reward_xp=65, character_type=AttackTypes.Poison)


class EnemyGen:
    # enemy list is defined as a list of tuples each of which define an enemy and its difficulty.
    # this list should be in ascending order
    enemy_list = [(DeathBeetle, 1), (WidowWasp, 1), (SlappingTree, 2), (VenusFlyTrap, 2), (ZombieRat, 2),
                  (TerrifyingTurantula, 3)]

    @classmethod
    def get_enemy_difficulty(cls, enemy):
        for e in cls.enemy_list:
            if e[0] == enemy:
                return e[1]
        return 2

    @classmethod
    def get_random_enemies(cls, difficulty, enemy_list=None):
        enemies = []
        if enemy_list is None:
            enemy_list = [DeathBeetle, WidowWasp, SlappingTree, VenusFlyTrap, ZombieRat, TerrifyingTurantula]
        while difficulty > 0:
            max_enemy_num = 0
            d = 1
            for enemy in enemy_list:
                d = cls.get_enemy_difficulty(enemy)
                if d > difficulty:
                    break
                max_enemy_num += 1

            enemy_to_add = enemy_list[random.randint(0, max_enemy_num-1)]
            difficulty -= d
            enemies.append(enemy_to_add())
        return enemies
