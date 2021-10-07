import random

import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 1
global width, height, text_range
width = 1700
height = 900
text_range = 500
screen = pygame.display.set_mode((width, height))

x = []
y = []
r = []
speed_x = []
speed_y = []
balls_color = []
shape_form = []

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def turn_point_arnd_center(point_turn_angle, start_coords, center_coords):

    return [math.cos(point_turn_angle) * (start_coords[0] - center_coords[0]) -
             math.sin( point_turn_angle) * (start_coords[1] - center_coords[1]) +
             center_coords[0],
            math.sin(point_turn_angle) * (start_coords[0] - center_coords[0]) +
             math.cos(point_turn_angle) * (start_coords[1] - center_coords[1]) +
             center_coords[1]]

def romb_coords(center_triangle_coords, vertice_coords):
    triangle_turn_angle = 360 / 4 * math.pi / 180
    return [turn_point_arnd_center(i * triangle_turn_angle, vertice_coords, center_triangle_coords)
            for i in range(4)]



def new_ball(indx):
    global x, y, r, speed_x, speed_y
    r.append(randint(30, 50))
    x.append(randint(0 + r[indx], width - text_range - r[indx]))
    y.append(randint(0 + r[indx], height - r[indx]))
    speed_x.append(random.uniform(-1, 1) * r[indx])
    speed_y.append(random.uniform(-1, 1) * r[indx])

    balls_color.append(COLORS[randint(0, 5)])
    shape_form.append(randint(0,1))
    if shape_form[indx] == 0:
        circle(screen, balls_color[indx], (x[indx], y[indx]), r[indx])
    else:
        polygon(screen, balls_color[indx], romb_coords([x[indx], y[indx]], [x[indx], y[indx] + r[indx]]))

def click(event):
    print(x, y, r)

def vector_length(vec1, vec2):
    return ((vec2[0] - vec1[0]) ** 2 + (vec2[1] - vec1[1]) ** 2) ** 0.5

def draw_print(scr, color_print, min_coords, max_coords, text_of_print):
    font1 = pygame.font.Font(None, 125)

    text1 = font1.render(text_of_print, True, BLACK)

    text_rect = rect(scr, color_print, (min_coords[0], min_coords[1], max_coords[0], max_coords[1]))

    scr.blit(text1, text_rect)

def event_handler_for_catch_ball(evnt):
    global score_count
    guess_vec = (0, 0)

    if evnt.button == 1:
        guess_vec = pygame.mouse.get_pos()
        for i in range(num_ball):
            if vector_length(guess_vec, (x[i], y[i])) <= r[i]:
                if shape_form[i] == 0:
                    score_count += 1
                else:
                    score_count += 2



def boundary_conditions(xcor, ycor, speed_x, speed_y, id):

    if (xcor[id] + speed_x[id]) >= width - text_range : #rignt boundary
        speed_x[id] *= -1
    if (xcor[id] + speed_x[id]) <= 0 : #left boundary
        speed_x[id] *= -1
    if (ycor[id] + speed_y[id]) >= height : #bot boundary
        speed_y[id] *= -1
    if (ycor[id] + speed_y[id]) <= 0 : #top boundary
        speed_y[id] *= -1

def new_balls_coordinate(indx):
    x[indx] += speed_x[indx]
    y[indx] += speed_y[indx]

    boundary_conditions(x, y, speed_x, speed_y, indx)

    if shape_form[indx] == 0:
        circle(screen, balls_color[indx], (x[indx], y[indx]), r[indx])
    else:
        polygon(screen, balls_color[indx], romb_coords([x[indx], y[indx]], [x[indx], y[indx] + r[indx]]))

def move_balls():
    for i in range(num_ball):
        new_balls_coordinate(i)

def create_balls(num_ball):
    for i in range(num_ball):
        new_ball(i)

screen.fill(BLACK)

pygame.display.update()
clock = pygame.time.Clock()

finished = False

score_count = 0
guess_vec = (0, 0)

num_ball = 10

create_balls(num_ball)

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_handler_for_catch_ball(event)

    screen.fill(BLACK)

    draw_print(screen, GREEN, (width - text_range, 0), (width, height), f"SCORE:" + str(score_count))

    move_balls()

    pygame.display.update()

pygame.quit()
