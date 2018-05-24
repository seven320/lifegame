#encoding:utf-8

import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()
    screen=pygame.display.set_mode((300,200))
    pygame.display.set_caption("GAME")

    while(1):
        screen.fill((0,0,0))
        pygame.draw.line(screen,(0,95,0),(0,0),(80,80),5)
        pygame.display.update()
        #event
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()


if __name__=="__main__":
    main()
