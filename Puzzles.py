import random


class Riddle:
    def __init__(self, answer, clues):
        self.answer = answer
        self.clues = clues

    def get_rand_clue(self):
        return self.clues[random.randint(0, len(self.clues)-1)]
