from copy import deepcopy
from attacks.StatusEffects import Triggers
from Multiplayer import IO
from functools import partial

# Player class used to keep track of player stats and actions
class Player:

    def __init__(self, name, character, player_num, character_type):
        self.character = character
        self.race = character.name
        self.player_num = player_num
        self.character.player_num = player_num
        self.character_type = character_type
        self.desc = "mighty"
        character.name = name
        character.is_player = True

    def choose_target(self, targets):
        if len(targets) == 0:
            return []
        elif len(targets) == 1:
            return targets
        else:
            target_num = 1
            IO.print_text("Choose target: ", [self.player_num])
            for target in targets:
                IO.print_text(str(target_num) + ". " + target.name, [self.player_num])
                target_num += 1
            target_choice = int(IO.get_input(self.player_num, "Your choice: ",
                                             partial(IO.check_num_in_range, minimum=1, maximum=len(targets))))-1
            return [targets[target_choice]]

    def choose_attack(self):
        attacks_enabled = []
        for a in self.attacks:
            if a.enabled:
                attacks_enabled.append(a)

        if len(attacks_enabled) > 0 or len(self.character.items) > 0:
            IO.print_text("Choose your attack: ", [self.player_num])
            attack_num = 1
            for attack in self.character.attacks:
                if attack.enabled:
                    IO.print_text(str(attack_num) + ". " + attack.name + " - " + attack.desc, [self.player_num])
                else:
                    IO.print_text(str(attack_num) + ". " + attack.name + " - (DISABLED)", [self.player_num])
                attack_num += 1

            for item in self.character.items:
                IO.print_text(str(attack_num) + ". " + item.name, [self.player_num])
                attack_num += 1

            chosen_attack_num = int(IO.get_input(self.player_num, "Your choice: ", partial(IO.check_num_in_range, minimum=1,
                                             maximum=len(self.character.attacks) + len(self.character.items))))-1

            while True:
                if chosen_attack_num < len(self.character.attacks):
                    if self.attacks[chosen_attack_num].enabled is False:
                        IO.print_text("That attack is disabled this turn!", [self.player_num])
                        return self.choose_attack()
                    else:
                        attack_chosen = deepcopy(self.character.attacks[chosen_attack_num])
                        IO.print_text(self.name + " uses " + attack_chosen.name, self.player_nums)
                        self.trigger_status_effects(Triggers.ON_ATTACKING, self.character, attack_chosen)
                        if self.character.mana > 0 and not(self.character.mana < attack_chosen.manaCost):
                            self.character.mana -= attack_chosen.manaCost
                        elif self.character.mana < attack_chosen.manaCost:
                            IO.print_text("You don't have enough mana for that attack")
                            return self.choose_attack()
                        else:
                            self.character.mana = 0
                        return attack_chosen
                else:
                    chosen_item = self.character.items[chosen_attack_num - len(self.character.attacks)]
                    IO.print_text(self.character.name + " used a " + chosen_item.name, [self.player_num])
                    chosen_item.use_item_on(self.character)
                    self.character.items.remove(chosen_item)
                    return None
        else:
            IO.print_text(self.name + " cannot attack this turn!", [self.player_num])
            return None

    def __getattr__(self, item):
        if hasattr(self.character, item):
            return self.character.__getattribute__(item)
