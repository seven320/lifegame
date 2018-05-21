#encoding:utf-8

import numpy as np
import time

X=10
Y=10

A=np.zeros((X,Y))
# print(a[0])

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
                        else:
                            pass
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
    else:pass
    return status

def status__update(A):
    b=np.zeros((len(A[0]),len((A[1]))))#なんでこれで正しく動く？
    X=len(A[0])
    Y=len(A[1])
    for i in range(X):
        for j in range(Y):
            b[i][j]=cell_update(i,j,A)
    return b
# a[0][0]=1
# a[1][0]=1
# a[0][1]=1

# a[3][1]=1
# a[3][2]=1
# a[3][0]=1

A[3][4]=1
A[3][5]=1
A[4][4]=1
A[4][5]=1
A[5][6]=1
A[5][7]=1
A[6][6]=1
A[6][7]=1
print(A)
while True:
    A=status__update(A)
    time.sleep(1)
    # if b.any==False:#全滅のとき終了
    #     print(b)
    #     print("全滅のため終了")
        # break
    # elif np.all(a==b):
    #     print(b)
    #     print("変化なしのため終了")
    #     break
    print(A)
