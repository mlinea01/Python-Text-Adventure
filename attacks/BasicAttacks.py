# This is used to define basic attacks available to players and enemies
from attacks.AttacksInfo import AttackTypes, TargetTypes, Attack
from attacks.StatusEffects import *


# Offensive
class Punch(Attack):
    def __init__(self):
        name = "Punch"
        desc = "An attack where you throw Hawaiian Punch at - wait, what? It's just a punch? Fine..."
        super().__init__(name, desc, damage=1, atkType=AttackTypes.Normal, statusEffects=[],
                         target=TargetTypes.Enemy_Single, manaCost=0)


class BlankStare(Attack):
    def __init__(self):
        name = "Blank Stare"
        desc = "Just an awkward blank stare at your opponent"
        super().__init__(name, desc, damage=0, atkType=AttackTypes.Normal, statusEffects=[],
                         target=TargetTypes.Enemy_Single, manaCost=0)


# Defensive
class Block(Attack):
    def __init__(self):
        name = "Block"
        desc = "Attempt to block the next incoming attack to reduce its damage and effects."
        super().__init__(name, desc, damage=0, atkType=AttackTypes.Normal, statusEffects=[Shield(5)],
                         target=TargetTypes.Self, manaCost=0)
