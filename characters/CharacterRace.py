from attacks import BasicAttacks
from characters.CharacterInfo import Character
from equipment.Armor import *


class Gnome(Character):
    def __init__(self):
        desc = "The Gnome has increased speed and may be able to dodge attacks."
        super().__init__("Gnome", desc, hp=10, mana=10, speed=20, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()],
                         armor=[leatherLegArmor(), leatherChestArmor(), leatherGloves(), leatherShoes()])

    def level_up(self, **kwargs):
        super().level_up(speed_mod=15, mana_mod=10, hp_mod=10)


class Ogre(Character):
    def __init__(self):
        desc = "The Ogre has increased HP and will last longer in fights."
        super().__init__("Ogre", desc, hp=20, mana=10, speed=5, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()],
                         armor=[plateLegArmor(), plateChestArmor(), plateGloves(), plateShoes()])

    def level_up(self, **kwargs):
        super().level_up(speed_mod=10, mana_mod=10, hp_mod=15)


class Elf(Character):
    def __init__(self):
        desc = "The elf has increased endurance and will be able to fight longer in battle."
        super().__init__("Elf", desc, hp=10, mana=20, speed=5, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()],
                         armor=[clothLegArmor(), clothChestArmor(), clothGloves(), clothShoes()])

    def level_up(self, **kwargs):
        super().level_up(speed_mod=10, mana_mod=15, hp_mod=10)


class Human(Character):
    def __init__(self):
        desc = "The human is a balanced race, having equal stats in all categories."
        super().__init__("Human", desc, hp=10, mana=10, speed=10, attacks=[BasicAttacks.Punch(), BasicAttacks.Block()],
                         armor=[chainmailLegArmor(), chainmailChestArmor(), chainmailGloves(), chainmailShoes()])

    def level_up(self, **kwargs):
        super().level_up(speed_mod=10, mana_mod=10, hp_mod=10)
