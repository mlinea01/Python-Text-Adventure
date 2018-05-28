from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class Earthquake(Attack):
    def __init__(self):
        desc = "Shakes the earth below your enemy, dealing heavy damage."
        super().__init__("Earthquake", desc, damage=10, atkType=AttackTypes.Earth, statusEffects=[],
                         manaCost=2, multi_target=True)

class rock_throw(Attack):
    def __init__(self):
        desc = "Hurls a boulder at your enemy, stunning them and dealing medium damage."
        super().__init__("Rock Throw", desc, damage=7, atkType=AttackTypes.Earth, statusEffects=Stun(1), manaCost=1)


class rock_slide(Attack):
    def __init__(self):
        desc = "Causes rocks to fall onto your enemy, blinding them and dealing medium damage."
        super().__init__("Rock Slide", desc, damage=7, atkType=AttackTypes.Earth, statusEffects=Blind(1), manaCost=1)


class fire_twister(Attack):
    def __init__(self):
        desc = "Surrounds your enemy in a tornado of fire, dealing heavy damage."
        super().__init__("Fire Twister", desc, damage=10, atkType=AttackTypes.Fire, statusEffects=[],
                         manaCost=2, multi_target=True)


class Scorch(Attack):
    def __init__(self):
        desc = "Sets your enamy ablaze, dealing medium damage, and stunning them."
        super().__init__("Scorch", desc, damage=7, atkType=AttackTypes.Fire, statusEffects=Stun(1), manaCost=1)


class fire_breathe(Attack):
    def __init__(self):
        desc = "Shoots a breathe of fire at your enamy, blinding them and dealing medium damage."
        super().__init__("Fire Breathe", desc, damage=7, atkType=AttackTypes.Fire, statusEffects=Blind(1), manaCost=1)


class tidal_wave(Attack):
    def __init__(self):
        desc = "Hurls a huge wave toward your enemy, dealing heavy damage."
        super().__init__("Tidal Wave", desc, damage=10, atkType=AttackTypes.Water, statusEffects=[],
                         manaCost=2, multi_target=True)


class whirl_pool(Attack):
    def __init__(self):
        desc = "Surrounds your enemy in a tornado of Water, stunning them and dealing medium damage."
        super().__init__("Whirl Pool", desc, damage=7, atkType=AttackTypes.Water, statusEffects=Stun(1), manaCost=1)


class Mist(Attack):
    def __init__(self):
        desc = "Shoots a cloud of mist at the target, blinding them and dealing medium damage."
        super().__init__("Mist", desc, damage=7, atkType=AttackTypes.Water, statusEffects=Blind(1), manaCost=1)


class calming_waters(Attack):
    def __init__(self):
        desc = "Heals a target ally"
        super().__init__("Calming Waters", desc, damage=-7, atkType=AttackTypes.Water, statusEffects=[], manaCost=2,
                         is_dodgeable=False)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_allies(attacker, targets)


class Hurricane(Attack):
    def __init__(self):
        desc = "150 mile per around wind tosses your opponent, dealing heavy damage."
        super().__init__("Hurricane", desc, damage=10, atkType=AttackTypes.Wind, statusEffects=[], manaCost=1)


class Tornado(Attack):
    def __init__(self):
        desc = "Surrounds your opponent in a whirling wind, stunning them and dealing medium damage."
        super().__init__("Tornado", desc, damage=7, atkType=AttackTypes.Wind, statusEffects=Stun(1),
                         manaCost=1, multi_target=True)


class poison_breeze(Attack):
    def __init__(self):
        desc = "Blows a poison wind at your enemy, blinding them and dealing medium damage."
        super().__init__("Poison Breeze", desc, damage=7, atkType=AttackTypes.Wind, statusEffects=Blind(1), manaCost=1)


class healing_breeze(Attack):
    def __init__(self):
        desc = "Heals a target ally"
        super().__init__("Healing Wind", desc, damage=-7, atkType=AttackTypes.Wind, statusEffects=[], manaCost=2,
                         is_dodgeable=False)

    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_allies(attacker, targets)
