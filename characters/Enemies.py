from characters.CharacterInfo import Character
from attacks import BasicAttacks
from attacks.AttacksInfo import AttackTypes


class TrainingDummy(Character):
    def __init__(self):
        super().__init__("Training Dummy", "", hp=10, mana=0, speed=5, attacks=[BasicAttacks.BlankStare()], weapons=[],
                         reward_xp=10, character_type= AttackTypes.Normal)