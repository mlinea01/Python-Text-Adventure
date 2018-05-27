# This module is simply used to keep track of pre-defined values used by attack metadata (such as type)
import enum
from Multiplayer import IO


# Base class for all attacks
class Attack:
    def __init__(self, name, desc, damage, atkType, statusEffects, manaCost, multi_target=False, accuracy=100):
        self.name = name
        self.desc = desc
        self.damage = damage
        self.atkType = atkType
        self.multi_target = multi_target
        self.manaCost = manaCost
        self.statusEffects = statusEffects
        self.enabled = True
        self._accuracy = accuracy

    def upgrade(self):
        self.damage += 2

    # default targeting behavior is to target enemies. This can be overridden for different behavior.
    def filter_targets(self, attacker, targets):
        TargetFilters.target_filter_enemies(attacker, targets)

    def change_accuracy(self, amount):
        self._accuracy += amount
        if self._accuracy < 0:
            self._accuracy = 0
        if self._accuracy > 100:
            self._accuracy = 100

    def get_accuracy(self):
        return self._accuracy


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
        targetIndex = 0
        while targetIndex < len(targets):
            target = targets[targetIndex]
            if target.is_player == attacker.is_player:
                targets.remove(target)
            else:
                targetIndex += 1

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
