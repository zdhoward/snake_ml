import pygame
from pygame.locals import *
import time

WIN_WIDTH = 500
WIN_HEIGHT = 500

SIZE = 10
SPEED = 0.5

def main():
    (width, height) = (WIN_WIDTH, WIN_HEIGHT)
    screen = pygame.display.set_mode((width, height))
    #pygame.draw.rect(screen, (0,0,200), (0,0,SIZE,SIZE))
    pygame.display.flip()

    x = int((WIN_WIDTH / SIZE) / 2)
    y = int((WIN_HEIGHT / SIZE) / 2)
    tail_length = 0
    tail = []
    grow = False

    direction = "wait"

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if  event.key == K_UP:
                    direction = "up"
                elif  event.key == K_RIGHT:
                    direction = "right"
                elif  event.key == K_DOWN:
                    direction = "down"
                elif  event.key == K_LEFT:
                    direction = "left"

        if len(tail) > 0 and grow == False:
            tail.pop(0)
        tail.append((x, y))

        if direction == "up":
            y -= 1
        if direction == "right":
            x += 1
        if direction == "down":
            y += 1
        if direction == "left":
            x -= 1

        pygame.draw.rect(screen, (255,255,255), (x*SIZE,y*SIZE,SIZE,SIZE))
        pygame.display.flip()
        time.sleep(SPEED)

def display_board():
    return ""

if __name__ == "__main__":
    main()