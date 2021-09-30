import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''
    create new_ball with random coordinates (x, y) and radius (r)
    have random color
    :return:
    '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    print(x, y, r)

def vector_length(vec1, vec2):
    return ((vec2[0] - vec1[0]) ** 2 + (vec2[1] - vec1[1]) ** 2) ** 0.5

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score_count = 0

guess_vec = (0, 0)

while not finished:
    clock.tick(FPS)

    new_ball()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                guess_vec = pygame.mouse.get_pos()

    pygame.time.wait(3000)

    print(guess_vec)
    print((x, y))

    if vector_length(guess_vec, (x, y)) <= r:
        score_count += 1
    else:
        print('LOOOSER!!!')

    print(score_count)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()