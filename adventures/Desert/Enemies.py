from characters.CharacterInfo import *
from adventures.Desert.DesertAttacks import DesertAttacks

class AntagonisticArmadillo(Character):
    def __init__(self):
        super().__init__("Antagonistic Armadillo", "", hp=25, mana=20, speed=25, attacks=[DesertAttacks.SandStorm],
                         weapons=[], reward_xp=75, character_type=AttackTypes.Earth)

class ChaoticCactus(Character):
    def __init__(self):
        super().__init__("Chaotic Cactus", "", hp=25, mana=20, speed=25, attacks=[DesertAttacks.CactusNeedle],
                         weapons=[], reward_xp=75, character_type=AttackTypes.Earth)

class TantalizingTremor(Character):
    def __init__(self):
        super().__init__("Tantalizing Tremor", "", hp=25, mana=20, speed=25, attacks=[DesertAttacks.DuneTomb],
                         weapons=[], reward_xp=75, character_type=AttackTypes.Earth)