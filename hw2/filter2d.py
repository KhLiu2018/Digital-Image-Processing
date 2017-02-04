# encoding: utf-8
import cv2
import numpy as np

def filter2d(img, filters):
    n = len(filters)
    img1 = np.zeros((img.shape[0]+2*(n-1),img.shape[1]+2*(n-1)))
    img1[(n-1):(n+img.shape[0]-1),(n-1):(n+img.shape[1]-1)] = img
    img2 = np.zeros((img1.shape[0]-n+1,img1.shape[1]-n+1))
    for i in range(img1.shape[0]-n+1):
    	for j in range(img1.shape[1]-n+1):
    		temp = img1[i:i+n,j:j+n]
    		img2[i,j] = matrix_filter(temp, filters)
    new_img = img2[(n-1):(n+img.shape[0]-1),(n-1):(n+img.shape[1]-1)]
    return new_img

def matrix_filter(arr, filters):
    n = len(filters)
    ans = 0
    for i in range(n):
    	for j in range(n):
    		ans += arr[i,j]*float(filters[i,j])
    return ans

def high_boost(img, filters, k):
    return img + k*(img-filter2d(img, filter3mul3))

if __name__ == '__main__':
    img = cv2.imread('75.png',0)
    filter3mul3 = np.ones((3,3))
    filter3mul3 *= float(1)/float(3*3)

    filter7mul7 = np.ones((7,7))
    filter7mul7 *= float(1)/float(7*7)

    filter11mul11 = np.ones((11,11))
    filter11mul11 *= float(1)/float(11*11)

    filterlaplac1 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

    img1 = filter2d(img, filter11mul11)
    cv2.imwrite('11mul11.png',img1)
    img2 = filter2d(img, filter7mul7)
    cv2.imwrite('7mul7.png',img2)
    img3 = filter2d(img, filter3mul3)
    cv2.imwrite('3mul3.png',img3)

    img4 = filter2d(img, filterlaplac1)
    cv2.imwrite('filterlaplac.png',img4+img)
    cv2.imwrite('filterlaplac_shap.png',img4)

    k = input('Please enter the coefficient of high boost\n')
    img5 = high_boost(img, filter3mul3, k)
    cv2.imwrite('high_boost.png',img5)
