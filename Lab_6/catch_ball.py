import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
global width, height, text_range
width = 1700
height = 900
text_range = 500
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():

    global x, y, r
    r = randint(30, 50)
    x = randint(0 + r, width - text_range - r)
    y = randint(0 + r, height - r)

    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

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

        if vector_length(guess_vec, (x, y)) <= r:
            score_count += 1
        else:
            print('LOOOSER!!!')

screen.fill(BLACK)

pygame.display.update()
clock = pygame.time.Clock()

finished = False

score_count = 0
guess_vec = (0, 0)


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                guess_vec = pygame.mouse.get_pos()

                if vector_length(guess_vec, (x, y)) <= r:
                    score_count += 1
                else:
                    print('LOOOSER!!!')



    new_ball()

    draw_print(screen, GREEN, (width - text_range, 0), (width, height), f"SCORE:" + str(score_count))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
