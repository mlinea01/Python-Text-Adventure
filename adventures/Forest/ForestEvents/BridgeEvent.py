from time import sleep
from attacks.AttacksInfo import Attack
from attacks.AttacksInfo import AttackTypes
from threading import Timer
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

    def __init__(self, player):
        print("The party comes upon a clearing in the forest in which you can see a giant gorge extending\n"
                      "down for miles with a stream running at the bottom. Stretching the length of the gorge is a\n"
                      "rope bridge that looks like it's been there for ages. It looks really old and doesn't seem\n"
                      "like it can handle much weight. Nonetheless, it is the only way across.")
        self.event_active = True
        self.player = player
        self.player.bridge_status = PlayerBridgeStatus.AtStart
        self.player_falling = None
        self.player_injured = None
        self.player_dead = None
        self.player_across = None
        self.player_go_back = None
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

    def get_event_result(self):
        return self.result

    def start_event(self):

        while True:
            sleep(0.5)
            if self.bridge_status == "broken" and len(self.player_falling) == 0 and len(self.player_injured) > 0:
                injured_name = self.player.name

                injured_name += " climbs"
                print(injured_name + " back up after clinging onto part of the bridge as it swung down "
                                              "hard into the side of the gorge. They have some bruises to show for it.")
                self.result = BridgeResults.BridgeBroke
                return self

            elif len(self.player_across) == 1 and len(self.player_dead) == 0:
                sleep(0.5)
                print("You have made it across safely! Now you may continue onwards...")
                self.result = BridgeResults.MadeItAcross
                sleep(1)
                self.event_active = False
                return self

            elif len(self.player_go_back) > 0:
                print("You look very flustered and just run away!")
                if self.bridge_status == "normal":
                    self.result = BridgeResults.RanAway
                else:
                    self.result = BridgeResults.BridgeBroke
                sleep(1)
                return self

    def player_action(self, player):
        while True:
            if player.bridge_status is not PlayerBridgeStatus.MadeItAcross:
                input_text = input("What would you like to do? ")

            if self.event_active is False:
                return

            is_moving_neutral = StringUtils.string_contains(input_text, self.move_words_neutral)
            is_moving_fast = StringUtils.string_contains(input_text, self.move_words_fast)
            is_moving_cross = StringUtils.string_contains(input_text, self.move_words_cross)
            move_death_index = StringUtils.get_index_string_in_list(input_text, self.move_words_death)


            if StringUtils.string_contains(input_text, self.retreat_words):
                if player.bridge_status == PlayerBridgeStatus.MadeItAcross:
                    print("You start to go back over the bridge, but decide not to try your luck a "
                                  "second time...")
                break

            elif is_moving_neutral or is_moving_fast or is_moving_cross:
                if is_moving_cross or StringUtils.string_contains(input_text, self.move_words_bridge):
                    if player.bridge_status == PlayerBridgeStatus.MadeItAcross:
                        print("You start to go back over the bridge, but decide not to try your luck a "
                                      "second time...")
                        continue
                    self.player_crosses(player, is_moving_fast)
                else:
                    print("Can you please be more specific?")

            elif StringUtils.string_contains(input_text, self.investigate_words):
                print("The bridge sways and creaks in the breeze.\n"
                              "This thing does NOT seem very stable!")

            elif move_death_index is not None:
                print(player.name + " " + self.move_words_death[move_death_index]+"s into the gorge!")
                sleep(1)
                print("You yell aaaaaall the way down...")
                sleep(2)
                player.hit_by(self.fall_death)
                break

            elif StringUtils.string_contains(input_text, self.dance_words):
                print(player.name + " is dancing!")

            else:
                print("You cannot do that.")

    #def player_crosses(self, player, is_moving_fast):
        


    def player_falls(self, player):
        time_out=30
        timer = Timer(time_out, print, ["Times up!"])
        timer.start();
        reaction = input("Type 'run back' to get back quick!")
        
        if reaction != "run back":
            print("You start falling! But you grab onto a piece of the bridge as it swings down and you "
                          "hit the side of the gorge!")
            self.player_falling = player;
        else:
            timer.cancel()
            print("You made it back safely!")
