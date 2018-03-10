from characters.Enemies import *
from Battle import *
from adventures.Potions import *
from functools import partial
from adventures.Adventures import Adventure
from adventures.Clues import *

startJourney = True


class Adventure1:

    def __init__(self, players):
        self.players = players

        map_data = [[self.step1, self.camp, self.empty],
                    [self.empty, None, self.empty],
                    [self.camp, self.empty, self.dragon_fight],
                    [self.zombieRat_fight, self.empty, self.empty],
                    [self.camp, self.empty, None],
                    [None, self.camp, self.empty],
                    [self.turantula_fight, self.empty, self.empty],
                    [None, self.empty, None],
                    [self.camp, self.empty, self.giantSquid_fight]]

        self.adventure = Adventure(self.players, map_data, 0, 0)
        self.adventure.start()

    def empty(self):
        IO.print_text(
            "This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

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

                IO.get_input(0, "There's no turning back now! Keep your eyes open, this forest is filled with "
                                "creatures that will not be too happy about you being on their land.")
                IO.print_text("")
                self.adventure.mark_visited()

    def camp(self):
        IO.print_text("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
        IO.print_text("")
        time.sleep(1)
        self.item_loot()
        self.find_clues()

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
            IO.print_text("There are no items here, Let's see if we can find any clues.")

    def find_clues(self):
        clues = [clue1, clue2, clue3, clue4]
        find = random.randint(1, 8)

        if find <= 4 and self.adventure.already_visited() is False:
            IO.print_text("You found a clue! You may need this at some point.")
            clue = clues[find - 1]()
            IO.print_text(clue.name + ": " + clue.desc)
            self.players[0].clues.append(clue)
            self.adventure.mark_visited()

        elif self.adventure.mark_visited():
            IO.print_text("We already found all the clues we could here!")
        else:
            IO.print_text("There doesn't seem to be any clues!")

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
            self.find_clues()
            self.adventure.mark_visited()

        else:
            IO.print_text("The slain Mountain Dragon lies in the middle of the camp.")
            IO.print_text("The wind blows steadily from the mountains to the East, but there is nothing else here.")

    def turantula_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("There is a huge turantula in this camp! OMG kill it!!!!!")
            time.sleep(2)
            IO.print_text("")
            Battle(self.players, TerrifyingTurantula())
            IO.print_text("")
            IO.get_input(0, "Wow that was a huge spider, I really hope we don't see another one of those!")
            IO.print_text("")
            self.item_loot()
            self.find_clues()
            self.adventure.mark_visited()

        else:
            IO.print_text("That nasty spider is still laying here, why did we come back here?")
            IO.print_text("This camp is completely empty, no need to look around again and be near this spider!")

    def zombieRat_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("That is one big rat, it looks like it should be dead.  Its a ZOMBIE!!!")
            time.sleep(2)
            IO.print_text("")
            Battle(self.players, ZombieRat())
            IO.print_text("")
            IO.get_input(0, "Where did a zombie rat come from? that was so wierd!")
            IO.print_text("")
            self.item_loot()
            self.find_clues()
            self.adventure.mark_visited()

        else:
            IO.print_text("The blood from the zombie rat is here but the rat is gone! we must not have killed it!")
            IO.print_text("We've searched this camp as much as we could, lets go before that rat comes back.")

    def giantSquid_fight(self):
        if self.adventure.already_visited() is False:
            IO.print_text("What is that coming out of the water? NO! its a giant squid!!!")
            time.sleep(2)
            IO.print_text("")
            Battle(self.players, GiantSquid())
            IO.print_text("")
            IO.get_input(0, "That squid almost had us! And you wanted to take a boat!")
            IO.print_text("")
            self.item_loot()
            self.find_clues()
            self.adventure.mark_visited()

        else:
            IO.print_text("Whats that smell? Smells like rotten fish! oh its that squid!")
            IO.print_text("If you want to look around go for it, ")
