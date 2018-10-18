#encoding utf-8

import numpy as np
import time
import sys,os

import pygame
from pygame.locals import *
import core

def main():
    controller = core.MAP()
    controller.load(0)
    status = False
    button = False
    cell_size = 6
    X,Y = controller.cells.shape
    pygame.init()
    screen = pygame.display.set_mode((X*cell_size,Y*cell_size))
    pygame.display.set_caption("LIFE GAME")
    while(1):
    # for i in range(3):
        screen.fill((0,0,0))
        #vertical line
        for i in range(int(X)):
            pygame.draw.line(screen,(0,95,0),(i*cell_size,0),(i*cell_size,Y*cell_size),1)
        # horizontal line
        for j in range(int(Y)):
            pygame.draw.line(screen,(0,95,0),(0,j*cell_size),(X*cell_size,j*cell_size),1)
        #event
        for event in pygame.event.get():
            #終了用イベント
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #キー入力時
            if event.type==pygame.KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_BACKSPACE:
                    controller.cells=np.zeros((controller.cells.shape))
                if event.key==pygame.K_SPACE: status=not(status)
                if event.key==K_1: controller.load(1)
                if event.key==K_2: controller.load(2)
                if event.key==K_3: controller.load(3)
                if event.key==K_4: controller.load(4)
        x,y = np.where(controller.cells)
        for k in range(x.size):
            pygame.draw.rect(screen,(0,95,0),(y[k]*cell_size,x[k]*cell_size,cell_size,cell_size))
             #最初の２変数はx,y座標、後ろの２変数は長方形のサイズ
        pygame.display.update()
        time.sleep(0.1)
        if status == False:
            controller.cells_update()
        else:
            pass

class GUI(core.MAP):
    def __init__(self):
        self.time_skip = 0.3
        self.status = False
        #上位クラスの初期値を定義
        core.MAP.__init__(self)
#
# MAP = GUI()
# MAP.load(0)
# status = False
# button = False
# cell_size = 6
# X,Y = MAP.cells.shape
# pygame.init()
# screen = pygame.display.set_mode((X*cell_size,Y*cell_size))
# pygame.display.set_caption("LIFE GAME")
# while(1):
# # for i in range(3):
#     screen.fill((0,0,0))
#     #vertical line
#     for i in range(int(X)):
#         pygame.draw.line(screen,(0,95,0),(i*cell_size,0),(i*cell_size,Y*cell_size),1)
#     # horizontal line
#     for j in range(int(Y)):
#         pygame.draw.line(screen,(0,95,0),(0,j*cell_size),(X*cell_size,j*cell_size),1)
#     #event
#     for event in pygame.event.get():
#         #終了用イベント
#         if event.type==QUIT:
#             pygame.quit()
#             sys.exit()
#         #キー入力時
#         if event.type==pygame.KEYDOWN:
#             if event.key==K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()
#             if event.key==K_BACKSPACE:
#                 MAP.cells=np.zeros((MAP.cells.shape))
#             if event.key==pygame.K_SPACE: status=not(status)
#             if event.key==K_1: MAP.load(1)
#             if event.key==K_2: MAP.load(2)
#             if event.key==K_3: MAP.load(3)
#             if event.key==K_4: MAP.load(4)
#     x,y = np.where(MAP.cells)
#     for k in range(x.size):
#         pygame.draw.rect(screen,(0,95,0),(y[k]*cell_size,x[k]*cell_size,cell_size,cell_size))
#          #最初の２変数はx,y座標、後ろの２変数は長方形のサイズ
#     pygame.display.update()
#     time.sleep(0.1)
#     if status == False:
#         MAP.cells_update()
#     else:
#         pass
#


if __name__ == "__main__":
    main()
