# This module is used to keep track of information common to all characters (including players and enemies)

import random
from attacks.StatusEffects import Triggers
from copy import deepcopy

# This is the base class for all characters
class Character:

    def __init__(self, name, desc, hp, mana, speed, attacks, weapons=[]):
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.attacks = attacks
        self.name = name
        self.desc = desc
        self.weapons = []
        for weapon in weapons:
            self.equip_weapon(weapon, False)
        self.status_effects = []
        self.cannot_attack = 0
        self.attacks_disabled = []

    # start and ending turn in battle
    def turn_start(self):
        self.trigger_status_effects(Triggers.ON_TURN_START, self)
        all_effects = "Normal"
        effect_num = 0
        while effect_num < len(self.status_effects):
            if effect_num == 0:
                all_effects = ""
            all_effects += self.status_effects[effect_num].name
            if effect_num < len(self.status_effects)-1:
                all_effects += ", "
            effect_num += 1
        print(self.name + ":  HP: " + str(self.hp) + ", Status: " + all_effects)

    def turn_end(self):
        self.trigger_status_effects(Triggers.ON_TURN_END, self)

    # default behavior is to choose an attack randomly
    #   (this can be overridden in subclasses for more specific behavior)
    def choose_attack(self):
        attacks_enabled = []
        for a in self.attacks:
            if a.enabled:
                attacks_enabled.append(a)
        if len(attacks_enabled) > 0:
            attack_chosen = deepcopy(self.attacks[random.randint(0, len(attacks_enabled)-1)])
            self.trigger_status_effects(Triggers.ON_ATTACKING, self, attack_chosen)
            return attack_chosen
        else:
            print(self.name + " cannot attack this turn!")
            return None

    def equip_weapon(self, weapon, show_message=True):
        if show_message:
            print(self.name + " equipped " + weapon.name + "!")
        self.weapons.append(weapon)
        self.learn_attack(weapon.attack, False)

    def learn_attack(self, attack, show_message=True):
        if show_message:
            print(self.name + " learned " + attack.name + "!")
        self.attacks.append(attack)


    # status effects
    def status_effect_add(self, effect):
        if random.randint(0, 100) <= effect.chance:
            for e in self.status_effects:
                if e.name == effect.name:
                    print(self.name + " is already " + effect.name)
                    return

            print(self.name + " is " + effect.name)
            self.status_effects.append(effect)
            self.trigger_status_effects(Triggers.ON_EFFECT_APPLY, self)

    def status_effect_remove(self, status_effect):
        for effect in self.status_effects:
            if effect == status_effect:
                self.status_effects.remove(effect)

    def trigger_status_effects(self, trigger, *args):
        for effect in self.status_effects:
            if hasattr(effect, trigger):
                effect.__getattribute__(trigger)(args)

        for effect in self.status_effects:
            if effect.is_resolved:
                effect.resolve()

    def apply_damage(self, damage, show_message=True):
        # subtract hp and check for defeat
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        if show_message:
            print(self.name + " takes " + str(damage) + " damage!" + "  HP: " + str(self.hp))

        if self.hp == 0:
            print(self.name + " has been defeated!")


    # called when hit by an attack
    def hit_by(self, attack):

        self.trigger_status_effects(Triggers.ON_HIT_BY, self, attack)

        if attack.damage is not None:
            self.apply_damage(attack.damage)

        if self.hp > 0:
            # if not defeated, apply status effect(s) - one or more can be applied
            try:
                for effect in attack.statusEffects:
                    self.status_effect_add(effect)
            except TypeError:
                self.status_effect_add(attack.statusEffects)

    def attack_disable(self, attack):
        attack.enabled = False

    def attack_enable(self, attack):
        attack.enabled = True
