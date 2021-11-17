from random import choice

class Creature:
    def __init__(self, atr1, atr2):
        self.attribute1 = atr1
        self.attribute2 = atr2

    def __add__(self, other):
        return Creature(choice([self.attribute1, other.attribute1]), choice([self.attribute2, other.attribute2]))

    def __str__(self):
        return 'attribute 1 is ' + str(self.attribute1) + ' and attribute 2 is ' + str(self.attribute2)


Mom = Creature('BlueEye', 'BlondHair')
Dad = Creature('BrownEye', 'BrownHair')

Child = Mom + Dad

print(Child)

