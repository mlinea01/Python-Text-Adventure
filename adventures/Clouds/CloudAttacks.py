from attacks.AttacksInfo import *
from attacks.StatusEffects import *

class CloudAttacks:
    class MushroomCloud(Attack):
        def __init__(self):
            name = "Mushroom Cloud"
            desc = "Engulfs enemy in a huge suffocating cloud!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Wind,
                             statusEffects=[Blind(blindDuration=1, chance=60)], manaCost=0)

    class WhirlWind(Attack):
        def __init__(self):
            name = "Whirl Wind"
            desc = "Creates a very strong gusty wind!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Wind,
                             statusEffects=[Paralyze(paralyzeDuration=1, chance=60)], manaCost=0)

    class StormCloud(Attack):
        name = "Storm Cloud"
        desc = "Creates a storm cloud that strikes enemy down with powerful lightening"
        super().__init__(name, desc, damage=2, atkType=AttackTypes.Wind,
                         statusEffects=[], manaCost=0)