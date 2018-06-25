from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class MountainAttacks:
    class Fissure(Attack):
        def __init__(self):
            name = "Fissure"
            desc = "Shakes the ground creating a large crack beneath the enemy"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Earth,
                             statusEffects=[Stun(stunDuration=1, chance=60)], manaCost=0)

    class MudSlide(Attack):
        def __init__(self):
            name = "Mud Slide"
            desc = "Causes a mud slide that bury's the enemy alive"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Earth,
                             statusEffects=[Paralyze(paralyzeDuration=1, chance=60)], manaCost=0)

    class BoulderDash(Attack):
        def __init__(self):
            name = "Boulder Dash"
            desc = "A boulder crushes enemies in it's path!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Earth, statusEffects=[], manaCost=0)