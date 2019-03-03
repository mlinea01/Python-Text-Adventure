from Battle import *
from adventures.Forest.ForestEvents.BridgeEvent import BridgeEvent, BridgeResults
from adventures.Forest.ForestEvents.FruitEvent import FruitEvent
from items.Potions import *
from functools import partial
from adventures.Adventures import Adventure
from adventures.Forest.Traps import *
from adventures.Puzzles import Riddle
from adventures.Forest.Enemies import *
import threading
from time import sleep
from adventures.Merchant import Merchant
import csv

startJourney = True


class Adventure1:

    def __init__(self, players):
        self.players = players

        adventure_data_file = open("forestAdventureData.csv", "rt", encoding="utf-8")
        adventure_data_reader = csv.reader(adventure_data_file)
        adventure_data = []
        for data in adventure_data_reader:
            adventure_data.append(data)

        map_data = [[self.step1,                           partial(self.random_fight, 3, 1, 80),    self.hit_trap],
                    [partial(self.random_fight, 4, 4, 80),     None,                                self.empty],
                    [self.camp,                            self.empty,                          self.turantula_fight],
                    [self.zombieRat_fight,                 self.hit_trap,                       self.empty],
                    [self.camp,                            self.forest_merchant,                None],
                    [None,                                 self.camp,                           self.empty],
                    [self.turantula_fight,                 self.empty,                          self.empty],
                    [None,                                 self.empty,                          None],
                    [self.camp,                            self.hit_trap,                       self.turantula_fight]]

        self.riddle = Riddle("mailbox", ["I start with M",
                                         "I end with X",
                                         "I have a never ending amount of letters"])
        self.riddle2 = Riddle("coin", ["I have a head", "I don't have a body", "I have a tail"])

        self.traps = [Hole(), Net(), BarbedWire(), BearTrap()]

        self.adventure = Adventure(self.players, adventure_data, self, 0, 0)
        self.adventure.start()

    def random_fight(self, difficulty=3, max_diff=10, chance=100):
        if random.randint(0,100) < chance:
            enemies = EnemyGen.get_random_enemies(difficulty, max_diff)
            if Battle().start(self.players, enemies):
                print("")
                input("Whew we made it out alive!")
                print("")
                self.adventure.mark_visited()

        if self.adventure.already_visited():
            self.item_loot()
            self.adventure.mark_visited()
        else:
            input("Looks like this place has been ransacked...")

    def get_primary_player(self, players):
        result = 0
        for player in players:
            if player.hp > 0:
                return result
            else:
                result += 1

    def forest_merchant(self):
        print("A merchant stands in a cozy hut in a shaded area. You go inside...")
        merchant = Merchant(items_list=[HealthPotion(), ManaPotion()],
                            greeting="The forest smiles upon us and provides us with bounty.",
                            sales_pitch="Perhaps these will give you sustenance. What would you like?",
                            goodbye="Farewell, and beware.")
        merchant.greet(self.players[0])

    def empty(self):
        print(
            "This area is empty. Fred wasn't sure what to put here, but wanted to put something as a proof of concept.")

    def step1(self):
        if self.adventure.already_visited():
            print("You have returned to the start!")
        else:
            print("Now that you have completed your training, we can begin our first adventure!")
            print("This is exciting!")
            start = input("Are you ready to go? (yes or no)")
            print("")

            if start == "yes":
                print("A long time ago, in a mythical land...It is up to you to find those responsible and take"
                              " them down!")
                print("You must begin your journey through the enchanted forest, but be careful! It's not as "
                              "glamorous as it sounds!")

                input("Press enter to start your journey in the enchanted forest!")
                print("")

                input("There's no turning back now! Keep your eyes open, this forest is filled with "
                                "creatures that will not be too happy about you being on their land.")
                print("")
                self.adventure.mark_visited()

    def camp(self):
        print("Look! There is a camp up ahead, Let's check it out and see if we can find any clues!")
        print("")
        time.sleep(1)
        self.item_loot()
        self.find_clues()

    def item_loot(self):
        potions = [HealthPotion, ManaPotion, SpeedPotion, DamagePotion]
        search = random.randint(1, 8)

        if search <= 4 and self.adventure.already_visited() is False:
            print("You found an item!")
            item = potions[search - 1]()
            print("You found a " + item.name)
            self.players[self.get_primary_player(self.players)].items.append(item)
            self.adventure.mark_visited()

        elif self.adventure.already_visited():
            print("The place has been ransacked! Looks like there's nothing left.")
        else:
            print("There are no items here, Let's see if we can find any clues.")

    def find_clues(self):
        find = random.randint(1, 8)

        if find <= 4 and self.adventure.already_visited() is False:
            print("You found a clue! You may need this at some point.")
            clue = self.riddle.get_rand_clue()
            print("Clue: " + clue)
            self.players[self.get_primary_player(self.players)].clues.append(clue)
            self.adventure.mark_visited()

        elif self.adventure.mark_visited():
            print("We already found all the clues we could here!")
        else:
            print("There doesn't seem to be any clues!")

    def hit_trap(self):
        if self.adventure.already_visited() is False:
            trap = self.traps[random.randint(0, 3)]
            self.activePlayers = copy(self.players)
            TargetFilters.target_filter_isAlive(self.activePlayers)

            for player in self.players:
                threading.Thread(target=self.player_hit_by_trap, args=[player, trap]).start()
        else:
            print("Theres that trap you got caught in! Let's not do that again!")

        while len(self.activePlayers) > 0:
            sleep(0.5)

    def player_hit_by_trap(self, player, trap):
        jump = input("Theres a " + trap.name + ", Type 'jump' to avoid the trap!!!!!!!!!")
        print(" ")
        if jump != "jump":
            print(trap.desc, player.player_num)
            player.hit_by(trap)
            time.sleep(2)
            self.adventure.mark_visited()
        else:
            print("You avoided the trap! I almost peed my pants!", player.player_num)
        self.adventure.mark_visited()
        self.activePlayers.remove(player)

    def turantula_fight(self):
        if self.adventure.already_visited() is False:
            print("There is a huge turantula in this camp! OMG kill it!!!!!")
            time.sleep(2)
            print("")
            if Battle().start(self.players, TerrifyingTurantula()):
                print("")
                input("Wow that was a huge spider, I really hope we don't see another one of those!")
                print("")
                self.item_loot()
                self.find_clues()
                self.adventure.mark_visited()

        else:
            print("That nasty spider is still laying here, why did we come back here?")
            print("This camp is completely empty, no need to look around again and be near this spider!")

    def zombieRat_fight(self):
        if self.adventure.already_visited() is False:
            print("That is one big rat, it looks like it should be dead.  Its a ZOMBIE!!!")
            time.sleep(2)
            print("")
            if Battle().start(self.players, ZombieRat()):
                print("")
                input("Where did a zombie rat come from? that was so wierd!")
                print("")
                self.item_loot()
                self.find_clues()
                self.adventure.mark_visited()

        else:
            print("The blood from the zombie rat is here but the rat is gone! we must not have killed it!")
            print("We've searched this camp as much as we could, lets go before that rat comes back.")

    def venusFlyTrap_fight(self):
        if self.adventure.already_visited() is False:
            print("ACK! There's something touching my leg - it's a vine!")
            time.sleep(2)
            print("")
            if Battle().start(self.players, VenusFlyTrap()):
                print("")
                input("Whew, that plant almost made us its dinner! (Press enter to continue)")
                print("")
                self.item_loot()
                self.find_clues()
                self.adventure.mark_visited()

        else:
            print("The brutal venus fly trap is here, tunring to compost to grow more venus fly traps... weird.")

    def bridge_event(self, dir_success, dir_fail):
        if self.adventure.already_visited() is False:
            result = BridgeEvent(self.players).start_event().get_event_result()
            if result == BridgeResults.MadeItAcross:
                sleep(1)
                print("The party continues " + dir_success)
                sleep(1)
                input("Press Enter to continue.")
                self.adventure.move_players_in_dir(dir_success)
                self.adventure.player_choose_next_move = False

            elif result == BridgeResults.BridgeBroke or result == BridgeResults.RanAway:
                if result == BridgeResults.BridgeBroke:
                    self.adventure.mark_visited()
                sleep(1)
                print("The party moves back " + dir_fail)
                sleep(1)
                input("Press Enter to continue.")
                self.adventure.move_players_in_dir(dir_fail)
                self.adventure.player_choose_next_move = False
        else:
            print("The bridge still lies broken in pieces and the wind howls down the gorge.\n"
                          "Looks like there is no way across now...")
            sleep(1)
            print("The party moves back " + dir_fail)
            sleep(1)
            input("Press Enter to continue.")
            self.adventure.move_players_in_dir(dir_fail)
            self.adventure.player_choose_next_move = False

    def fruit_event(self):
        FruitEvent(self.players).start_event()
