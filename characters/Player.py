from copy import deepcopy
from attacks.StatusEffects import Triggers

# Player class used to keep track of player stats and actions
class Player:

    def __init__(self, name, character):
        self.character = character
        self.race = character.name
        character.name = name

    def choose_attack(self):
        attacks_enabled = []
        for a in self.attacks:
            if a.enabled:
                attacks_enabled.append(a)

        if len(attacks_enabled) > 0 or len(self.character.items) > 0:
            print("Choose your attack: ")
            attack_num = 1
            chosen_attack_num = -1
            for attack in self.character.attacks:
                if attack.enabled:
                    print(str(attack_num) + ". " + attack.name + " - " + attack.desc)
                else:
                    print(str(attack_num) + ". " + attack.name + " - (DISABLED)")
                attack_num += 1

            for item in self.character.items:
                print(str(attack_num) + ". " + item.name)
                attack_num += 1

            while chosen_attack_num < 0 or chosen_attack_num > len(self.character.attacks) + len(self.character.items) \
                    or self.attacks[chosen_attack_num].enabled is False:
                chosen_attack_num = int(input("Your choice: "))-1
                if chosen_attack_num < 0 or chosen_attack_num > len(self.character.attacks) + len(self.character.items):
                    print("Please choose a valid attack or item number from the list!")
                elif chosen_attack_num > len(self.character.attacks):
                    chosen_item = self.character.items[chosen_attack_num - len(self.character.attacks)]
                    chosen_item.use_item_on(self)
                elif self.attacks[chosen_attack_num].enabled is False:
                    print("That attack is disabled this turn!")
                    continue

            attack_chosen = deepcopy(self.character.attacks[chosen_attack_num])
            self.trigger_status_effects(Triggers.ON_ATTACKING, self.character, attack_chosen)
            return attack_chosen
        else:
            print(self.name + " cannot attack this turn!")
            return None

    def __getattr__(self, item):
        if hasattr(self.character, item):
            return self.character.__getattribute__(item)
