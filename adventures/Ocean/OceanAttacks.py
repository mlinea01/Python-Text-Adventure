from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class OceanAttacks:
    class Chomp(Attack):
        def __init__(self):
            name = "Chomp"
            desc = "Rips enemy to shreds!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Water,
                             statusEffects=[Bleed(bleedDuration=1, chance=60)], manaCost=0)

    class TidalWave(Attack):
        def __init__(self):
            name = "Tidal Wave"
            desc = "Creates a huge wave, squashing the enemy into fish food!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Water, statusEffects=[], manaCost=0)

    class RipCurrent(Attack):
        def __init__(self):
            name = "Rip Current"
            desc = "Pulls enemy under water!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Water,
                             statusEffects=[Paralyze(paralyzeDuration=1, chance=60)], manaCost=0)
