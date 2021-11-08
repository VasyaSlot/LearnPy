from random import randrange as rnd, choice
from random import randint as rndint
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.lifetime = 0
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def boundary_conditions(self):

        if (self.x + self.vx) >= 800:  # right boundary
            self.vx *= -1
        if (self.x + self.vx) <= 0:  # left boundary
            self.vx *= -1
        if (self.y - self.vy) >= 600:  # bot boundary
            self.vy *= -1
        if (self.y - self.vy) <= 0:  # top boundary
            self.vy *= -1

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """



        self.boundary_conditions()

        self.x += self.vx
        self.y -= self.vy

        #self.vy -= 0.9999 * self.vy / abs(self.vy) * (abs(self.vy) + 2)
        #self.vx -= 0.9999 * self.vx / abs(self.vx) * (abs(self.vx))
        #print(self.vy)


    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)

        self.vx, self.vy = 0, 0

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if abs(self.x - obj.x) <= obj.r and abs(self.y - obj.y) < obj.r:
            return True
        else:
            return False


class gun():

    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():

    def __init__(self):
        self.live = 1
        self.points = 0
        self.id = canv.create_oval(50, 50, 100, 100)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(20, 50)
        color = self.color = 'red'

        self.vx = rndint(0, 10)
        self.vy = rndint(0, 10)
        #self.new_target()
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)

        self.vx, self.vy = 0, 0


    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def boundary_conditions(self):

        if (self.x + self.vx) >= 800:  # right boundary
            self.vx *= -1
        if (self.x + self.vx) <= 0:  # left boundary
            self.vx *= -1
        if (self.y - self.vy) >= 600:  # bot boundary
            self.vy *= -1
        if (self.y - self.vy) <= 0:  # top boundary
            self.vy *= -1

    def move(self):
        self.boundary_conditions()

        self.x += self.vx
        self.y -= self.vy

num_tar = 2
tars = [target() for i in range(num_tar)]

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, tars, screen1, balls, bullet
    num_hittest = num_tar
    for tar in tars:
        tar.live = 1
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    while (num_hittest > 0) or balls:
        for b in balls:
            b.move()
            b.set_coords()
            b.lifetime = 0.3
        for tar in tars:
            if tar.live == 1:
                tar.move()
                tar.set_coords()
            for b in balls:
                if b.hittest(tar) and tar.live:
                    tar.live = 0
                    tar.hit()
                    num_hittest -= 1
                if num_hittest == 0:
                    canv.bind('<Button-2>', new_game)
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    b.hit()
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='Test')
    canv.delete(gun)

    root.after(100, new_game)

def click(event):
    print(event.x, event.y)

#canv.bind('<Button-1>', click)

new_game()

root.mainloop()
