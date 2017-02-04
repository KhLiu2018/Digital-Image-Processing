import cv2
import numpy as np
import guidedfilter as gf
from scipy.misc import imresize
def fastguidedfilter(I, p, r, eps, s):
    I_sub = imresize(I, 1.0/s, 'nearest')
    p_sub = imresize(p, 1.0/s, 'nearest')
    r_sub = r / s

    h_sub, w_sub = I_sub.shape[:2]
    N = gf.boxfilter(np.ones((h_sub, w_sub),np.float), r)
    mean_I = gf.boxfilter(I_sub, r_sub) / N
    mean_p = gf.boxfilter(I_sub, r_sub) / N
    mean_Ip = gf.boxfilter(I_sub * p_sub, r_sub) / N
    cov_Ip = mean_Ip - mean_I * mean_p

    mean_II = gf.boxfilter(I_sub * I_sub, r_sub) / N
    var_I = mean_II - mean_I * mean_I

    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I

    mean_a = gf.boxfilter(a, r_sub) / N
    mean_b = gf.boxfilter(b, r_sub) / N

    mean_a = imresize(mean_a, I.shape[:2], 'bilinear')
    mean_b = imresize(mean_b, I.shape[:2], 'bilinear')
    q = mean_a * I + mean_b

    return q

if __name__ == '__main__':
    p = cv2.imread('baboon.bmp', 0)/255.0
    I = p
    r = np.array([4, 8])
    eps = np.array([0.01, 0.04, 0.16])
    s = np.array([4.0])
    for i in range(2):
        for j in range(3):
            string = 'baboon%d%d.bmp'%(i,j)
            img = fastguidedfilter(I,p,r[i],eps[j],s[0])
            cv2.imwrite(string, img)
