import pygame
from pygame.locals import *
import numpy as np
import sys

X=600
Y=600
cell_size=15
pygame.init()
screen=pygame.display.set_mode((X,Y))
pygame.display.set_caption("LIFE GAME")
while(1):
    screen.fill((0,0,0))
    A=np.zeros((int(X/cell_size),int(Y/cell_size)))
    pygame.draw.rect(screen,(0,80,0),Rect(10,10,20,20))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:                              # 閉じるボタンが押されたら終了
            pygame.quit()                                   # Pygameの終了(画面閉じられる)
            sys.exit()
