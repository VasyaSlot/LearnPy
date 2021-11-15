from random import  randint

class People:
    uniq_number = 1

    def __init__(self, team):
        self.uniq_id = self.uniq_number
        self.uniq_number += 1
        self.team_choice = team


class Soldiers(People):

    def follow_hero(self):
        pass


class Heroes(People):

    def __init__(self, team):
        People.__init__(self, team)
        self.lvl = 1
        self.soldiers_in_control = []

    def lvlup(self):
        self.lvl += 1


if __name__ == '__main__':
    num_team = 2
    num_soldiers = 11
    num_heroes = 2

    hero_pool = [Heroes(i) for i in range(num_team)]
    soldier_pool = []

    for i in range(num_soldiers):
        soldier_team = randint(0, num_team - 1)
        soldier = Soldiers(soldier_team)
        hero_pool[soldier_team].soldiers_in_control.append(soldier)

    print(hero_pool[0].lvl)
    print(hero_pool[1].lvl)

    print(len(hero_pool[0].soldiers_in_control))
    print(len(hero_pool[1].soldiers_in_control))


    if len(hero_pool[0].soldiers_in_control) > len(hero_pool[1].soldiers_in_control):
        hero_pool[0].lvlup()
    else:
        hero_pool[1].lvlup()

    print(hero_pool[0].lvl)
    print(hero_pool[1].lvl)





