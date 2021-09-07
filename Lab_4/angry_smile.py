import pygame
from pygame.draw import *


#создадим набор цветов (красный, зеленый, синий, желтый, черный, белый)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Инициализация библиотеки
pygame.init()
#Значение FPS для блавноого
FPS = 30
#Создание окна в котором будут картинки
screen = pygame.display.set_mode((500,500))
screen.fill(WHITE)

#Рисуем желтый круг (рожа)
circle(screen, YELLOW, (250, 250), 200)
circle(screen, BLACK, (250, 250), 200, 1)

#Рисуем красные круги (глаза) и их границы
circle(screen, RED, (150, 190), 40)
circle(screen, BLACK, (150, 190), 40, 1)
circle(screen, RED, (350, 195), 30)
circle(screen, BLACK, (350, 195), 30, 1)

#Рисуем черные круги (зрачки)
circle(screen, BLACK, (150, 190), 10)
circle(screen, BLACK, (350, 195), 10)

#Рисуем черные прямоугольники (брови и рот)
polygon(screen, BLACK, [(76,92), (86, 75), (235, 160), (225, 167)])
polygon(screen, BLACK, [(300,173), (288, 164), (358, 106), (370, 120)])

polygon(screen, BLACK, [(160, 375), (160, 360), (340, 360), (340, 375)])





#Обновление экрана, чтобы появились нарисованнные вещи
pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    #print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        #if pygame.mouse.get_pressed():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(pygame.mouse.get_pos())

pygame.quit()