import math

class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


def str_list_to_int_list(list1):
    return [int(s) for s in list1]
def str_list_to_float_list(list1):
    return [float(s) for s in list1]


class Room:
    def __init__(self, x, y, z):
        self.width = x
        self.length = y
        self.height = z

        self.wd = []

    def full_area(self):
        return 2 * self.height * (self.width + self.length)

    def windoor_area(self):
        windoor_area = 0
        for i in self.wd:
            windoor_area += i.square
        return windoor_area

    def add_wd(self, i, n):
        print('Введите длину и ширину окна/двери №' + str(i+1) + ' из ' + str(n) + ' окон/дверей')
        l_windoor, w_windoor = str_list_to_int_list(input().split())
        print('Средняя длина одного окна/двери: ' + str(l_windoor) + ', ширина: ' + str(w_windoor))
        self.wd.append(WinDoor(l_windoor, w_windoor))

    def need_wallpaper_rul(self, wp_len, wp_width):
        wp_num = (self.full_area() - self.windoor_area()) / (wp_len * wp_width)
        print('Полная площадь комнаты: ' + str(self.full_area()) )
        print('Полезная площадь комнаты: ' + str(self.full_area() - self.windoor_area()))
        print('Для оклейки комнаты потребуется: ' + str(math.ceil(wp_num)) + ' рулонов обоев!')





if __name__ == '__main__':
    print('Введите габариты комнаты')
    l, w, h = str_list_to_float_list(input().split())
    print('Длина комнаты: ' + str(l) + ', ширина: ' + str(w) + ', высота: ' + str(h))
    r1 = Room(l, w, h)

    print('Введите число окон + дверей')
    n_windoor = int(input())
    print('Число окон + дверей: ' + str(n_windoor))

    for i in range(n_windoor):
        r1.add_wd(i, n_windoor)


    print('Введите длину и ширину одного рулона обоев')
    l_wp, w_wp = str_list_to_float_list(input().split())
    print('Длина одного рулона: ' + str(l_wp) + ', ширина: ' + str(w_wp))

    r1.need_wallpaper_rul(l_wp, w_wp)





