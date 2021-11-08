from random import randint

class Warrior():
    def __init__(self, name):
        self.health = 100
        self.damage = 20
        self.name = name

    def kick_enemy(self, obj):
        obj.health -= self.damage


if __name__ == '__main__':
    War1 = Warrior('War1')
    War2 = Warrior('War2')

    while (War1.health > 0 and War2.health > 0):
        rand_dmg = randint(1, 2)
        if rand_dmg == 1:
            war_beat = War1
            war_beated = War2
        else:
            war_beat = War2
            war_beated = War1

        war_beat.kick_enemy(war_beated)
        print('Атакует ' + str(war_beat.name) + '! У его противника, ' + war_beated.name + ', осталось ' + str(war_beated.health) + ' жизней')

    if War1.health == 0:
        print('ПОБЕДИЛ War2')
    else:
        print('ПОБЕДИЛ War1')

