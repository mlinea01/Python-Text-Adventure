import threading
from Multiplayer import IO
from time import sleep
from copy import copy
from attacks.AttacksInfo import Attack
from attacks.AttacksInfo import AttackTypes
import enum
import re


class StringUtils:
    @classmethod
    def string_contains(cls, input_str, str_list):
        if input_str is None:
            return False
        for word in str_list:
            if cls.search_str_for_word(word)(input_str) is not None:
                return True
        return False

    @classmethod
    def get_index_string_in_list(cls, input_str, str_list):
        str_index = 0
        while str_index < len(str_list):
            s = str_list[str_index]
            if cls.search_str_for_word(s)(input_str):
                return str_index
            str_index += 1
        return None

    @classmethod
    def search_str_for_word(cls, word):
        return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search


# This class keeps track of attack types - useful for things like determining resistances to certain moves
class BridgeResults(enum.Enum):
    BridgeBroke = enum.auto()
    MadeItAcross = enum.auto()
    RanAway = enum.auto()

class PlayerBridgeStatus(enum.Enum):
    AtStart = enum.auto()
    MadeItAcross = enum.auto()

class BridgeEvent:

    def __init__(self, players):
        print("The party comes upon a clearing in the forest in which you can see a giant gorge extending\n"
                      "down for miles with a stream running at the bottom. Stretching the length of the gorge is a\n"
                      "rope bridge that looks like it's been there for ages. It looks really old and doesn't seem\n"
                      "like it can handle much weight. Nonetheless, it is the only way across.")
        self.event_active = True
        self.players = players
        for player in players:
            player.bridge_status = PlayerBridgeStatus.AtStart
        self.lock = threading.Lock()
        self.players_on_bridge = []
        self.players_falling = []
        self.players_injured = []
        self.players_dead = []
        self.players_across = []
        self.player_go_back = []
        self.result = ""
        self.fall = Attack("Bridge Fall", "You slam into the side of the gorge while clinging onto the broken bridge "
                           "as it swings down!", damage=20, atkType=AttackTypes.Normal, manaCost=0,
                           statusEffects=[])
        self.fall_death = Attack("Death Fall", "Wow, way to go.", damage=1000000, atkType=AttackTypes.Normal,
                                 manaCost=0, statusEffects=[])
        self.bridge_status = "normal"
        self.move_words_bridge = ["bridge", "across", "forward", "continue", "cross"]
        self.move_words_death = ["jump", "leap"]
        self.move_words_slow = ["stroll", "meander", "crawl"]
        self.move_words_neutral = ["go", "walk", "skip", "cartwheel"]
        self.move_words_fast = ["run", "sprint", "jog", "fast", "quick", "quickly", "swiftly", "speed"]
        self.move_words_cross = ["cross"]
        self.investigate_words = ["investigate", "look", "test", "check", "examine", "touch"]
        self.retreat_words = ["back", "leave", "away", "turn around", "flee", "retreat"]
        self.talk_words = ["say", "tell", "yell", "scream", "whisper"]
        self.dance_words = ["dance"]
        self.num_players_on_bridge = 0

    def get_event_result(self):
        return self.result

    def start_event(self):
        for player in self.players:
            threading.Thread(target=self.player_action, args=[player]).start()

        while True:
            sleep(0.5)
            if self.bridge_status == "broken" and len(self.players_falling) == 0 and len(self.players_injured) > 0:
                injured_names = ""
                injured_player_index = 0
                while injured_player_index < len(self.players_injured):
                    injured_player = self.players_injured[injured_player_index]
                    injured_names += injured_player.name
                    if injured_player_index < len(self.players_injured)-1:
                        injured_names += " and "
                    injured_player.hit_by(copy(self.fall))
                    injured_player_index += 1
                if len(self.players_injured) > 1:
                    injured_names += " climb"
                else:
                    injured_names += " climbs"
                print(injured_names + " back up after clinging onto part of the bridge as it swung down "
                                              "hard into the side of the gorge. They have some bruises to show for it.")
                self.result = BridgeResults.BridgeBroke
                return self

            elif len(self.players_across) + len(self.players_dead) == len(self.players) and \
                    len(self.players_dead) < len(self.players):
                sleep(0.5)
                print("Everyone has made it across safely! Now you may continue onwards...")
                if len(self.players_dead) > 0:
                    sleep(1)
                    print("Everyone who is still alive anyway...")
                self.result = BridgeResults.MadeItAcross
                sleep(1)
                for player in self.players:
                    IO.stop_waiting_for_input(player.player_num)
                self.event_active = False
                return self

            elif len(self.player_go_back) > 0:
                print(self.player_go_back[0].name + " looks very flustered and just runs away!")
                if len(self.players) > 1:
                    sleep(1)
                    print("Everyone else quickly runs after them.")
                if self.bridge_status == "normal":
                   self.result = BridgeResults.RanAway
                else:
                    self.result = BridgeResults.BridgeBroke
                sleep(1)
                return self

    def player_action(self, player):
        while True:
            if player.bridge_status is not PlayerBridgeStatus.MadeItAcross:
                input_text = IO.get_input(player.player_num, "What would you like to do? ")
            else:
                input_text = IO.get_input(player.player_num, "You are partying it up on the other side!\n"
                                                             "Would you like to do anything else?")

            if self.event_active is False:
                return

            is_moving_neutral = StringUtils.string_contains(input_text, self.move_words_neutral)
            is_moving_fast = StringUtils.string_contains(input_text, self.move_words_fast)
            is_moving_cross = StringUtils.string_contains(input_text, self.move_words_cross)
            talk_word_index = StringUtils.get_index_string_in_list(input_text, self.talk_words)
            move_death_index = StringUtils.get_index_string_in_list(input_text, self.move_words_death)

            if talk_word_index is not None:
                talk_word_used = self.talk_words[talk_word_index]
                what_to_say = input_text.split(talk_word_used,1)[1]
                print(player.name + " " + talk_word_used+"s '" + what_to_say + " '")

            elif StringUtils.string_contains(input_text, self.retreat_words):
                if player.bridge_status == PlayerBridgeStatus.MadeItAcross:
                    print("You start to go back over the bridge, but decide not to try your luck a "
                                  "second time...",
                                  player.player_num)
                    continue
                self.lock.acquire()
                self.player_go_back.append(player)
                self.lock.release()
                break

            elif is_moving_neutral or is_moving_fast or is_moving_cross:
                if is_moving_cross or StringUtils.string_contains(input_text, self.move_words_bridge):
                    if player.bridge_status == PlayerBridgeStatus.MadeItAcross:
                        print("You start to go back over the bridge, but decide not to try your luck a "
                                      "second time...",
                                      player.player_num)
                        continue
                    self.player_crosses(player, is_moving_fast)
                else:
                    print("Can you please be more specific?")

            elif StringUtils.string_contains(input_text, self.investigate_words):
                print("The bridge sways and creaks in the breeze.\n"
                              "This thing does NOT seem very stable!", player.player_num)

            elif move_death_index is not None:
                self.lock.acquire()
                print(player.name + " " + self.move_words_death[move_death_index]+"s into the gorge!")
                sleep(1)
                print("They yell aaaaaall the way down...")
                sleep(2)
                player.hit_by(self.fall_death)
                print("I think they're dead now.")
                sleep(1)
                print("They were so " + player.desc + ". They will be missed...")
                sleep(1)
                self.players_dead.append(player)
                self.lock.release()
                break

            elif StringUtils.string_contains(input_text, self.dance_words):
                print(player.name + " is dancing!")

            else:
                print("You cannot do that.")

    def player_crosses(self, player, is_moving_fast):
        self.lock.acquire()
        self.players_on_bridge.append(player)
        print(player.name + " steps onto the bridge and begins moving across...")
        self.lock.release()
        if len(self.players_on_bridge) >= 2:
            self.lock.acquire()
            self.bridge_status = "broken"
            sleep(0.5)
            print("The bridge ropes snap! The bridge begins to fall into the gorge below!")
            self.players_falling = copy(self.players_on_bridge)
            for player_falling in self.players_falling:
                threading.Thread(target=self.player_falls, args=[player_falling]).start()
            self.players_on_bridge = []
            self.lock.release()

        else:
            if is_moving_fast:
                sleep(3)
            else:
                sleep(5)

            self.lock.acquire()
            if self.bridge_status == "normal":
                self.players_on_bridge.remove(player)
                self.players_across.append(player)
                print(player.name + " made it across the bridge!")
                player.bridge_status = PlayerBridgeStatus.MadeItAcross
            self.lock.release()

    def player_falls(self, player):
        reaction = IO.get_input(player.player_num,
                                "Type 'run back' to get back quick!",
                                time_out=30)
        print(" ")
        self.lock.acquire()
        if reaction != "run back":
            print("You start falling! But you grab onto a piece of the bridge as it swings down and you "
                          "hit the side of the gorge!", player.player_num)
            self.players_injured.append(player)
        else:
            print(player.name + " made it back safely!")

        self.players_falling.remove(player)
        self.lock.release()
