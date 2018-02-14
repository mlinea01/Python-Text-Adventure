from characters.CharacterInfo import Character
from attacks import BasicAttacks
from attacks import Weapons


class TrainingDummy(Character):
    def __init__(self):
        super().__init__("Training Dummy", "", hp=10, mana=0, speed=0, attacks=[BasicAttacks.BlankStare()], weapons=[])
