from Multiplayer import IO
from functools import partial


class Merchant:

    def __init__(self, items_list,
                 greeting="Hello. Are you looking to buy or sell?",
                 sales_pitch="Here are the goods I have to sell.",
                 goodbye="Goodbye."):
        self.items_list = items_list
        self.greeting = greeting
        self.sales_pitch = sales_pitch
        self.goodbye = goodbye

    def greet(self, player):
        print(self.greeting)
        print("1. Buy")
        print("2. Sell")
        print("3. Goodbye")
        sellbuy_chosen_num = int(IO.get_input(player.player_num, "Your choice: ",
                                           partial(IO.check_num_in_range,
                                                   minimum=1,
                                                   maximum=3)))
        if sellbuy_chosen_num == 1:
            self.sell_items_to(player)
            self.greet(player)
        elif sellbuy_chosen_num == 2:
            self.buy_items_from(player)
            self.greet(player)
        else:
            print(self.goodbye)

    def buy_items_from(self, player):
        print("What do you have to sell?")
        item_no = 0
        item_chosen = None
        item_chosen_num = 0
        while True:
            while item_chosen is None:
                for item in player.items:
                    item_no += 1
                    print(str(item_no) + ". " + item.name)
                print(str(item_no+1) + ". Goodbye")
                item_chosen_num = int(IO.get_input(player.player_num, "Your choice: ",
                                                   partial(IO.check_num_in_range,
                                                           minimum=1,
                                                           maximum=len(player.items) + 1)))

                if item_chosen_num == len(player.items)+1:
                    break

                item_chosen = player.items[item_chosen_num-1]
                if IO.get_input(0, "Sure, I can give ya " + str(item_chosen.value) + " gold for that. Sound good? (y/n)",
                                partial(IO.check_in_list, list_data=["y", "n"])) == "n":
                    print("Okay, fine, no deal...")
                    continue
                    
                print("Sold!")
                player.items.remove(item_chosen)
                player.money += item_chosen.value
                print("You now have " + str(player.money) + " gold!")

            if item_chosen_num == len(player.items)+1 or IO.get_input(0, "would you like to sell anything else? (y/n)",
                            partial(IO.check_in_list, list_data=["y", "n"])) == "n":
                break

    def sell_items_to(self, player):
        print(self.sales_pitch)
        item_chosen_num = 0

        while True:
            print("You have " + str(player.money) + " gold.")
            item_chosen = None
            item_chosen_num = 0
            while item_chosen is None:
                item_no = 0
                for item in self.items_list:
                    item_no += 1
                    print(str(item_no) + ". " + item.name + " - " + str(item.value))
                print(str(item_no+1) + ". Goodbye")
                item_chosen_num = int(IO.get_input(player.player_num, "Your choice: ",
                                                   partial(IO.check_num_in_range,
                                                           minimum=1,
                                                           maximum=len(self.items_list)+1)))
                if item_chosen_num == len(self.items_list)+1:
                    break

                item_chosen = self.items_list[item_chosen_num-1]
                if player.money < item_chosen.value:
                    print("You don't have enough money for that!")
                    item_chosen = None
                    continue
                else:
                    print("Sure, here's your " + item_chosen.name + "! (cha-ching)")
                    player.items.append(item_chosen)
                    player.money -= item_chosen.value
                    print("You now have " + str(player.money) + " gold.")

            if item_chosen_num == len(self.items_list)+1 or IO.get_input(0, "Would you like anything else? (y/n)",
                                                                partial(IO.check_in_list, list_data=["y", "n"])) == "n":
                break