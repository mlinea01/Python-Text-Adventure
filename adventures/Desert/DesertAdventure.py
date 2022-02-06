from Battle import *
from adventures.Desert.Enemies import *
from adventures.Adventures import *
from adventures.Desert.Traps import *
from items.Potions import *
from threading import Timer
from adventures.Merchant import Merchant


class DesertAdventure:
    def __init__(self, player):
        self.player = player

        map_data = []
        self.adventure = Adventure(self.player, map_data, 0, 0)

        self.traps = [HuggingCactus(), QuickSand(), Mirage()]

    def Desert_merchant(self):
        print("You see a merchant in the distance, is that a mirage?. You approach with caution...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="Don't worry, I am as real as the heat covering this desert!",
                            sales_pitch="Perhaps these will give you sustenance. What would you like?",
                            goodbye="Farewell, and beware.")
        merchant.greet(self.player)

    def empty(self):
        print(
            "This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

    def camp(self):
        print("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
        print("")
        time.sleep(1)
        self.item_loot()

    def item_loot(self):
        potions = [HealthPotion, ManaPotion, SpeedPotion, DamagePotion]
        search = random.randint(1, 8)

        if search <= 4 and self.adventure.already_visited() is False:
            print("You found an item!")
            item = potions[search - 1]()
            print("You found a " + item.name)
            self.player.items.append(item)
            self.adventure.mark_visited()

        elif self.adventure.already_visited():
            print("The place has been ransacked! Looks like there's nothing left.")
        else:
            print("There are no items here, Let's see if we can find any clues.")

    def hit_trap(self):
        if self.adventure.already_visited() is False:
            trap = self.traps[random.randint(0, 3)]
            self.player_hit_by_trap(self.player, trap).start()
        else:
            print("Theres that trap you got caught in! Let's not do that again!")

        
    def player_hit_by_trap(self, player, trap):
        time_out=50
        timer = Timer(time_out, print, ['Times up!!!'])
        jump = input("Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!")
        timer.start()
        print(" ")
        if jump != "jump":
            print(trap.desc)
            player.hit_by(trap)
            time.sleep(2)
            self.adventure.mark_visited()
        else:
            print("You avoided the trap! I almost peed my pants!")
            timer.cancel()
        self.adventure.mark_visited()

    def antagonsticArmadillo_fight(self):
        if self.adventure.already_visited() is False:
            print("Is that a huge ball rolling around the desert? OMG IT'S AN ARMADILLO, RUN!!!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, AntagonisticArmadillo()):
                print("")
                input("Wow that armadillo had me rollin! No pun intended!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Oh god we came back to the armadillo! lets run before backup shows up!!!")
            print("If you really think you missed something, keep looking but i'm scared!")

    def chaoticCactus_fight(self):
        if self.adventure.already_visited() is False:
            print("Oh look a cactus, maybe we can get some juice i'm thirsty! OH CRAP IT'S MOVING!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, ChaoticCactus()):
                print("")
                input("Well we survived but i'm still thirsty!")
                print("")
                self.adventure.mark_visited()

        else:
            print("Well there is that cactus that tried to kill us again!")
            print("I guess we can look around a bit more, maybe we'll find some juice!")

    def tantalizingTremor_fight(self):
        if self.adventure.already_visited() is False:
            print("OMG it's a tremor!!! its tough has teeth, THIS IS MY NIGHTMORE!!!")
            time.sleep(2)
            print("")
            if Battle().start(self.player, TantalizingTremor()):
                print("")
                input("Ok, if we see one of those again I will cry!")
                print("")
                self.adventure.mark_visited()

        else:
            print("It's the tremor again...I'm not scared, you're scared!...Shut up!")
            print("I'm not so sure i want to be here.  Is it on me? i feel like it's on me!")