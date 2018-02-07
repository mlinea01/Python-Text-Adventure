from attacks.AttacksInfo import *
from attacks.StatusEffects import *


class Earthquake(Attack):
    desc = "Shakes the earth below your enemy, dealing heavy damage."
    super().__init__("Earthquake", desc, damage=10, atkType=AttackTypes.Earth, statusEffects=[],
                     target=TargetTypes.Enemy_All, manaCost=1)


class rock_throw(Attack):
    desc = "Hurls a boulder at your enemy, stunning them and dealing medium damage."
    super().__init__("Rock Throw", desc, damage=7, atkType=AttackTypes.Earth, statusEffects=Stun,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class rock_slide(Attack):
    desc = "Causes rocks to fall onto your enemy, blinding them and dealing medium damage."
    super().__init__("Rock Slide", desc, damage=7, atkType=AttackTypes.Earth, statusEffects=Blind,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class fire_twister(Attack):
    desc = "Surrounds your enemy in a tornado of fire, dealing heavy damage."
    super().__init__("Fire Twister", desc, damage=10, atkType=AttackTypes.Fire, statusEffects=[],
                     target=TargetTypes.Enemy_All, manaCost=1)


class Scorch(Attack):
    desc = "Sets your enamy ablaze, dealing medium damage, and stunning them."
    super().__init__("Scorch", desc, damage=7, atkType=AttackTypes.Fire, statusEffects=Stun,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class fire_breathe(Attack):
    desc = "Shoots a breathe of fire at your enamy, blinding them and dealing medium damage."
    super().__init__("Fire Breathe", desc, damage=7, atkType=AttackTypes.Fire, statusEffects=Blind,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class tidal_wave(Attack):
    desc = "Hurls a huge wave toward your enemy, dealing heavy damage."
    super().__init__("Tidal Wave", desc, damage=10, atkType=AttackTypes.Water, statusEffects=[],
                     target=TargetTypes.Enemy_All, manaCost=1)


class whirl_pool(Attack):
    desc = "Surrounds your enemy in a tornado of Water, stunning them and dealing medium damage."
    super().__init__("Whirl Pool", desc, damage=7, atkType=AttackTypes.Water, statusEffects=Stun,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class Mist(Attack):
    desc = "Shoots a cloud of mist at the target, blinding them and dealing medium damage."
    super().__init__("Mist", desc, damage=7, atkType=AttackTypes.Water, statusEffects=Blind,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class Hurricane(Attack):
    desc = "150 mile per around wind tosses your opponent, dealing heavy damage."
    super().__init__("Hurricane", desc, damage=10, atkType=AttackTypes.Wind, statusEffects=[],
                     target=TargetTypes.Enemy_All, manaCost=1)


class Tornado(Attack):
    desc = "Surrounds your opponent in a whirling wind, stunning them and dealing medium damage."
    super().__init__("Tornado", desc, damage=7, atkType=AttackTypes.Wind, statusEffects=Stun,
                     target=TargetTypes.Enemy_Single, manaCost=1)


class poison_breeze(Attack):
    desc = "Blows a poison wind at your enemy, blinding them and dealing medium damage."
    super().__init__("Poison Breeze", desc, damage=7, atkType=AttackTypes.Wind, statusEffects=Blind,
                     target=TargetTypes.Enemy_Single, manaCost=1)
