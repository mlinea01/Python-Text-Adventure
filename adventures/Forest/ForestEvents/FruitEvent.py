import re
import threading
from time import sleep

from copy import copy

from Multiplayer import IO
from attacks import StatusEffects
from attacks.AttacksInfo import Attack, AttackTypes
from items.ItemsInfo import Items


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

class FruitEvent:

    def __init__(self, players):
        print("You come to a clearing in the dense forest trees, in the middle of which is a\n"
                      "beautiful willow tree. The tree is bearing fruit that looks strange, but at the\n"
                      "same time, enticingly delicious. They are plump and juicy looking with a bright\n"
                      "blue skin and dark green leaves. One of them is particularly low and one of you\n"
                      "goes to grab it...")
        sleep(7)
        print("Willow Tree: Hey! What do you think you're doing?! That's my fruit!")
        sleep(2)
        print("Willow Tree: Hmm... tell you what, if you are worthy I will give you\n"
                      "the fruit. Answer my questions to prove your heart is true. You may\n"
                      "discuss amongst yourselves, just say 'final answer' before your final answer!")
        sleep(7)
        print("Willow Tree: Ready? Then we shall begin...")
        sleep(2)

        self.players = players
        self.fruit_desc = "A delicious, juicy fruit from a magical willow tree that restores HP and Mana."
        self.fruit_effect = Attack(atkType=AttackTypes.Normal, damage=None, desc="", manaCost=0,
                                   name="Willow Tree Fruit",
                                   statusEffects=[StatusEffects.HpBoost(10), StatusEffects.manaBoost(10)])
        self.fruit_item = Items("Willow Tree Fruit", self.fruit_desc, self.fruit_effect, value=15)
        self.answer_given = None
        self.looking_for_player_input = True
        self.question_num = 0
        self.questions = ["Question 1",
                          "Question 2"]
        self.answers = [["trees"],
                        ["roots"]]

        print(self.questions[self.question_num])

    def start_event(self, ):
        for player in self.players:
            threading.Thread(target=self.player_action, args=[player]).start()

        while True:
            if self.answer_given is not None:
                if StringUtils.string_contains(self.answer_given,  self.answers[self.question_num]):
                    print("That is correct!")
                    if self.question_num == len(self.questions)-1:
                        print("Wow)
                        if len(self.players) == 1:
                            print("You have earned this fruit! Here you go...")
                        else:
                            print("You have each earned a fruit. Here you go...")
                        for player in self.players:
                            print("You have recieved a " + self.fruit_item.name + "!")
                            player.items.append(copy(self.fruit_item))
                    else:
                        self.question_num += 1
                        print("On to the next question...")
                        sleep(1)
                        self.answer_given = None
                        print(self.questions[self.question_num])
                        self.looking_for_player_input = True
                else:
                    print("That is incorrect! I knew you were not worthy! Be gone with you!")
                    return

    def player_action(self, player):
        while True:
            if self.looking_for_player_input:
                print("What would you like to say?")
                input_text = IO.get_input(player.player_num,
                                          "(type 'final answer' first to give your answer to the Willow Tree)")
                if not self.looking_for_player_input:
                    continue
                if input_text.startswith("final answer"):
                    self.answer_given = input_text
                    print(player.name + " has answered: " + input_text)
                    self.looking_for_player_input = False
                    for player in self.players:
                        IO.stop_waiting_for_input(player.player_num)
                else:
                    print(player.name + " says " + input_text)
