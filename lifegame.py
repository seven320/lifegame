#encoding:utf-8

import numpy as np

X=10
Y=10

a=np.zeros((X,Y))
b=np.zeros((X,Y))
print(a[0])

def update_status(x,y,a):
    count=0
    status=0
    for i in range(-1,2):
        for j in range(-1,2):
            if i==0 and j==0:pass
            else:
                周囲のカウントをしたい
                上下左右の端で定義してない空間ができるのでそこの例外条件を書く


    if a[x][y]==0 and count==3:#誕生
        status=1
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

for i in range(X):
    for j in range(Y):
        b[i][j]=update_status(i,j,a)
print(b)
