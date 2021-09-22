import pygame
import numpy as np
import math
from random import *
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


def draw_man(scr, coord_min, coord_max):
    '''

    :param scr: screen where draw
    :param coord_min: couple coordinates (x_min, y_min)
    :param coord_max: couple coordinates (x_max, y_max)
    :return:
    '''
    x_center = 0.5 * (coord_min[0] + coord_max[0])
    y_center = 0.5 * (coord_min[1] + coord_max[1])
    width_man = abs(coord_max[0] - coord_min[0])
    height_man = abs(coord_max[1] - coord_min[1])

    body_coords = (x_center, coord_max[1])
    body_size = 0.4 * height_man
    draw_body(scr, body_coords, body_size, YELLOW)

    head_coords = (x_center, coord_max[1] - 1.5 * body_size)
    draw_head(scr, head_coords, 0.8 * body_size, HUMAN)

    left_arm_coords_start = (body_coords[0] - 2/3 * body_size, body_coords[1] - 2/3 * body_size)
    left_arm_coords_end = (coord_min[0] + 0.1 * width_man, coord_min[1])
    draw_arm(scr, left_arm_coords_start, left_arm_coords_end, GREEN, HUMAN)

    right_arm_coords_start = (body_coords[0] + 2 / 3 * body_size, body_coords[1] - 2 / 3 * body_size)
    right_arm_coords_end = (coord_max[0] - 0.1 * width_man, coord_min[1])
    draw_arm(scr, right_arm_coords_start, right_arm_coords_end, GREEN, HUMAN)

    #draw_hair()



def draw_right_pentagon(pentagon_centr_coords, pentagon_radius):
    random_angle = randint(0, 180) * math.pi / 180

    random_start_point = (pentagon_centr_coords[0] + pentagon_radius * math.cos(random_angle),
                          pentagon_centr_coords[1] + pentagon_radius * math.sin(random_angle)
                          )

    pentagon_angle = 360 / 5 * math.pi / 180

    return [[math.cos(i * pentagon_angle) * (random_start_point[0] - pentagon_centr_coords[0]) -
             math.sin(i * pentagon_angle) * (random_start_point[1] - pentagon_centr_coords[1]) +
             pentagon_centr_coords[0],
            math.sin(i * pentagon_angle) * (random_start_point[0] - pentagon_centr_coords[0]) +
             math.cos(i * pentagon_angle) * (random_start_point[1] - pentagon_centr_coords[1]) +
             pentagon_centr_coords[1]]
            for i in range(5)]


def draw_arm(scr, start_point, end_point, shirt_color, arm_color):
    size_punch = 50
    draw_punch(screen, end_point, size_punch, arm_color)

    line(scr, arm_color, start_point, end_point, size_punch)

    polygon(scr, shirt_color, draw_right_pentagon(start_point, 1.5 * size_punch))


def draw_body(scr, body_coord_center, body_size, color):
    circle(scr, color, body_coord_center, body_size)
    circle(scr, BLACK, body_coord_center, body_size, 1)


def draw_head(scr, head_coord_center, head_size, color):
    '''
    draw dace in scr
    :param scr: screen where draw
    :param coords: x,y-coords of center of face
    :param size:size of face
    :param color: color of face
    :return:
    '''
    draw_face(scr, head_coord_center, head_size, color)

    delta_eyes_coords = (0.3 * head_size, 0.3 * head_size)
    draw_eyes(scr, head_coord_center, delta_eyes_coords, 0.2 * head_size, BLUE)

    nose_size = (0.1 * head_size, 0.1 * head_size)
    draw_nose(scr, head_coord_center, nose_size, BROWN)

    mouth_size = (0.5 * head_size, 0.1 * head_size)
    mouth_center_coords = (head_coord_center[0], head_coord_center[1] + 0.4 * head_size)
    draw_mouth(scr, mouth_center_coords, mouth_size, RED)

def draw_mouth(scr, mouth_center_coords, mouth_size, mouth_color):
    mouth_coords = triangle_coords_up(mouth_center_coords, mouth_size)
    polygon(scr, mouth_color, mouth_coords)

def triangle_coords_up(triangle_center_coords, triangle_size):
    return ((triangle_center_coords[0], triangle_center_coords[1] - triangle_size[1]),
                    (triangle_center_coords[0] - triangle_size[0], triangle_center_coords[1] + triangle_size[1]),
                    (triangle_center_coords[0] + triangle_size[0], triangle_center_coords[1] + triangle_size[1]),
            )

def triangle_coords_down(triangle_center_coords, triangle_size):
    return ((triangle_center_coords[0], triangle_center_coords[1] + triangle_size[1]),
                   (triangle_center_coords[0] + triangle_size[0], triangle_center_coords[1] - triangle_size[1]),
                   (triangle_center_coords[0] - triangle_size[0], triangle_center_coords[1] - triangle_size[1]),
                   )


def draw_nose(scr, nose_center_coords, nose_size, nose_color):
    '''
    draw nose as right triangle
    :param scr: screen object where need to draw nose
    :param nose_center_coords: coords center nose
    :param nose_size: size of triangle (from center ro vertice)
    :param nose_color: color of nose
    :return:
    '''
    nose_coords = triangle_coords_down(nose_center_coords, nose_size)
    polygon(scr, nose_color, nose_coords)

def draw_face(scr, face_coords, face_size, face_color):
    circle(scr, face_color, face_coords, face_size)

def draw_eyes(scr, face_coord_center, delta_coord_eyes, eye_size, eye_color):
    coord_left_eye = (face_coord_center[0] - delta_coord_eyes[0], face_coord_center[1] - delta_coord_eyes[1])
    circle(screen, eye_color, coord_left_eye, eye_size)
    circle(screen, BLACK, coord_left_eye, 0.3 * eye_size)

    coord_right_eye = (face_coord_center[0] + delta_coord_eyes[0], face_coord_center[1] - delta_coord_eyes[1])
    circle(screen, eye_color, coord_right_eye, eye_size)
    circle(screen, BLACK, coord_right_eye, 0.3 * eye_size)


def draw_punch(scr, coords, size, color):
    '''
    draw punch in screen
    :param scr: screen where draw
    ::param coords: x,y-coords of center of punch
    :param size: size of punch
    :param color: color of punch
    :return:
    '''
    #coords_left_punch_1 = np.array([[coords[1], coords[2]]])
    circle(scr, color, (coords[0], coords[1]), size)


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

width = 2000
height = 800

#Значение FPS для блавноого
FPS = 30
#Создание окна в котором будут картинки
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)

#Создаем кулаки

#coords_left_punch_1 = np.array([[90, 100]])
#draw_punch(screen, (90, 100), 50, HUMAN)
#circle(screen, HUMAN, coords_left_punch_1[0], 50)
#draw_punch(screen, )
#circle(screen, HUMAN, mirror_image_2D(coords_left_punch_1, coords_of_center_symmetry=500)[0], 50)
#Создаем кулаки второго чела
#circle(screen, HUMAN, mirror_image_2D(coords_left_punch_1, coords_of_center_symmetry=1000)[0], 50)
#circle(screen, HUMAN, mirror_image_2D(mirror_image_2D(coords_left_punch_1, coords_of_center_symmetry=500), coords_of_center_symmetry=1000)[0], 50)
'''
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
polygon(screen, MAGENTA, mirror_image_2D(coords_hairs, coords_of_center_symmetry=1000))'''

#Рисуем человека
draw_man(screen, (0, 0.1 * height), (0.5 * width, height))


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