from characters.CharacterInfo import *
from attacks import BasicAttacks

class MountainDragon(Character):
    def __init__(self):
        super().__init__("Mountain Dragon", "", hp=15, mana=10, speed=15, attacks=[BasicAttacks.Punch()], weapons=[],
                         resistance=[AttackTypes.Fire], reward_xp=50)


class TerrifyingTurantula(Character):
    def __init__(self):
        super().__init__("Terrifying Turantula", "", hp=20, mana=15, speed=20, attacks=[BasicAttacks.Bite()],
                         weapons=[], reward_xp=65)


class ZombieRat(Character):
    def __init__(self):
        super().__init__("Zombie Rat", "", hp=20, mana=15, speed=20, attacks=[BasicAttacks.Bite()], weapons=[],
                         reward_xp=65)


class GiantSquid(Character):
    def __init__(self):
        super().__init__("Giant Squid", "", hp=25, mana=20, speed=25, attacks=[BasicAttacks.Bind()], weapons=[],
                         resistance=[AttackTypes.Water], reward_xp=70)