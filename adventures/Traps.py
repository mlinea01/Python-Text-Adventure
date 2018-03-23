from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class Hole(Attack):
    def __init__(self):
        desc = "You fell into a huge hole! It may be tough to get out. "
        super().__init__("Hole", desc, damage=1, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)


class Net(Attack):
    def __init__(self):
        desc = "A net fell from above you and trapped you underneath!"
        super().__init__("Net", desc, damage=1, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)


class BarbedWire(Attack):
    def __init__(self):
        desc = "You just ran into Barbed wire and cut yourself! We need to find another way around."
        super().__init__("Barbed Wire", desc, damage=1, atkType=AttackTypes.Normal,
                         statusEffects=Bleed(bleedDuration=1, chance= 30), manaCost=0)


class BearTrap(Attack):
    def __init__(self):
        desc = "Your leg is caught in a bear trap! Get out quick before you bleed to death!"
        super().__init__("Bear Trap", desc, damage=1, atkType=AttackTypes.Normal,
                         statusEffects=Bleed(bleedDuration=1, chance=30), manaCost=0)