import random
from characters.Enemies import *
from Battle import *
from adventures.Potions import *

startJourney = True


class Adventure1:

    def __init__(self, players):
        self.players = players

    def step1(self):
        from Multiplayer import GameSession
        from Multiplayer import IO
        server = GameSession.get_server()

        server.print_text("Now that you have completed your training, we can begin our first adventure!")
        server.print_text("This is exciting!")
        start = IO().get_input(server, 0, "Are you ready to go? (yes or no)")
        server.print_text("")

        if start == "yes":
            server.print_text("A long time ago, in a mythical land...It is up to you to find those responsible and take"
                              " them down!")
            server.print_text("You must begin your journey through the enchanted forest, but be careful! It's not as "
                              "glamorous as it sounds!")

        IO().get_input(server, 0, "Press enter to start your journey in the enchanted forest!")
        server.print_text("")

        while startJourney:

            def search_camp():
                potions = [HealthPotion(), ManaPotion(), SpeedPotion(), DamagePotion()]
                search = random.randint(1, 8)

                if search <= 4:
                    server.print_text("You found an item!")
                    server.print_text("You found a " + potions[search - 1].name)
                    self.players[0].items.append(potions[search - 1])

                else:
                    server.print_text("There's nothing here, let's keep moving!")

            IO().get_input(server, 0,"There's no turning back now! Keep your eyes open, this forest is filled with "
                                    "creatures that will not be too happy about you being on their land.")
            server.print_text("")

            server.print_text("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
            server.print_text("")
            enter_camp = random.randint(1, 3)

            if enter_camp == 1:
                server.print_text("There is a Mountain Dragon in the camp, Hurry, take that dragon down!")
                server.print_text("")
                Battle(self.players, MountainDragon())
                server.print_text("")
                IO().get_input(server, 0, "Woah that dragon was tough! Now that that's over lets take a look around "
                                        "this camp.")
                server.print_text("")
                search_camp()

            elif enter_camp == 2 or enter_camp == 3:
                server.print_text("This camp looks pretty quiet, lets search for clues to see what has happened here.")
                server.print_text("")
                search_camp()
