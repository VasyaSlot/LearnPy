import math

class Snow():
    def __init__(self, n_snwf):
        self.snowflakes_number = n_snwf

    def __add__(self, other):
        self.snowflakes_number += other

    def __sub__(self, other):
        self.snowflakes_number -= other

    def __mul__(self, other):
        self.snowflakes_number *= other

    def __truediv__(self, other):
        self.snowflakes_number //= other

    def makeSnow(self, n_snowflake_row):
        n_all = math.ceil(self.snowflakes_number / n_snowflake_row)
        for i in range(n_all):
            if self.snowflakes_number - i * n_snowflake_row >= n_snowflake_row:
                print('*' * (n_snowflake_row))
            else:
                print('*' * (self.snowflakes_number - i * n_snowflake_row))


if __name__ == '__main__':

    s1 = Snow(13)
    s1 / 2
    s1.makeSnow(5)