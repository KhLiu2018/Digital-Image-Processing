# encoding: utf-8  
import cv2
import numpy as np

def equalize_hist(img, hist):
    m, n = img.shape[:2]
    new_grey = np.zeros(256)
    for i in range(len(hist)):
        for j in range(i):
            new_grey[i] += float(hist[j])/float(m*n)
        new_grey[i] = int(new_grey[i]*255 + 0.5)
    new_img = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            new_img[i,j] = new_grey[img[i,j]]
    return new_img

def getHist(img):
    hist = np.zeros(256)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i,j]] += 1
    return hist

def calcAndDrawHist(img):
    hist = getHist(img)
    maxVal = max(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt = int(0.9* 256) #直方图的范围限定在0-255×0.9之间     
    for h in range(256):
        intensity = int(hist[h]*hpt/maxVal)  # 计算直方图的最大值再乘以一个系数  
        ''''' 
        绘制线 
        histImg --   图像 
        (h,256)  --  线段的第一个端点 
        (h,256-intensity)  --  线段的第二个端点 
        color  --  线段的颜色 
        '''
        cv2.line(histImg, (h,256), (h,256-intensity), [255, 0, 0])
    return histImg

if __name__ == '__main__':
    img = cv2.imread('task_2.png',0)
    img_int = np.zeros((m,n), np.int)
    img_int[:,:] = img[:,:]
    hist = getHist(img_int)
    new_img = equalize_hist(img_int, hist)

    cv2.imwrite('test.png', new_img)
    new_img = cv2.imread('test.png')

    histImg = calcAndDrawHist(img)
    histnewImg = calcAndDrawHist(new_img)
    cv2.imshow("histImg", histImg)
    cv2.imshow("histnewImg", histnewImg)
    cv2.imwrite('histImg.png', histImg)
    cv2.imwrite('histnewImg.png', histnewImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
