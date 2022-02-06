from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class ForestAttacks:
    class StickyWeb(Attack):
        def __init__(self):
            name = "Sticky Web"
            desc = "Shoots sticky web."
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Normal, statusEffects=[Paralyze(
                paralyzeDuration=1, chance=60)], manaCost=0)

    class SweetScent(Attack):
        def __init__(self):
            name = "Sweet Scent"
            desc = "Lures the enemy in."
            super().__init__(name, desc, damage=None, atkType=AttackTypes.Plant, statusEffects=charmed(2, 100), manaCost=0)


    class Devour(Attack):
        def __init__(self):
            name = "Devour"
            desc = "Devours enemy whole!"
            super().__init__(name, desc, damage=7, atkType=AttackTypes.Normal, statusEffects=[antiCharmed()], manaCost=0)


    class Slap(Attack):
        def __init__(self):
            name = "Slap"
            desc = "A mighty slap!"
            super().__init__(name, desc, damage=3, atkType=AttackTypes.Normal, statusEffects=[], manaCost=0)

    class VineWhip(Attack):
        def __init__(self):
            name = "Vine Whip"
            desc = "So whip it, whip it good!"
            super().__init__(name, desc, damage=4, atkType=AttackTypes.Plant, statusEffects=[], manaCost=0)

    class WeakVenom(Attack):
        def __init__(self):
            name = "Weak Venom"
            desc = "Meh not too bad, not too good either."
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Poison,
                             statusEffects=[Poison(poison_duration=2, damage=1, chance=60)],
                             manaCost=0)

    class StrongVenom(Attack):
        def __init__(self):
            name = "Strong Venom"
            desc = "Vicious venom is injected into the enemy."
            super().__init__(name, desc, damage=3, atkType=AttackTypes.Poison,
                             statusEffects=[Poison(poison_duration=2, damage=2, chance=70)],
                             manaCost=0)

    class Sting(Attack):
        def __init__(self):
            name = "Sting"
            desc = "Ouch, that's gotta... hurt a bunch!"
            super().__init__(name, desc, damage=2, atkType=AttackTypes.Poison,
                             statusEffects=[Poison(poison_duration=2, damage=1, chance=75)],
                             manaCost=0)