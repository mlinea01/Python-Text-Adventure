from characters.CharacterInfo import *
from adventures.Clouds.CloudAttacks import CloudAttacks

class UnluckyLeprechaun(Character):
    def __init__(self):
        super().__init__("Unlucky Leprechaun", "", hp=25, mana=20, speed=25, attacks=[CloudAttacks.MushroomCloud],
                         weapons=[], reward_xp=75, character_type=AttackTypes.Wind)

class HideousHippogryph(Character):
    def __init__(self):
        super().__init__("Hideous Hippogryph", "", hp=25, mana=20, speed=25, attacks=[CloudAttacks.WhirlWind],
                         weapons=[], reward_xp=75, character_type=AttackTypes.Wind)

class CrazyCockatrice(Character):
    def __init__(self):
        super().__init__("Crazy Cockatrice", "", hp=25, mana=20, speed=25, attacks=[CloudAttacks.StormCloud],
                         weapons=[], reward_xp=75, character_type=AttackTypes.Wind)