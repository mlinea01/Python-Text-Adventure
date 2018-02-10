# Player class used to keep track of player stats and actions
class Player:

    def __init__(self, name, character):
        self.character = character
        character.choose_attack = self.choose_attack
        self.race = character.name
        character.name = name

    def choose_attack(self):
        print("Choose your attack: ")
        attack_num = 1
        chosen_attack_num = -1
        for attack in self.character.attacks:
            print(str(attack_num) + ". " + attack.name)
            attack_num += 1

        while chosen_attack_num < 0 or chosen_attack_num > len(self.character.attacks):
            chosen_attack_num = int(input("Your choice: "))-1
            if chosen_attack_num < 0 or chosen_attack_num > len(self.character.attacks):
                print("Please choose a valid attack number from the list!")

        return self.character.attacks[chosen_attack_num]


