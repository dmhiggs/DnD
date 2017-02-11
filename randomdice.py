#dice and also random rolling

#dice ...d2...d4...d6...d8...d10...d12...d20...d100

import random

class die():
    def __init__(self, side):
        self.roll = 0
        self.sides = side
        return

    def rolldie(self):
        self.roll = random.SystemRandom().randint(1, self.sides)
        return

