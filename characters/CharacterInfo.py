# This module is used to keep track of information common to all characters (including players and enemies)

import random
from attacks.StatusEffects import Triggers
from copy import deepcopy
from attacks.AttacksInfo import *
from Multiplayer import IO
import time

# This is the base class for all characters
class Character:

    def __init__(self, name, desc, hp, mana, speed, attacks, weapons=[], armor=[], reward_xp=50):
        self.hp = hp
        self.maxHp = hp
        self.mana = mana
        self.maxMana = mana
        self.xp = 0
        self.maxXp = 150
        self.level = 1
        self.speed = speed
        self.maxSpeed = speed
        self.attacks = attacks
        self.name = name
        self.desc = desc
        self.totalArmor = 0
        self.totalMagResist = 0
        self.items = []
        self.clues = []
        self.weapons = []
        for weapon in weapons:
            self.equip_weapon(weapon, False)
        self.armor = []
        for a in armor:
            self.equip_armor(a, False)
        self.status_effects = []
        self.cannot_attack = 0
        self.attacks_disabled = []
        self.player_num = None
        self.is_player = False
        self.players_list = []
        self.reward_xp = reward_xp

    def battle_start(self, players_list):
        self.players_list = players_list

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
        IO.print_text(self.name + ": HP: " + str(self.hp) + " MANA: " + str(self.mana) + " SPEED: " + str(self.speed)
                      + ", Status: " + all_effects, self.players_list)

    def turn_end(self):
        self.trigger_status_effects(Triggers.ON_TURN_END, self)

    def choose_target(self, targets):
        if len(targets) == 0:
            return []
        elif len(targets) == 1:
            return targets
        else:
            return [targets[random.randint(0, len(targets)-1)]]

    # default behavior is to choose an attack randomly
    #   (this can be overridden in subclasses for more specific behavior)
    def choose_attack(self):
        time.sleep(2)
        attacks_enabled = []
        for a in self.attacks:
            if a.enabled:
                attacks_enabled.append(a)
        if len(attacks_enabled) > 0:
            attack_chosen = deepcopy(self.attacks[random.randint(0, len(attacks_enabled)-1)])
            IO.print_text(self.name + " uses " + attack_chosen.name, self.players_list)
            self.trigger_status_effects(Triggers.ON_ATTACKING, self, attack_chosen)
            return attack_chosen
        else:
            IO.print_text(self.name + " cannot attack this turn!",  self.players_list)
            return None

    def equip_weapon(self, weapon, show_message=True):
        if show_message:
            IO.print_text(self.name + " equipped " + weapon.name + "!", [self.player_num])
        self.weapons.append(weapon)
        self.learn_attack(weapon.attack, False)

    def equip_armor(self, Armor, show_message=True):
        if show_message:
            IO.print_text(self.name + " equipped " + Armor.name + "!", [self.player_num])
        self.armor.append(Armor)
        self.totalArmor += Armor.armor
        self.totalMagResist += Armor.magResist

    def learn_attack(self, attack, show_message=True):
        if show_message:
            IO.print_text(self.name + " learned " + attack.name + "!", [self.player_num])
        self.attacks.append(attack)


    # status effects
    def status_effect_add(self, effect):
        if random.randint(0, 100) <= effect.chance:
            for e in self.status_effects:
                if e.name == effect.name:
                    IO.print_text(self.name + " is already " + effect.name, self.players_list)
                    return

            IO.print_text(self.name + " is " + effect.name, self.players_list)
            time.sleep(1)
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

        if self.hp > self.maxHp:
            self.hp = self.maxHp

        if self.hp < 0:
            self.hp = 0

        if show_message:
            if damage >= 0:
                IO.print_text(self.name + " takes " + str(damage) + " damage!" + "  HP: " + str(self.hp),
                              self.players_list)
            else:
                IO.print_text(self.name + " is healed for " + str(-damage) + " damage! " + "HP: " + str(self.hp),
                              self.players_list)

        time.sleep(1.5)

        if self.hp == 0:
            IO.print_text(self.name + " has been defeated!",  self.players_list)
            time.sleep(2)


    # called when hit by an attack
    def hit_by(self, attack):

        self.trigger_status_effects(Triggers.ON_HIT_BY, self, attack)

        if attack.damage is not None:
            if attack.damage > 0:
                if attack.atkType == AttackTypes.Normal:
                    attack.damage -= (self.totalArmor/5)

                else:
                    attack.damage -= (self.totalMagResist/5)

                if attack.damage < 0:
                    attack.damage = 0

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

    def level_up(self, max_xp_mod=150, speed_mod=0, mana_mod=0, hp_mod=0):
        self.maxXp += max_xp_mod
        self.xp = 0

        for attack in self.attacks:
            attack.upgrade()

        self.maxSpeed += speed_mod
        self.speed = self.maxSpeed

        self.maxMana += mana_mod
        self.mana = self.maxMana

        self.maxHp += hp_mod
        self.hp = self.maxHp

    def change_hp(self, amount):
        if amount > 0:
            self.hp += amount
            if self.hp > self.maxHp:
                self.hp = self.maxHp
        else:
            if self.hp >= amount*-1:
                self.hp += amount
            else:
                self.hp = 0

    def change_mana(self, amount):
        if amount > 0:
            self.mana += amount
            if self.mana > self.maxMana:
                self.mana = self.maxMana
        else:
            if self.mana >= amount*-1:
                self.mana += amount
            else:
                self.mana = 0

    def change_speed(self, amount):
        if amount > 0:
            self.speed += amount
            if self.speed > self.maxSpeed:
                self.speed = self.maxSpeed
            else:
                if self.speed >= amount*-1:
                    self.speed += amount
                else:
                    self.speed = 0
