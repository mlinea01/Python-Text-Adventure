from copy import deepcopy


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

        if len(attacks_enabled) > 0:
            print("Choose your attack: ")
            attack_num = 1
            chosen_attack_num = -1
            for attack in self.character.attacks:
                if attack.enabled:
                    print(str(attack_num) + ". " + attack.name + " - " + attack.desc)
                else:
                    print(str(attack_num) + ". " + attack.name + " - (DISABLED)")
                attack_num += 1

            while chosen_attack_num < 0 or chosen_attack_num > len(self.character.attacks) \
                    or self.attacks[chosen_attack_num].enabled is False:
                chosen_attack_num = int(input("Your choice: "))-1
                if chosen_attack_num < 0 or chosen_attack_num > len(self.character.attacks):
                    print("Please choose a valid attack number from the list!")
                elif self.attacks[chosen_attack_num].enabled is False:
                    print("That attack is disabled this turn!")
                    continue

            return deepcopy(self.character.attacks[chosen_attack_num])
        else:
            print(self.name + " cannot attack this turn!")
            return None

    def __getattr__(self, item):
        if hasattr(self.character, item):
            return self.character.__getattribute__(item)
