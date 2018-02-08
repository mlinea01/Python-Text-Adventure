from attacks.AttacksInfo import *
from attacks.StatusEffects import *


# a base class that all weapons extend. It has an attack variable but also other data like its own name, description,
# monetary value, etc. Maybe we'll think of more things a weapon can have or just keep it like this.
class Weapon:
    def __init__(self, name, desc, attack, value):
        self.name = name
        self.desc = desc
        self.attack = attack
        self.value = value


class Sword(Weapon):
    def __init__(self):
        desc = "Long steel sword with razor sharp edges that can cut through anything!"
        attack = Attack("Swing Long Sword", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Bleed(1),
                         target=TargetTypes.Enemy_Single, manaCost=0)
        super().__init__("Long Sword", desc, attack, value=10)


class war_hammer(Attack):
    def __init__(self):
        desc = "Huge hammer with metal head that cannot be shattered, and a steel handle to swing the hammer so hard" \
               "it can break a mountain into a million pieces!"
        super().__init__("War Hammer", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Paralyze(1),
                         target=TargetTypes.Enemy_Single, manaCost=0)


class Staff(Attack):
    def __init__(self):
        desc = "A long staff specifically used in martial arts made from magical wood that possesses incredible " \
               "power. It looks like nothing but make no mistake, you will feel the affects of this staff from around" \
               "the world!"
        super().__init__("Staff", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Slow(1),
                         target=TargetTypes.Enemy_Single, manaCost=0)


class battle_axe(Attack):
    def __init__(self):
        desc = "An axe molded from moon rocks and molten lava! This axe can cut through to the center of the WORLD!"
        super().__init__("Battle Axe", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Bleed(1),
                         target=TargetTypes.Enemy_Single, manaCost=0)


class Trident(Attack):
    def __init__(self):
        desc = "This trident was said to be the one and only trident from the depths of Atlantis! Wielding the power" \
               "of the sea!"
        super().__init__("Trident", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Bleed(1),
                         target=TargetTypes.Enemy_Single, manaCost=0)

class bowAndArrow(Attack):
    def __init__(self):
        desc = "This bow and its arrows were crafted from the AVATAR him self, giving it the ability to manipulate" \
               "the elements around us!"
        super().__init__("Bow and Arrow", desc, damage=2, atkType=AttackTypes.Normal, statusEffects=Slow(1),
                         target=TargetTypes.Enemy_Single, manaCost=0)
