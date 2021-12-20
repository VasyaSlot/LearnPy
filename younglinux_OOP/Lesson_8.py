from math import pi

class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    def __init__(self, di, hi):
        self.diam = di
        self.height = hi
        self.__dict__['area'] = self.make_area(self.diam, self.height)

    def __setattr__(self, attr, value):
        if attr == 'diam' or attr == 'height':
            self.__dict__[attr] = value
            if hasattr(self, 'diam') and hasattr(self, 'height'):
                self.__dict__['area'] = self.make_area(self.diam, self.height)
        elif attr == 'area':
            print('NELZYA!')


a = Cylinder(1, 2)
print(a.diam, a.height, a.area)
a.diam = 4.5
a.height = 3.3
print(a.diam, a.height, a.area)
# Не позволено
a.area = 100
print(a.area)