import adventures.ItemsInfo


#First Riddle
class clue1(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue One", "I start with M")

class clue2(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue Two", "and end with X")

class clue3(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue Three", "I have a never ending...")

class clue4(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue Four", "amount of letters, What am i?")

class answer1(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Answer", "Mailbox")


#Second Riddle
class clue5(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue Five", "I have a head")

class clue6(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue Six", "but no body")

class clue7(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("clue Seven", "But i do have a tail. What am i?")

class answer2(adventures.ItemsInfo.Items):
    def __init__(self):
        super().__init__("Answer", "Coin")