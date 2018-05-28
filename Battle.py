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

        fighters = copy(self.players)
        try:
            for enemy in enemies:
                fighters.append(enemy)
        except TypeError:
            self.enemies = [enemies]
            fighters.append(enemies)

        for fighter in fighters:
            fighter.battle_start(self.player_nums)

        while Battle.alive(self.enemies) and Battle.alive(self.players):
            fighters.sort(key=lambda char: char.speed, reverse=True)
            IO.print_text(" ", self.player_nums)
            IO.print_text("ROUND START", self.player_nums)
            IO.print_text(" ", self.player_nums)

            i = 0
            turn_num = 1
            while i < len(fighters):
                fighter = fighters[i]

                if fighter.hp <= 0:
                    i += 1
                    continue

                IO.print_text("Turn " + str(turn_num), self.player_nums)
                turn_num += 1
                IO.print_text(fighter.name + " is attacking!", self.player_nums)
                fighter.turn_start()
                if fighter.is_player:
                    IO.print_text("Level: " + str(fighter.level) + ", XP: " + str(fighter.xp) + " / " +
                                  str(fighter.maxXp), self.player_nums)

                if fighter.cannot_attack > 0:
                    IO.print_text(fighter.name + " cannot attack!", self.player_nums)
                else:
                    chosen_attack = fighter.choose_attack()
                    if chosen_attack is not None:

                        target_list = copy(fighters)
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
                                IO.print_text(fighter.name + "'s " + "attack missed!", self.player_nums)
                            elif target_dodged:
                                IO.print_text(target.name + " dodged the attack!", self.player_nums)
                            else:
                                target.hit_by(chosen_attack)

                            if fighter.is_player and target.hp == 0:
                                for fighter in players:
                                    fighter.character.xp += target.reward_xp
                                    IO.print_text("You gained " + str(target.reward_xp) + " xp!", fighter.player_num)

                                    if fighter.character.xp >= fighter.character.maxXp:
                                        fighter.character.level += 1
                                        fighter.character.level_up()

                                        IO.print_text(fighter.name + " grew to level " + str(fighter.character.level)
                                                      + "!", self.player_nums)

                i += 1
                fighter.turn_end()
                if fighter.hp > 0 and Battle.alive(self.players) and Battle.alive(self.enemies):
                    IO.print_text(fighter.name + "'s turn is over!", self.player_nums)
                IO.print_text(" ", self.player_nums)
                time.sleep(3)

        return Battle.alive(self.players)

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
