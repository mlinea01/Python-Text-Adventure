import csv


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

        self.print(2, 2)

    def print(self, x, y):
        x -= 1
        y -= 1
        print(self.adventure_data[x + y*self.width])
