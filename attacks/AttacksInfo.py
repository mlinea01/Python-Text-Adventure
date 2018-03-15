# This module is simply used to keep track of pre-defined values used by attack metadata (such as type)
import enum


# Base class for all attacks
class Attack:
    def __init__(self, name, desc, damage, atkType, statusEffects, manaCost, multi_target=False):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.atkType = atkType
        self.multi_target = multi_target
        self.manaCost = manaCost
        self.statusEffects = statusEffects
        self.enabled = True

    def upgrade(self):
        self.damage += 2

    # default targeting behavior is to target enemies. This can be overridden for different behavior.
    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_enemies(attacker, targets)


# This class keeps track of attack types - useful for things like determining resistances to certain moves
class AttackTypes(enum.Enum):
    Normal = enum.auto()
    Fire = enum.auto()
    Water = enum.auto()
    Earth = enum.auto()
    Wind = enum.auto()


# used for filtering valid targets for attacks
class TargetFilters:
    @classmethod
    def target_filter_enemies(cls, attacker, targets):
        for target in targets:
            if target.is_player == attacker.is_player:
                targets.remove(target)

    @classmethod
    def target_filter_allies(cls, attacker, targets):
        for target in targets:
            if target.is_player != attacker.is_player:
                targets.remove(target)

    @classmethod
    def target_filter_self(cls, attacker, targets):
        for target in targets:
            if target != attacker:
                targets.remove(target)
