#encoding:utf-8

import pygame
from pygame.locals import *
import sys,os
import numpy as np
import time

# def main_3():
#     pygame.init()
#     screen=pygame.display.set_mode((400,300))
#     pygame.display.set_caption("Test")#title bar
#
#     while(1):
#         screen.fill((0,0,0))
#         pygame.display.update()
#         #イベント処理
#         for event in pygame.event.get():
#             if event.type==QUIT:
#                 pygame.quit()
#                 sys.exit()
#
# def main_2():
#     pygame.init()
#     screen=pygame.display.set_mode((400,300))
#     pygame.display.set_caption("GAME")
#
#     while(1):
#         screen.fill((0,0,0))
#         pygame.draw.line(screen,(0,95,0), (100,0), (100,300), 1)
#         pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50),5)
#         pygame.draw.rect(screen,(0,80,0),Rect(20,20,30,40))
#         pygame.display.update()
#         #イベント処理
#         for event in pygame.event.get():
#             if event.type==QUIT:
#                 pygame.quit()
#                 sys.exit()

def cell_update(x,y,a):
    count=0
    status=0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:
                pass
            else:
                #端処理
                if x+i<0:
                    if y+j<0 or y+j>=len(a[1]):#角
                        pass
                    else:
                        if a[len(a[0])-1][y+j]==1:
                            count+=1
                elif x+i>=len(a[0]):
                    if y+j<0 or y+j>=len(a[1]):#角
                        pass
                    else:
                        if a[0][y+j]==1:
                            count+=1
                elif y+j<0:
                    if a[x+i][len(a[1])-1]==1:
                        count+=1
                elif y+j>=len(a[1]):
                    if a[x+i][0]==1:
                        count+=1
                elif a[x+i][y+j]==1:
                    count+=1
                    # print("該当カウント: x:{0} y:{1} i:{2} j:{3} count:{4}".format(x,y,i,j,count))
    # print("x:{0},y:{1},count:{2}".format(x,y,count))
    if a[x][y]==0 and count==3:#誕生
        status=1
        # print("誕生{0}_{1}".format(x,y))
    elif a[x][y]==1:
        if count==2 or count==3:#生存(維持)
            status=1
        elif count<=1:#過疎
            status=0
        elif count>=4:#過密
            status=0
        else:print("error")
    return status

def status__update(A):#A.shape
    b=np.zeros(A.shape)#なんでこれで正しく動く？場所引き渡しを行っているため
    X=len(A[0])
    Y=len(A[1])
    for i in range(X):
        for j in range(Y):
            b[i][j]=cell_update(i,j,A)
    return b

def printlife(A):#表示機能
    X,Y=A.shape
    for i in range(len(A[0])):
        for j in range(len(A[1])):
            if A[i][j]==1:
                print(" ■",end="")
            else:
                print(" □",end="")
        print("")
    print("")
    return 0

def load_life(life,A):
    if len(life)%2==0:
        for i in range(int(len(life)/2)):
            A[life[2*i]][life[2*i+1]]=1
    else:
        print("error:入力が奇数個です。")
    return A


def main():
    X=600
    Y=600
    cell_size=10
    pygame.init()
    screen=pygame.display.set_mode((X,Y))
    pygame.display.set_caption("LIFE GAME")
    A=np.zeros((int(X/cell_size),int(Y/cell_size)))
    # printlife(A)
    # b=status__update(A)
    # printlife(b)
    #グライダー銃
    life=[1,25,2,23,2,25,3,13,3,14,3,21,3,22,3,35,3,36,4,12,4,16,4,21,4,22,4,35,4,36,5,1,5,2,5,11,5,17,5,21,5,22,6,1,6,2,6,11
    ,6,15,6,17,6,18,6,23,6,25,7,11,7,17,7,25,8,12,8,16,9,13,9,14]
    # life=[0,0,1,1,1,0,0,1]
    A=load_life(life,A)
    while(1):
        screen.fill((0,0,0))
        #vertical line
        for i in range(int(X/cell_size)):
            pygame.draw.line(screen,(0,95,0),(i*cell_size,0),(i*cell_size,Y),1)
        #horizontal line
        for j in range(int(Y/cell_size)):
            pygame.draw.line(screen,(0,95,0),(0,j*cell_size),(X,j*cell_size),1)
        y,x=np.where(A==1)
        for k in range(x.size):
            # print(x[k],y[k])
            pygame.draw.rect(screen,(0,95,0),(x[k]*cell_size,y[k]*cell_size,cell_size,cell_size))
            #最初の２変数はx,y座標、後ろの２変数は長方形のサイズ
        # printlife(A)
        A=status__update(A)
        # time.sleep(10)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

if __name__=="__main__":
    main()
