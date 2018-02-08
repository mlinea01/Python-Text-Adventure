from attacks import BasicAttacks
from characters import CharacterInfo


# Player class used to keep track of player stats and actions
class Player(CharacterInfo.Character):
    def chooseAttack(self):
        print("Choose your attack: ")
        attack_num = 1
        chosen_attack_num = -1
        for attack in self.attacks:
            print(str(attack_num) + ". " + attack.name)
            attack_num += 1

        while chosen_attack_num < 0 or chosen_attack_num > len(self.attacks):
            chosen_attack_num = int(input("Your choice: "))-1
            if chosen_attack_num < 0 or chosen_attack_num > len(self.attacks):
                print("Please choose a valid attack number from the list!")

        return self.attacks[chosen_attack_num]


