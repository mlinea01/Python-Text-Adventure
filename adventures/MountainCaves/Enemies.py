from characters.CharacterInfo import *
from attacks import BasicAttacks

class MountainDragon(Character):
    def __init__(self):
        super().__init__("Mountain Dragon", "", hp=15, mana=10, speed=15, attacks=[BasicAttacks.Punch()], weapons=[]
                         , reward_xp=50, character_type= AttackTypes.Fire)