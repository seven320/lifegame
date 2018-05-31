#encoding:utf-8

import pygame
from pygame.locals import *
import sys,os
import numpy as np
import time

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
    state=False
    X=600
    Y=600
    cell_size=8
    pygame.init()
    screen=pygame.display.set_mode((X,Y))
    pygame.display.set_caption("LIFE GAME")
    A=np.zeros((int(X/cell_size),int(Y/cell_size)))

    #life_game　図鑑　wikipedia参照　https://ja.wikipedia.org/wiki/%E3%83%A9%E3%82%A4%E3%83%95%E3%82%B2%E3%83%BC%E3%83%A0
    #グライダー銃
    life=[1,25,2,23,2,25,3,13,3,14,3,21,3,22,3,35,3,36,4,12,4,16,4,21,4,22,4,35,4,36,5,1,5,2,5,11,5,17,5,21,5,22,6,1,6,2,6,11
    ,6,15,6,17,6,18,6,23,6,25,7,11,7,17,7,25,8,12,8,16,9,13,9,14]
    #どんぐり
    life_2=[41,42,42,44,43,41,43,42,43,45,43,46,43,47]
    #ダイハード
    life_3=[22,28,23,22,23,23,24,23,24,27,24,28,24,29]
    #horizontal_line
    life_4=[]
    for i in range(Y//cell_size):
        life_4.append((X//cell_size)//2)
        life_4.append(i)
    #vertical_line
    life_5=[]
    for i in range(X//cell_size):
        life_5.append(i)
        life_5.append((X//cell_size)//2)
    #ブリーダー　直線型
    # life_6=[2,2,3,2,4,2,5,2,6,2,7,2,8,2,9,2,11,2,12,2,13,2,14,2,15,2,19,2,20,2,21,2,28,2,29,2,30,2,31,2,32,2,33,2,34,2,35,2,37
    # ,2,38,2,39,2,40,2,41,2]

    A=load_life(life,A)
    while(1):

        screen.fill((0,0,0))
        #vertical line
        for i in range(int(X/cell_size)):
            pygame.draw.line(screen,(0,95,0),(i*cell_size,0),(i*cell_size,Y),1)
        #horizontal line
        for j in range(int(Y/cell_size)):
            pygame.draw.line(screen,(0,95,0),(0,j*cell_size),(X,j*cell_size),1)


        for event in pygame.event.get():
            #カーソル操作時
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                x_pix,y_pix=event.pos
                A[y_pix//cell_size][x_pix//cell_size]=not(A[y_pix//cell_size][x_pix//cell_size])
            #終了用イベント
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #キー入力時
            if event.type==pygame.KEYDOWN:
                #終了機能
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key==K_BACKSPACE:
                    A=np.zeros((int(X/cell_size),int(Y/cell_size)))
                if event.key==K_1: load_life(life,A)
                if event.key==K_2: load_life(life_2,A)
                if event.key==K_3: load_life(life_3,A)
                if event.key==K_4: load_life(life_4,A)
                if event.key==K_5: load_life(life_5,A)
                if event.key==K_6:pass
                if event.key==K_7:pass
                if event.key==K_8:pass
                if event.key==K_9:pass
                #pause機能
                if event.key==pygame.K_SPACE: state=not(state)
        #cell表示
        x,y=np.where(A==1)
        for k in range(x.size):
            # print(x[k],y[k])
            pygame.draw.rect(screen,(0,95,0),(y[k]*cell_size,x[k]*cell_size,cell_size,cell_size))
            #最初の２変数はx,y座標、後ろの２変数は長方形のサイズ
        pygame.display.update()
        #running
        if state==0: A=status__update(A)
        #pause
        elif state==1:pass


if __name__=="__main__":
    main()
