#encoding utf-8
#life gameの書き直し

import numpy as np
import time
import sys,os
import test

X = 50
Y = 50

class MAP():
    def __init__(self):
        self.cells = np.zeros((X,Y))
        self.next_cells = np.zeros((X,Y))

    def cells_update(self):
        self.next_cells = np.zeros((X,Y))
        for i in range(X):
            for j in range(Y):
                self.cell_update(i,j)
        self.cells = np.array(self.next_cells)

    def cell_update(self,x,y):
        cells = self.cells
        count=0
        status=0
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    pass
                else:
                    #端処理
                    if x+i<0:
                        if y+j<0 or y+j>=len(cells[1]):#角
                            pass
                        else:
                            if cells[len(cells[0])-1][y+j]==1:
                                count+=1
                    elif x+i>=len(cells[0]):
                        if y+j<0 or y+j>=len(cells[1]):#角
                            pass
                        else:
                            if cells[0][y+j]==1:
                                count+=1
                    elif y+j<0:
                        if cells[x+i][len(cells[1])-1]==1:
                            count+=1
                    elif y+j>=len(cells[1]):
                        if cells[x+i][0]==1:
                            count+=1
                    elif cells[x+i][y+j]==1:
                        count+=1
        if cells[x][y]==0 and count==3:#誕生
            status=1
            # print("誕生{0}_{1}".format(x,y))
        elif cells[x][y]==1:
            if count==2 or count==3:#生存(維持)
                status=1
            elif count<=1:#過疎
                status=0
            elif count>=4:#過密
                status=0
            else:print("error")
        self.next_cells[x][y] = status

    def load(self,map_num):
        life = []
           #life_game　図鑑　wikipedia参照　https://ja.wikipedia.org/wiki/%E3%83%A9%E3%82%A4%E3%83%95%E3%82%B2%E3%83%BC%E3%83%A0
        #グライダー銃
        if map_num == 0:
            life = [[1,25],[2,23],[2,25],[3,13],[3,14],[3,21],[3,22],[3,35],[3,36],[4,12],[4,16],[4,21],[4,22],\
        [4,35],[4,36],[5,1],[5,2],[5,11],[5,17],[5,21],[5,22],[6,1],[6,2],[6,11],[6,15],[6,17],[6,18],\
        [6,23],[6,25],[7,11],[7,17],[7,25],[8,12],[8,16],[9,13],[9,14]]

         #どんぐり
        elif map_num == 1:
            life=[[41,42],[42,44],[43,41],[43,42],[43,45],[43,46],[43,47]]

        #ダイハード
        elif map_num == 2:
            life=[[22,28],[23,22],[23,23],[24,23],[24,27],[24,28],[24,29]]

        #horizontal_line
        elif map_num == 3:
            life = []
            for i in range(Y):
                life.append([(X)//2,i])
        elif map_num == 4:
        #vertical_line
            life=[]
            for i in range(X):
                life.append([i,(X)//2])

        for i in range(len(life)):
            x,y = life[i]
            self.cells[x,y] = 1

    def print_map(self):
        x,y = self.cells.shape
        for i in range(x):
            for j in range(y):
                if self.cells[i,j] == 1:
                    print(" ■", end="")
                else:
                    print("  ", end="")
            print("")
        print("")


def main():
    MAP1 = MAP()
    MAP1.load(3)
    for i in range(10):
        print("turn:",i)
        MAP1.print_map()
        MAP1.cells_update()
        time.sleep(0.3)
        # input("")
    return 0

if __name__ == "__main__":
    main()
