import csv
from Multiplayer import IO
from functools import partial


class Adventure:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.adventure_data = []
        file_data = csv.reader(open("adventure_data/adventure1.csv", "rt", encoding='utf-8-sig'))
        for row in file_data:
            for item in row:
                self.adventure_data.append(item)
                self.x += 1
            if self.width == 0:
                self.width = self.x
            self.x = 0
            self.y += 1

        self.player_x = 1
        self.player_y = 1

        while True:
            self.print(self.player_x, self.player_y)
            IO.print_text("Choose a direction")
            IO.print_text("1. North")
            IO.print_text("2. South")
            IO.print_text("3. East")
            IO.print_text("4. West")
            direction = IO.get_input(0, "Your choice: ", partial(IO.check_num_in_range, minimum=1, maximum=4))

            if direction == 1:
                self.player_y -= 1
            elif direction == 2:
                self.player_y += 1
            elif direction == 3:
                self.player_x += 1
            else:
                self.player_x -= 1


    def print(self, x, y):
        x -= 1
        y -= 1
        print(self.adventure_data[x + y*self.width])
