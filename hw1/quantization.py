import cv2
import numpy as np

def quantization(img, level):
    newimg = np.zeros((img.shape[0],img.shape[1]))
    for i in range(img.shape[0]-1):
        for j in range(img.shape[1]-1):
            newimg[i,j] = (img[i,j]/(256/level))*(255/(level-1))
    return newimg

if __name__ == '__main__':
    img = cv2.imread('75.png',0)

    level = input('Please enter the level:\n')
    while level <= 1:
        level = input('Error. Level should be larger than one.\nPlease enter the level again:\n')
    newimg = quantization(img, level)
    cv2.imwrite('test.png', newimg)
