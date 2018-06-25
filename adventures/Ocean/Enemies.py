from characters.CharacterInfo import *
from attacks import BasicAttacks
from adventures.Ocean.OceanAttacks import OceanAttacks

class GiantSquid(Character):
    def __init__(self):
        super().__init__("Giant Squid", "", hp=25, mana=20, speed=25, attacks=[BasicAttacks.Bind()], weapons=[]
                         , reward_xp=70, character_type= AttackTypes.Water)

class MegalodonShark(Character):
    def __init__(self):
        super().__init__("Megalodon Shark", "", hp=25, mana=20, speed=25, attacks=[OceanAttacks.RipCurrent],
                         weapons=[], reward_xp=70, character_type=AttackTypes.Water)

class PetrifyingPiranha(Character):
    def __init__(self):
        super().__init__("Petrifying Piranha", "", hp=25, mana=20, speed=25, attacks=[OceanAttacks.Chomp],
                         weapons=[], reward_xp=70, character_type=AttackTypes.Water)