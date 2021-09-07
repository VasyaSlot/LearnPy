import pygame
import numpy as np
from pygame.draw import *

def mirror_image_2D(coords_need_change, coords_of_center_symmetry = 500 ):
        list_coords_need_change = np.empty((0, 2))
        if np.shape(coords_need_change)[0] == 1:
            for coords in (coords_need_change):
                x_coords_new = coords_of_center_symmetry + abs(coords[0] - coords_of_center_symmetry)
                list_coords_need_change = np.vstack((list_coords_need_change, [x_coords_new, coords[1]]))
                return list_coords_need_change
        else:
            for coords in (coords_need_change):
                x_coords_new = coords_of_center_symmetry + abs(coords[0] - coords_of_center_symmetry)
                list_coords_need_change = np.vstack((list_coords_need_change, [x_coords_new, coords[1]]))
            return list_coords_need_change

#Инициализация библиотеки
pygame.init()

#создадим набор цветов (красный, зеленый, синий, желтый, черный, белый)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HUMAN = (255, 223, 196)
BROWN = (210, 105, 30)
MAGENTA = (255, 0, 255)


#Значение FPS для блавноого
FPS = 30
#Создание окна в котором будут картинки
screen = pygame.display.set_mode((2000, 1000))
screen.fill(WHITE)

#Создаем кулаки
coords_left_punch_1 = np.array([[90, 100]])
circle(screen, HUMAN, coords_left_punch_1[0], 50)
circle(screen, HUMAN, mirror_image_2D(coords_left_punch_1, coords_of_center_symmetry=500)[0], 50)
#Создаем кулаки второго чела
circle(screen, HUMAN, mirror_image_2D(coords_left_punch_1, coords_of_center_symmetry=1000)[0], 50)
circle(screen, HUMAN, mirror_image_2D(mirror_image_2D(coords_left_punch_1, coords_of_center_symmetry=500), coords_of_center_symmetry=1000)[0], 50)

#Создаем руки
coords_arms = np.array([[79, 144], [106, 140], [287, 582], [263, 594]])
polygon(screen, HUMAN, coords_arms)
polygon(screen, HUMAN, mirror_image_2D(coords_arms, coords_of_center_symmetry=500))
polygon(screen, HUMAN, mirror_image_2D(coords_arms, coords_of_center_symmetry=1000))
polygon(screen, HUMAN, mirror_image_2D(mirror_image_2D(coords_arms, coords_of_center_symmetry=500), coords_of_center_symmetry=1000))

#Создаем тело
coords_body = np.array([[500, 775]])
circle(screen, YELLOW, coords_body[0], 220)

#Создаем тело 2 чела
circle(screen, YELLOW, mirror_image_2D(coords_body, coords_of_center_symmetry=1000)[0], 220)

#Создаем плечи
coords_shoulders = np.array([[230, 613], [318, 566], [364, 617], [319, 695], [236, 671]])
polygon(screen, YELLOW, coords_shoulders)
polygon(screen, BLACK, coords_shoulders, 1)

polygon(screen, YELLOW, mirror_image_2D(coords_shoulders, coords_of_center_symmetry=500))
polygon(screen, BLACK, mirror_image_2D(coords_shoulders, coords_of_center_symmetry=500), 1)

#Создаем плечи 2 чела
polygon(screen, YELLOW, mirror_image_2D(coords_shoulders, coords_of_center_symmetry= 1000))
polygon(screen, BLACK, mirror_image_2D(coords_shoulders, coords_of_center_symmetry= 1000), 1)

polygon(screen, YELLOW, mirror_image_2D(mirror_image_2D(coords_shoulders, coords_of_center_symmetry=500), coords_of_center_symmetry= 1000))
polygon(screen, BLACK, mirror_image_2D(mirror_image_2D(coords_shoulders, coords_of_center_symmetry=500), coords_of_center_symmetry= 1000), 1)

#Создаем лицо
coords_face = np.array([[500, 420]])
circle(screen, HUMAN, coords_face[0], 200)

#Создаем лицо 2 чела
circle(screen, HUMAN, mirror_image_2D(coords_face, coords_of_center_symmetry=1000)[0], 200)


#Создаем глаза
coords_eyes = np.array([[410, 390]])
circle(screen, BLUE, coords_eyes[0], 30)
circle(screen, BLUE, mirror_image_2D(coords_eyes, coords_of_center_symmetry = 500)[0], 30)

#Создаем глаза 2 чела
circle(screen, BLUE, mirror_image_2D(coords_eyes, coords_of_center_symmetry=1000)[0], 30)
circle(screen, BLUE, mirror_image_2D(mirror_image_2D(coords_eyes, coords_of_center_symmetry = 500), coords_of_center_symmetry=1000)[0], 30)

#Создаем зрачки
coords_ineyes = np.array([[405, 390]])
circle(screen, BLACK, coords_ineyes[0], 10)
circle(screen, BLACK, mirror_image_2D(coords_ineyes, coords_of_center_symmetry = 500)[0], 10)

#Создаем зрачки 2 чела
circle(screen, BLACK, mirror_image_2D(coords_ineyes, coords_of_center_symmetry=1000)[0], 10)
circle(screen, BLACK, mirror_image_2D(mirror_image_2D(coords_ineyes, coords_of_center_symmetry = 500), coords_of_center_symmetry=1000)[0], 10)

#Создаем нос
coords_noose = np.array([[485, 466], [500, 488], [515, 466]])
polygon(screen, RED, coords_noose)

#Создаем нос 2 чела
polygon(screen, RED, mirror_image_2D(coords_noose, coords_of_center_symmetry=1000))

#Создаем рот
coords_mouth = np.array([[425, 530], [500, 570], [575, 530]])
polygon(screen, BROWN, coords_mouth)

#Создаем рот 2 чела
polygon(screen, BROWN, mirror_image_2D(coords_mouth, coords_of_center_symmetry=1000))

#Создаем волосы
coords_hairs = np.array([[331, 314],
                          [316, 281],
                          [355, 282],
                          [350, 239],
                          [383, 255],
                          [390, 211],
                          [425, 233],
                          [437, 192],
                          [464, 223],
                          [491, 191],
                          [517, 219],
                          [558, 200],
                          [570, 232],
                          [609, 219],
                          [614, 255],
                          [656, 244],
                          [651, 287],
                          [691, 285],
                          [675, 318],
                          [651, 287],
                          [614, 255],
                          [570, 232],
                          [517, 219],
                          [464, 223],
                          [425, 233],
                          [383, 255],
                          [355, 282]])
polygon(screen, MAGENTA, coords_hairs)

#Создаем волосы 2 чела
polygon(screen, MAGENTA, mirror_image_2D(coords_hairs, coords_of_center_symmetry=1000))

#Создаем фон для надписи
rect(screen, GREEN, (0, 0, 2000, 100))

#Создаем надпись
font1 = pygame.font.Font(None, 135)
text1 = font1.render('             PYTHON IS REALLY AMAZING', True, BLACK)
screen.blit(text1, (0, 10))

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