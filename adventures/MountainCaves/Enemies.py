from characters.CharacterInfo import *
from adventures.MountainCaves.MountainAttacks import MountainAttacks

class MountainDragon(Character):
    def __init__(self):
        super().__init__("Mountain Dragon", "", hp=15, mana=10, speed=15, attacks=[MountainAttacks.MudSlide()],
                         weapons=[], reward_xp=50, character_type= AttackTypes.Fire)

class Golem(Character):
    def __init__(self):
        super().__init__("Golem", "", hp=20, mana=15, speed=20, attacks=[MountainAttacks.BoulderDash()],
                         weapons=[], reward_xp=50, character_type=AttackTypes.Earth)

class MaliciousMountainLion(Character):
    def __init__(self):
        super().__init__("Malicious Mountain Lion", "", hp=20, mana=15, speed=20, attacks=[MountainAttacks.Fissure],
                         weapons=[], reward_xp=50, character_type=AttackTypes.Earth)