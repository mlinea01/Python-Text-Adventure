from characters.CharacterInfo import Character
from attacks import BasicAttacks
from attacks import Weapons


class TrainingDummy(Character):
    def __init__(self):
        super().__init__("Training Dummy", "", hp=10, mana=0, speed=5, attacks=[BasicAttacks.BlankStare()], weapons=[])


class MountainDragon(Character):
    def __init__(self):
        super().__init__("Mountain Dragon", "", hp=15, mana=10, speed=5, attacks=[BasicAttacks.Punch()], weapons=[])
