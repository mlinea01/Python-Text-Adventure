from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class DesertAttacks:
    class SandStorm(Attack):
        def __init__(self):
            name = "Sand Storm"
            desc = "Surrounds the enemy with sand"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Earth,
                             statusEffects=[Blind(blindDuration=1, chance=60)], manaCost=0)

    class DuneTomb(Attack):
        def __init__(self):
            name = "Dune Tomb"
            desc = "Burys enemy alive in a dune tomb"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Earth,
                             statusEffects=[Stun(stunDuration=1, chance=60)], manaCost=0)

    class CactusNeedle(Attack):
        def __init__(self):
            name = "Cactus Needle"
            desc = "impales enemy with the needles of a cactus"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Earth, statusEffects=[], manaCost=0)