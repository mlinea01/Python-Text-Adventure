from copy import copy
from Multiplayer import IO
import random
from characters.Player import Player
import time

class TestClass:
    def __init__(self, value):
        self.value = value

class Battle:

    def start(self, players, enemies):
        self.players = players
        self.player_nums = []
        self.enemies = enemies

        p_num = 0
        while p_num < len(self.players):
            self.player_nums.append(self.players[p_num].player_num)
            p_num += 1

        self.fighters = copy(self.players)
        enemy_names = "A "
        try:
            enemy_num = 0
            while enemy_num < len(enemies):
                enemy = enemies[enemy_num]
                enemy_num += 1
                self.fighters.append(enemy)
                enemy_names += enemy.name
                if enemy_num < len(enemies)-1:
                    enemy_names += ", "
                elif enemy_num == len(enemies)-1:
                    enemy_names += " and "

            if len(enemy_names) > 1:
                print(enemy_names + " are about to attack!")
            else:
                print(enemy_names + " is about to attack!")

        except TypeError:
            self.enemies = [enemies]
            self.fighters.append(enemies)

        for fighter in self.fighters:
            fighter.battle_start(self.player_nums)

        while Battle.alive(self.enemies) and Battle.alive(self.players):
            self.fighters.sort(key=lambda char: char.speed, reverse=True)
            print(" ")
            print("ROUND START")
            print(" ")

            i = 0
            turn_num = 1
            while i < len(self.fighters):
                fighter = self.fighters[i]

                if fighter.hp <= 0:
                    i += 1
                    if fighter.is_player:
                        print(fighter.name + "is dead and cannot attack!")
                    continue

                print("Turn " + str(turn_num))
                turn_num += 1
                print(fighter.name + " is attacking!")
                fighter.turn_start()
                if fighter.is_player:
                    print("Level: " + str(fighter.level) + ", XP: " + str(fighter.xp) + " / " +
                                  str(fighter.maxXp))

                if fighter.cannot_attack > 0:
                    print(fighter.name + " cannot attack!")
                else:
                    chosen_attack = fighter.choose_attack(self)
                    if chosen_attack is not None:

                        target_list = copy(self.fighters)
                        chosen_attack.filter_targets(fighter, target_list)

                        if chosen_attack.multi_target is False:
                            target_list = fighter.choose_target(target_list)

                        time.sleep(2)
                        attack_missed = random.randint(1, 100) > chosen_attack.get_accuracy()
                        for target in target_list:

                            target_dodged = False
                            if chosen_attack.is_dodgeable:
                                if target.speed > fighter.speed:
                                    dodge_chance = ( (target.speed - fighter.speed) / fighter.speed) * 100
                                    if dodge_chance > 60:
                                        dodge_chance = 60
                                    if random.randint(1,100) <= dodge_chance:
                                        target_dodged = True

                            if attack_missed:
                                print(fighter.name + "'s " + "attack missed!")
                            elif target_dodged:
                                print(target.name + " dodged the attack!")
                            else:
                                target.hit_by(chosen_attack)

                            if fighter.is_player and target.hp == 0:
                                for fighter in players:
                                    fighter.character.xp += target.reward_xp
                                    print("You gained " + str(target.reward_xp) + " xp!", fighter.player_num)

                                    if fighter.character.xp >= fighter.character.maxXp:
                                        fighter.character.level += 1
                                        fighter.character.level_up()
                                        if fighter.character.level % 5 == 0:
                                            fighter.learn_new_spell()

                                        print(fighter.name + " grew to level " + str(fighter.character.level)
                                                      + "!")

                i += 1
                fighter.turn_end()
                if fighter.hp > 0 and Battle.alive(self.players) and Battle.alive(self.enemies):
                    print(fighter.name + "'s turn is over!")
                print(" ")
                time.sleep(3)

        return Battle.alive(self.players)

    def attack_has_targets(self, attacker, attack):
        target_list = copy(self.fighters)
        attack.filter_targets(attacker, target_list)
        return len(target_list) > 0

    @classmethod
    def alive(self, characters):
        for c in characters:
            if c.hp > 0:
                return True

        return False

    def get_enemies_of(self, character):
        if isinstance(character, Player):
            return self.enemies
        else:
            return self.players

    def get_allies_of(self, character):
        if isinstance(character, Player):
            return self.players
        else:
            return self.enemies
