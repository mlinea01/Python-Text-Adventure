import random
from characters.Enemies import *
from Battle import *
from characters.Player import Player
from adventures.Potions import *
from characters.CharacterInfo import *

startJourney = True


class Adventure1:

    def __init__(self, character):
        self.character = character

    def step1(self):
        print("Now that you have completed your training, we can begin our first adventure!")
        print("This is exciting!")
        start = input("Are you ready to go? (yes or no)")
        print("")

        if start == "yes":
            print("A long time ago, in a mythical land...It is up to you to find those responsible and take them down!")
            print("You must begin your journey through the enchanted forest, but be careful! It's not as glamorous\n"
                  "as it sounds!")

        input("Press enter to start your journey in the enchanted forest!")
        print("")

        while startJourney:

            def search_camp():
                potions = [HealthPotion(), ManaPotion(), SpeedPotion(), DamagePotion()]
                search = random.randint(1, 8)

                if search < 4:
                    print("You found an item!")
                    print("You found a " + str(potions[search - 1]))
                    self.character.items.append(potions[search - 1])

                else:
                    print("There's nothing here, let's keep moving!")

            input("There's no turning back now! Keep your eyes open, this forest is filled with creatures that will\n"
                  "not be too happy about you being on their land.")
            print("")

            input("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
            print("")
            enter_camp = random.randint(1, 3)

            if enter_camp == 1:
                input("There is a Mountain Dragon in the camp, Hurry, take that dragon down!")
                print()
                Battle.fight(Player, MountainDragon())
                print("")
                input("Woah that dragon was tough! Now that that's over lets take a look around this camp.")
                print("")
                search_camp()

            elif enter_camp == 2 or enter_camp == 3:
                print("This camp looks pretty quiet, lets search for clues to see what has happened here.")
                print("")
                search_camp()
