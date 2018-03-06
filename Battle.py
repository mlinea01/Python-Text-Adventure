from copy import copy
from Multiplayer import IO
import random
from characters.Player import Player
from attacks.AttacksInfo import TargetTypes

class Battle:

    def __init__(self, players, enemy):

        self.players = players
        self.player_nums = []
        self.enemy = enemy

        p_num = 0
        while p_num < len(self.players):
            self.player_nums.append(self.players[p_num].player_num)
            p_num += 1

        fighters = copy(self.players)
        fighters.append(enemy)

        for fighter in fighters:
            fighter.battle_start(self.player_nums)

        while enemy.hp > 0 and self.playersAlive(self.players):

            i = 0
            while i < len(fighters):
                fighter = fighters[i]

                if fighter.hp <= 0:
                    i += 1
                    continue

                fighter.turn_start()

                if i == len(fighters)-1:
                    other_fighter = players[0]
                else:
                    other_fighter = enemy

                if fighter.cannot_attack > 0:
                    IO.print_text(fighter.name + " cannot attack!", self.player_nums)
                else:
                    chosen_attack = fighter.choose_attack()
                    if chosen_attack is not None:

                        IO.print_text(fighter.name + " uses " + chosen_attack.name, self.player_nums)
                        target_list = []
                        can_choose_target = False
                        if chosen_attack.target == TargetTypes.Enemy_Single:
                            can_choose_target = True
                            target_list = self.get_enemies_of(fighter)
                        elif chosen_attack.target == TargetTypes.Ally_Single:
                            can_choose_target = True
                            target_list = self.get_allies_of(fighter)
                        elif chosen_attack.target == TargetTypes.Self:
                            can_choose_target = False
                            target_list = [fighter]
                        elif chosen_attack.target == TargetTypes.Enemy_All:
                            can_choose_target = False
                            target_list = self.get_enemies_of(fighter)
                        elif chosen_attack.target == TargetTypes.Ally_All:
                            can_choose_target = False
                            target_list = self.get_allies_of(fighter)

                        if can_choose_target:
                            target_list = fighter.choose_target(target_list)

                        for target in target_list:
                            if target.speed > fighter.speed:
                                attack_missed = random.randint(1,3)
                                if attack_missed == 1:
                                    IO.print_text(fighter.name + " " + "attack missed!")
                                else:
                                    target.hit_by(chosen_attack)
                            else:
                                target.hit_by(chosen_attack)

                            if enemy.hp == 0:
                                IO.print_text("You gained 50 xp!")
                                fighter.character.xp += 50
                                if fighter.character.xp == fighter.character.maxXp:
                                    fighter.character.level += 1
                                    fighter.character.maxXp += 150
                                    fighter.character.xp = 0

                                    fighter.character.mana = fighter.character.maxMana
                                    fighter.character.mana += 10
                                    fighter.character.maxMana = fighter.character.mana

                                    fighter.character.hp = fighter.character.maxHp
                                    fighter.character.hp += 10
                                    fighter.character.maxHp = fighter.character.hp

                                    IO.print_text("You grew to level " + str(fighter.character.level))

                i += 1
                fighter.turn_end()
                IO.print_text("", self.player_nums)

    def playersAlive(self, players):
        for player in players:
            if player.hp > 0:
                return True

        return False

    def get_enemies_of(self, character):
        if isinstance(character, Player):
            return [self.enemy]
        else:
            return self.players

    def get_allies_of(self, character):
        if isinstance(character, Player):
            return self.players
        else:
            return [self.enemy]
