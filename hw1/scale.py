import cv2
import numpy as np 

def scale(img, width, height):
    swidth = float(img.shape[1])/float(width)
    sheight = float(img.shape[0])/float(height)
    newimg = np.zeros((height,width))

    for i in range(height-1):
        for j in range(width-1):
            x = i*sheight
            y = j*swidth
            intx = int(x)
            inty = int(y)
            t = x-intx
            u = y-inty
            if (intx + 1 == img.shape[0]) or (inty + 1 == img.shape[1]):
                newimg[i,j] = int(img[intx,inty])
            else:
                newimg[i,j] = int(img[intx,inty]*(1-t)*(1-u) + img[intx+1,inty]*(1-t)*u + img[intx+1,inty+1]*t*u + img[intx,inty+1]*t*(1-u))
    return newimg


if __name__ == '__main__':
    img = cv2.imread('75.png',0)
    #print img
    width = input('Please enter the width of img\n')
    height = input('Please enter the height of img\n')
    newimg = scale(img, width, height)

    cv2.imwrite('test.png', newimg)
