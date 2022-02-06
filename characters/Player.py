from copy import deepcopy
from characters.CharacterLevelUp import *


# Player class used to keep track of player stats and actions
class Player:

    def __init__(self, name, character, character_type):
        self.character = character
        self.race = character.name
        self.character.character_type = character_type
        self.desc = "mighty"
        self.money = 10
        character.name = name
        character.is_player = True

    def choose_target(self, targets):
        if len(targets) == 0:
            return []
        elif len(targets) == 1:
            return targets
        else:
            target_num = 1
            print("Choose target: ")
            for target in targets:
                print(str(target_num) + ". " + target.name)
                target_num += 1
            target_choice = int(input("Your choice: ")) - 1
            return [targets[target_choice]]

    def choose_attack(self, battle):
        attacks_enabled = []
        for a in self.attacks:
            if not a.enabled:
                a.disabled_message = "That attack is disabled this turn!"

            if not battle.attack_has_targets(self, a):
                a.enabled = False
                a.disabled_message = "That attack has no valid targets!"

            if a.enabled:
                attacks_enabled.append(a)

        if len(attacks_enabled) > 0 or len(self.character.items) > 0:
            print("Choose your attack: ")
            attack_num = 1
            for attack in self.character.attacks:
                if attack.enabled:
                    print(str(attack_num) + ". " + attack.name + " - " + attack.desc)
                else:
                    print(str(attack_num) + ". " + attack.name + " - (DISABLED)")
                attack_num += 1

            for item in self.character.items:
                print(str(attack_num) + ". " + item.name)
                attack_num += 1

            chosen_attack_num = int(input("Your choice: ")) - 1

            while True:
                if chosen_attack_num < len(self.character.attacks):
                    if self.attacks[chosen_attack_num].enabled is False:
                        print(self.attacks[chosen_attack_num].disabled_message)
                        return self.choose_attack()
                    else:
                        attack_chosen = deepcopy(self.character.attacks[chosen_attack_num])
                        print(self.name + " uses " + attack_chosen.name)
                        self.trigger_status_effects(Triggers.ON_ATTACKING, self.character, attack_chosen)
                        if self.character.mana > 0 and not (self.character.mana < attack_chosen.manaCost):
                            self.character.mana -= attack_chosen.manaCost
                        elif self.character.mana < attack_chosen.manaCost:
                            print("You don't have enough mana for that attack")
                            return self.choose_attack()
                        else:
                            self.character.mana = 0
                        return attack_chosen
                else:
                    chosen_item = self.character.items[chosen_attack_num - len(self.character.attacks)]
                    print("You used a " + chosen_item.name)
                    self.character.items.remove(chosen_item)
                    return chosen_item.itemAttack
        else:
            print("You cannot attack this turn!")
            return None

    def learn_new_spell(self):
        spellTypes = None

        if self.character_type == "Fire":
            spellTypes = NewSpells.fireTierOne

        if self.character_type == "Water":
            spellTypes = NewSpells.waterTierOne

        if self.character_type == "Earth":
            spellTypes = NewSpells.earthTierOne

        if self.character_type == "Wind":
            spellTypes = NewSpells.windTierOne

        while True:
            print("You grew a level, Choose a new spell to use on your journey!")
            spellNum = 1
            for spell in spellTypes:
                if not self.character.has_attack(spell):
                    print(str(spellNum) + ". " + spell.name)
                    print("Your learned " + spell.name)
                    spellNum += 1

            new_spell = spellTypes[int(input("\nYour choice: ")) - 1]
            print(new_spell.name + "-" + new_spell.desc)
            if int(input("Is this the spell you want? (1.yes 2.no)")) != 1:
                continue
            else:
                self.character.learn_attack(new_spell)
                break

    def __getattr__(self, item):
        if hasattr(self.character, item):
            return self.character.__getattribute__(item)
