from characters.CharacterInfo import *
from attacks import BasicAttacks

class GiantSquid(Character):
    def __init__(self):
        super().__init__("Giant Squid", "", hp=25, mana=20, speed=25, attacks=[BasicAttacks.Bind()], weapons=[]
                         , reward_xp=70, character_type= AttackTypes.Water)