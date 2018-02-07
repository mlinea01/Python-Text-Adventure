from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class Sword(Attack):
    def __init__(self):
        desc = "Long steel sword with razor sharp edges that can cut through anything!"
        super().__init__("Long Sword", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Bleed,
                         target=TargetTypes.Enemy_Single, manaCost=0)


class war_hammer(Attack):
    def __init__(self):
        desc = "Huge hammer with metal head that cannot be shattered, and a steel handle to swing the hammer so hard" \
               "it can break a mountain into a million pieces!"
        super().__init__("War Hammer", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=[],
                         target=TargetTypes.Enemy_Single, manaCost=0)


class Staff(Attack):
    def __init__(self):
        desc = "A long staff specifically used in martial arts made from magical wood that possesses incredible " \
               "power. It looks like nothing but make no mistake, you will feel the affects of this staff from around" \
               "the world!"
        super().__init__("Staff", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=[],
                         target=TargetTypes.Enemy_Single, manaCost=0)
