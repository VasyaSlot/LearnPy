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


def draw_man(scr, coord_min, coord_max, body_color, head_color, shoulder_color, arm_color, hair_color):
    '''

    :param scr: screen where draw
    :param coord_min: min coords of area where man draw
    :param coord_max: max coords of area where man draw
    :param body_color: color of body
    :param head_color: color of head
    :param shoulder_color: color of shoulder
    :param arm_color: color of arm
    :param hair_color: color of head
    :return:
    '''
    x_center = 0.5 * (coord_min[0] + coord_max[0])
    y_center = 0.5 * (coord_min[1] + coord_max[1])
    width_man = abs(coord_max[0] - coord_min[0])
    height_man = abs(coord_max[1] - coord_min[1])

    body_coords = (x_center, coord_max[1])
    body_size = 0.4 * height_man
    draw_body(scr, body_coords, body_size, body_color)

    head_coords = (x_center, coord_max[1] - 1.5 * body_size)
    draw_head(scr, head_coords, 0.8 * body_size, head_color)

    left_arm_coords_start = (body_coords[0] - 2/3 * body_size, body_coords[1] - 2/3 * body_size)
    left_arm_coords_end = (coord_min[0] + 0.1 * width_man, coord_min[1])
    draw_arm(scr, left_arm_coords_start, left_arm_coords_end, shoulder_color, arm_color)

    right_arm_coords_start = (body_coords[0] + 2 / 3 * body_size, body_coords[1] - 2 / 3 * body_size)
    right_arm_coords_end = (coord_max[0] - 0.1 * width_man, coord_min[1])
    draw_arm(scr, right_arm_coords_start, right_arm_coords_end, shoulder_color, arm_color)

    draw_hair(scr, head_coords, 0.8 * body_size, hair_color)

def turn_point_arnd_center(point_turn_angle, start_coords, center_coords):

    return [math.cos(point_turn_angle) * (start_coords[0] - center_coords[0]) -
             math.sin( point_turn_angle) * (start_coords[1] - center_coords[1]) +
             center_coords[0],
            math.sin(point_turn_angle) * (start_coords[0] - center_coords[0]) +
             math.cos(point_turn_angle) * (start_coords[1] - center_coords[1]) +
             center_coords[1]]


def draw_hair(scr, center_head_coords, head_radius, hair_color):
    hair_start_coords = (center_head_coords[0] - math.cos(math.pi / 6) * head_radius,
                         center_head_coords[1] - math.sin(math.pi / 6) * head_radius)
    hair_angle = 120
    hair_size = head_radius * 0.2
    hairs_number = int(2 * math.pi * head_radius / 360 * hair_angle / hair_size)
    turn_angle = hair_angle / hairs_number * math.pi / 180
    L_center = head_radius + 3 ** 0.5 / 6 * hair_size
    L_vertice = head_radius + 3 ** 0.5 / 2 * hair_size
    print(L_vertice, L_center)
    for i in range(hairs_number + 1):
        center_bot_triangle_coords = turn_point_arnd_center(i * turn_angle, hair_start_coords, center_head_coords)

        proection_vec = [(center_bot_triangle_coords[0] - center_head_coords[0]) /
                         vector_length(center_head_coords, center_bot_triangle_coords),
                        (center_bot_triangle_coords[1] - center_head_coords[1]) /
                         vector_length(center_head_coords, center_bot_triangle_coords)]

        triangle_center_coords = [L_center * proection_vec[0] + center_head_coords[0],
                                    L_center * proection_vec[1] + center_head_coords[1]]
        triangle_top_vertice_coords = [L_vertice * proection_vec[0] + center_head_coords[0],
                                    L_vertice * proection_vec[1] + center_head_coords[1]]

        polygon(scr, hair_color, right_triangle_coords(triangle_center_coords, triangle_top_vertice_coords))

def vector_length(vec1, vec2):
    return ((vec2[0] - vec1[0]) ** 2 + (vec2[1] - vec1[1]) ** 2) ** 0.5

def right_triangle_coords(center_triangle_coords, vertice_coords):
    triangle_turn_angle = 360 / 3 * math.pi / 180
    return [turn_point_arnd_center(i * triangle_turn_angle, vertice_coords, center_triangle_coords)
            for i in range(3)]




def draw_right_pentagon(pentagon_centr_coords, pentagon_radius):
    random_angle = randint(0, 180) * math.pi / 180

    random_start_point = (pentagon_centr_coords[0] + pentagon_radius * math.cos(random_angle),
                          pentagon_centr_coords[1] + pentagon_radius * math.sin(random_angle)
                          )

    pentagon_angle = 360 / 5 * math.pi / 180
    return [turn_point_arnd_center(i * pentagon_angle, random_start_point, pentagon_centr_coords)
            for i in range(5)]


def draw_arm(scr, start_point, end_point, shirt_color, arm_color):
    size_punch = 50
    draw_punch(screen, end_point, size_punch, arm_color)

    line(scr, arm_color, start_point, end_point, size_punch)

    pentagon_coords = draw_right_pentagon(start_point, 1.5 * size_punch)

    polygon(scr, shirt_color, pentagon_coords)
    polygon(scr, BLACK, pentagon_coords, 1)


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


def draw_print(scr, color_print, min_coords, max_coords, text_of_print):

    rect(scr, color_print, (min_coords[0], min_coords[1], max_coords[0], max_coords[1]))

    # Создаем надпись
    font1 = pygame.font.Font(None, 125)
    text1 = font1.render('             PYTHON IS REALLY AMAZING', True, BLACK)
    screen.blit(text1, (0, 10))

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

#Рисуем человека
draw_man(screen, (0, 0.1 * height), (0.5 * width, height), YELLOW, HUMAN, YELLOW, HUMAN, RED)

#Рисуем 2го человекаа
draw_man(screen, (0.5 * width, 0.1 * height), (width, height), GREEN, HUMAN, GREEN, HUMAN, MAGENTA)

#Рисуем принт с надписью
draw_print(screen, GREEN, (0, 0), (width, 0.1 * height), 'PYTHON IS REALLY AMAZING')

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