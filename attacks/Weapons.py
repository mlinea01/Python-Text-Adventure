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
        name = "Long Sword"
        desc = "Long steel sword with razor sharp edges that can cut through anything!"
        attack_desc = "Slash with your Long Sword making your opponent bleed."
        attack = Attack(name, attack_desc, damage=2, atkType=AttackTypes.Normal,
                        statusEffects=Bleed(bleedDuration=2, chance=50), manaCost=0)
        super().__init__(name, desc, attack, value=10)


class WarHammer(Weapon):
    def __init__(self):
        name = "War Hammer"
        desc = "Huge hammer with metal head that cannot be shattered, and a steel handle to swing the hammer so hard" \
               "it can break a mountain into a million pieces!"
        attack_desc = "Swing your mighty War Hammer and paralyze your opponent!"
        attack = Attack(name, attack_desc, damage=2, atkType=AttackTypes.Normal,
                        statusEffects=Paralyze(paralyzeDuration=1, chance=50), manaCost=0)
        super().__init__(name, desc, attack, value=10)


class Staff(Weapon):
    def __init__(self):
        name = "Staff"
        desc = "A long staff specifically used in martial arts made from magical wood that possesses incredible " \
               "power. It looks like nothing but make no mistake, you will feel the affects of this staff from around" \
               "the world!"
        attack_desc = "Strike swiftly with your staff slowing your opponent"
        attack = Attack(name, attack_desc, damage=2, atkType=AttackTypes.Normal,
                        statusEffects=Slow(slowDuration=1, chance=100), manaCost=0)
        super().__init__(name, desc, attack, value=10)


class BattleAxe(Weapon):
    def __init__(self):
        name = "Battle Axe"
        desc = "An axe molded from moon rocks and molten lava! This axe can cut through to the center of the WORLD!"
        attack_desc = "Swing your deadly Battle Axe making your opponent bleed."
        attack = Attack(name, attack_desc, damage=2, atkType=AttackTypes.Normal,
                        statusEffects=Bleed(bleedDuration=1, chance=100), manaCost=0)
        super().__init__(name, desc, attack, value=10)


class Trident(Weapon):
    def __init__(self):
        name = "Trident"
        desc = "This trident was said to be the one and only trident from the depths of Atlantis! Wielding the power" \
               "of the sea!"
        attack_desc = "Strike with your mighty Trident making you opponent bleed."
        attack = Attack(name, desc, damage=2, atkType=AttackTypes.Normal,
                        statusEffects=Bleed(bleedDuration=1, chance=50), manaCost=0)
        super().__init__(name, desc, attack, value=10)


class BowAndArrow(Weapon):
    def __init__(self):
        name = "Bow and Arrow"
        desc = "This bow and its arrows were crafted from the AVATAR him self, giving it the ability to manipulate" \
               "the elements around us!"
        attack_desc = "Aim true with an Arrow that will slow your opponent from afar"
        attack = Attack(name, attack_desc, damage=2, atkType=AttackTypes.Normal,
                        statusEffects=Slow(slowDuration=1), manaCost=0)
        super().__init__(name, desc, attack, value=10)
