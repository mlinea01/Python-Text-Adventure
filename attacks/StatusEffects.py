# This module is for status effects usually applied by attacks (i.e. shields, poison, stuns, etc.)
from Multiplayer import IO

# the things that can trigger a status effect to perform some action (start of turn, getting hit by attack, etc.)
class Triggers:
    ON_EFFECT_APPLY = "on_effect_apply"
    ON_TURN_START = "on_turn_start"
    ON_TURN_END = "on_turn_end"
    ON_HIT_BY = "on_hit_by"
    ON_ATTACKING = "on_attacking"


# this class defines thing common to all Status Effects (like how they extract data from trigger arguments
class StatusEffect:
    def __init__(self):
        self.character = None
        self.attack = None
        self.is_resolved = False

    def on_effect_apply_getargs(self, args):
        self.character = args[0]

    def on_turn_start_getargs(self, args):
        self.character = args[0]

    def on_turn_end_getargs(self, args):
        self.character = args[0]

    def on_hit_by_getargs(self, args):
        self.character = args[0]
        self.attack = args[1]

    def on_attacking_getargs(self, args):
        self.character = args[0]
        self.attack = args[1]

    def resolve(self):
        self.character.status_effect_remove(self)


class Shield(StatusEffect):
    def __init__(self, shieldAmount, duration=1, chance=100):
        super().__init__()
        self.name = "is shielded"
        self.amount = shieldAmount
        self.duration = duration
        self.chance = chance

    def on_hit_by(self, args):
        super().on_hit_by_getargs(args)
        blocked_amount = self.amount
        if self.attack.damage is None or self.attack.damage == 0:
            return
        if self.attack.damage < self.amount:
            blocked_amount = self.attack.damage

        IO.print_text(self.character.name + " blocked " + str(blocked_amount) + " damage!")
        self.attack.damage -= blocked_amount
        self.amount -= blocked_amount
        if self.amount <= 0:
            self.character.status_effect_remove(self)

    def on_turn_start(self, args):
        super().on_turn_start_getargs(args)
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True


class Stun(StatusEffect):
    def __init__(self, stunDuration, chance=100):
        super().__init__()
        self.name = "is stunned"
        self.duration = stunDuration
        self.chance = chance

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        self.character.cannot_attack += 1

    def on_turn_end(self, args):
        super().on_turn_end_getargs(args)
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True

    def resolve(self):
        self.character.cannot_attack -= 1
        super().resolve()


class Blind(StatusEffect):
    def __init__(self, blindDuration, chance=100):
        super().__init__()
        self.name = "is blinded"
        self.duration = blindDuration
        self.chance = chance

    def on_attacking(self, args):
        super().on_attacking_getargs(args)
        self.attack.change_accuracy(-50)

    def on_turn_end(self, args):
        super().on_turn_end_getargs(args)
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True


class Bleed(StatusEffect):
    def __init__(self, bleedDuration, damage=1, chance=100):
        super().__init__()
        self.name = "is bleeding"
        self.duration = bleedDuration
        self.damage = damage
        self.chance = chance

    def on_turn_end(self, args):
        super().on_turn_end_getargs(args)
        hpLeft = self.character.hp-self.damage
        if hpLeft < 0:
            hpLeft = 0
        IO.print_text(self.character.name + " takes " + str(self.damage) + " damage from bleeding! HP: " + str(hpLeft))
        self.character.apply_damage(self.damage, False)
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True


class Poison(StatusEffect):
    def __init__(self, poison_duration=1, damage=1, chance=100):
        super().__init__()
        self.name = "is poisoned"
        self.duration = poison_duration
        self.damage = damage
        self.chance = chance

    def on_turn_end(self, args):
        super().on_turn_end_getargs(args)
        hpLeft = self.character.hp-self.damage
        if hpLeft < 0:
            hpLeft = 0
        IO.print_text(self.character.name + " takes " + str(self.damage) + " damage from poison! HP: " + str(hpLeft))
        self.character.apply_damage(self.damage, False)
        self.duration -= 1
        self.damage += 1
        if self.duration == 0:
            self.is_resolved = True


class Paralyze(StatusEffect):
    def __init__(self, paralyzeDuration, chance=100):
        super().__init__()
        self.name = "is paralyzed"
        self.duration = paralyzeDuration
        self.chance = chance

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        self.character.cannot_attack += 1

    def on_turn_end(self, args):
        super().on_turn_end_getargs(args)
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True

    def resolve(self):
        self.character.cannot_attack -= 1
        super().resolve()


class Slow(StatusEffect):
    def __init__(self, slowDuration, slow_amount=2, chance=100):
        super().__init__()
        self.name = "is slowed"
        self.duration = slowDuration+1
        self.chance = chance
        self.amount = slow_amount

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        if self.character.speed >= self.amount:
            self.character.speed -= self.amount
        else:
            self.character.speed = 0

    def resolve(self):
        self.character.speed += self.amount
        super().resolve()

    def on_turn_start(self, args):
        super().on_turn_start_getargs(args)
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True


class DamageBoost(StatusEffect):
    def __init__(self, amount, duration, chance=100):
        super().__init__()
        self.name = "now has increased damage"
        self.amount = amount
        self.duration = duration
        self.chance = chance

    def on_attacking(self, args):
        super().on_attacking_getargs(args)
        if self.attack.damage is not None and self.attack.damage > 0:
            self.attack.damage += self.amount

    def on_turn_end(self, args):
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True


class HpBoost(StatusEffect):
    def __init__(self, amount):
        super().__init__()
        self.name = "is healed"
        self.amount = amount
        self.chance = 100

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        self.character.change_hp(self.amount)
        self.is_resolved = True
        print(self.character.name + "'s HP is now " + str(self.character.hp))


class manaBoost(StatusEffect):
    def __init__(self, amount):
        super().__init__()
        self.name = "is imbued with mana"
        self.amount = amount
        self.chance = 100

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        self.character.change_mana(self.amount)
        self.is_resolved = True
        print(self.character.name + "'s mana is now " + str(self.character.mana))

class speedBoost(StatusEffect):
    def __init__(self, amount, duration):
        super().__init__()
        self.name = "is faster"
        self.amount = amount
        self.duration = duration
        self.chance = 100

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        self.character.change_speed(self.amount)
        self.is_resolved = True
        print(self.character.name + "'s speed is now " + str(self.character.speed))

    def on_turn_end(self, args):
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True


class charmed(StatusEffect):
    def __init__(self, duration, chance=100):
        super().__init__()
        self.name = "is charmed"
        self.duration = duration
        self.chance = chance

    def on_attacking(self, args):
        super().on_attacking_getargs(args)
        self.attack.change_accuracy(-50)

    def on_turn_end(self, args):
        self.duration -= 1
        if self.duration == 0:
            self.is_resolved = True

class antiCharmed(StatusEffect):
    def __init__(self, duration=1):
        super().__init__()
        self.name = "is no longer charmed"
        self.duration = duration
        self.chance = 100

    def on_effect_apply(self, args):
        super().on_effect_apply_getargs(args)
        for status_effect in self.character.status_effects:
            if status_effect.name == "charmed":
                status_effect.is_resolved = True
        self.is_resolved = True