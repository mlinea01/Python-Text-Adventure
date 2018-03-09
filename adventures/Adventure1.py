import random
from characters.Enemies import *
from Battle import *
from adventures.Potions import *
from Multiplayer import IO
from functools import partial
from adventures.Adventures import Adventure

startJourney = True


class Adventure1:

    def __init__(self, players):
        self.players = players

        map_data = [[self.step1,  self.camp,    self.empty],
                    [self.empty,      None,      self.empty],
                    [self.camp,  self.empty,    self.dragon_fight]]

        self.adventure = Adventure(self.players, map_data, 0, 0)
        self.adventure.start()

    def empty(self):
        IO.print_text("This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

    def step1(self):
        if self.adventure.already_visited():
            IO.print_text("You have returned to the start!")
        else:
            IO.print_text("Now that you have completed your training, we can begin our first adventure!")
            IO.print_text("This is exciting!")
            start = IO.get_input(0, "Are you ready to go? (yes or no)",
                                 partial(IO.check_in_list, list_data=["yes", "no"]))
            IO.print_text("")

            if start == "yes":
                IO.print_text("A long time ago, in a mythical land...It is up to you to find those responsible and take"
                                  " them down!")
                IO.print_text("You must begin your journey through the enchanted forest, but be careful! It's not as "
                                  "glamorous as it sounds!")

                IO.get_input(0, "Press enter to start your journey in the enchanted forest!")
                IO.print_text("")


                IO.get_input(0,"There's no turning back now! Keep your eyes open, this forest is filled with "
                                        "creatures that will not be too happy about you being on their land.")
                IO.print_text("")
                self.adventure.mark_visited()

    def camp(self):
        IO.print_text("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
        IO.print_text("")
        time.sleep(1)
        self.item_loot()

    def item_loot(self):
        potions = [HealthPotion, ManaPotion, SpeedPotion, DamagePotion]
        search = random.randint(1, 8)

        if search <= 4 and self.adventure.already_visited() is False:
            IO.print_text("You found an item!")
            item = potions[search - 1]()
            IO.print_text("You found a " + item.name)
            self.players[0].items.append(item)
            self.adventure.mark_visited()

        elif self.adventure.already_visited():
            IO.print_text("The place has been ransacked! Looks like there's nothing left.")
        else:
            IO.print_text("There's nothing here, let's keep moving!")

    def dragon_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("There is a Mountain Dragon in the camp, Hurry, take that dragon down!")
            time.sleep(2)
            IO.print_text("")
            Battle(self.players, MountainDragon())
            IO.print_text("")
            IO.get_input(0, "Woah that dragon was tough! Now that that's over lets take a look around this camp.")
            IO.print_text("")
            self.item_loot()
            self.adventure.mark_visited()
        else:
            IO.print_text("The slain Mountain Dragon lies in the middle of the camp.")
            IO.print_text("The wind blows steadily from the mountains to the East, but there is nothing else here.")
