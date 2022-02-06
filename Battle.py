from copy import copy
import random
from characters.Player import Player
import time


class Battle:

    fighters = None
    players = None
    enemies = None

    @classmethod
    def start(cls, player, enemies):
        cls.fighters = [player]

        for enemy in enemies:
            cls.fighters.append(enemy)

        enemy_names = "A "
        enemy_num = 0
        while enemy_num < len(enemies):
            enemy = enemies[enemy_num]
            enemy_num += 1
            enemy_names += enemy.name
            if enemy_num < len(enemies)-1:
                enemy_names += ", "
            elif enemy_num == len(enemies)-1:
                enemy_names += " and "

        if len(enemy_names) > 1:
            print(enemy_names + " are about to attack!")
        else:
            print(enemy_names + " is about to attack!")

        while cls.alive(enemies) and cls.alive(player):
            print(" ")
            print("ROUND START")
            print(" ")

            i = 0
            turn_num = 1

            while i < len(cls.fighters):
                fighter = cls.fighters[i]

                if fighter.hp <= 0:
                    i += 1
                    continue

                print("Turn " + str(turn_num))
                turn_num += 1
                print(fighter.name + " is attacking!")
                fighter.turn_start()
                if fighter.is_player:
                    print("Level: " + str(fighter.level) + ", XP: " + str(fighter.xp) + " / " +
                                  str(fighter.maxXp))

                if fighter.cannot_attack > 0:
                    print("You cannot attack!")
                else:
                    chosen_attack = fighter.choose_attack(cls)
                    if chosen_attack is not None:

                        target_list = copy(cls.fighters)
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
                                print("Your attack missed!")
                            elif target_dodged:
                                print(target.name + " dodged the attack!")
                            else:
                                target.hit_by(chosen_attack)

                            if fighter.is_player and target.hp == 0:
                                fighter.character.xp += target.reward_xp
                                print("You gained " + str(target.reward_xp) + " xp!", fighter.player_num)

                                if fighter.character.xp >= fighter.character.maxXp:
                                    fighter.character.level += 1
                                    fighter.character.level_up()
                                    if fighter.character.level % 5 == 0:
                                        fighter.learn_new_spell()

                                    print("You grew to level " + str(fighter.character.level)
                                                      + "!")

                i += 1
                fighter.turn_end()
                if fighter.hp > 0 and Battle.alive(player) and Battle.alive(enemies):
                    print(fighter.name + "'s turn is over!")
                print(" ")
                time.sleep(3)

        return Battle.alive(player)


    @classmethod
    def attack_has_targets(cls, attacker, attack):
        target_list = copy(cls.fighters)
        attack.filter_targets(attacker, target_list)
        return len(target_list) > 0

    @classmethod
    def alive(cls, character):
        try:
            if character.hp > 0:
                return True
            return False
        except TypeError:
            return character.hp > 0

    @classmethod
    def get_enemies_of(cls, character):
        if isinstance(character, Player):
            return cls.enemies
        else:
            return cls.players
