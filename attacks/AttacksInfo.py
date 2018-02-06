# This module is simply used to keep track of pre-defined values used by attack metadata (such as type)
import enum


# Base class for all attacks
class Attack:
    def __init__(self, name, desc, damage, atkType, statusEffects, target, manaCost):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.atkType = atkType
        self.target = target
        self.manaCost = manaCost
        self.statusEffects = statusEffects


# This class keeps track of attack types - useful for things like determining resistances to certain moves
class AttackTypes(enum.Enum):
    Normal = enum.auto()
    Fire = enum.auto()
    Water = enum.auto()
    Earth = enum.auto()
    Wind = enum.auto()


# This class keeps track of the different types of targets attacks can have
class TargetTypes(enum.Enum):
    Self = enum.auto()
    Enemy_Single = enum.auto()
    Enemy_All = enum.auto()
    Ally_Single = enum.auto()
    Ally_All = enum.auto()
