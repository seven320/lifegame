#encoding: utf-8

from PIL import Image, ImageFilter
import numpy as np
import cv2

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def main(X,Y,cell_size):
    max_size=min(X,Y)/cell_size
    IMAGE_PATH="/Users/kenkato/python/lifegame/cat.png"
    #画像読み込み-------
    # im=Image.open("/Users/kenkato/python/lifegame/cat.png")
    img=cv2.imread(IMAGE_PATH,0)
    img_gray=cv2.imread(IMAGE_PATH,cv2.IMREAD_GRAYSCALE)
    print(img.shape)
    #decide size

    #mosaic
    x,y = img_gray.shape
    img_pix = max(x,y)
    ratio=max_size/img_pix
    print("ratio:",ratio)
    img_mosaic=mosaic(img_gray,ratio)
    # cv2.imshow("mosaic",img_mosaic)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #2値化
    average = np.average(img_mosaic)
    thresh = average
    max_pixel = 255
    ret, img_dst = cv2.threshold(img_mosaic, thresh, max_pixel, cv2.THRESH_BINARY)
    #mosaic
    # img_mosaic=mosaic(img_gray_150,ratio=0.032)
    #画像表示
    print(img_dst.shape)
    life=[]
    print(len(img_dst[0]))
    for i in range(round(x*ratio)):
        for j in range(round(y*ratio)):
            cell=img_dst[i*round(1/ratio),j*round(1/ratio)]
            if cell==255:
                life.append([i,j])
    print(life)
    # cv2.imshow("normal",img_dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # new_im.show()

if __name__=="__main__":
    X,Y = 600,600
    cell_size=6
    main(X,Y,cell_size)
