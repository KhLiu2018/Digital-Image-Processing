#encoding: utf-8
import cv2
import numpy as np
def guidedfilter(I, p, r, eps):
    h, w = I.shape[:2]
    N = boxfilter(np.ones((h, w), dtype=np.float), r)
    mean_I = boxfilter(I, r) / N
    mean_p = boxfilter(p, r) / N
    mean_Ip = boxfilter(I * p, r) / N
    cov_Ip = mean_Ip - mean_I * mean_p

    mean_II = boxfilter(I * I, r) / N
    var_I = mean_II - mean_I * mean_I

    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I

    mean_a = boxfilter(a, r) / N
    mean_b = boxfilter(b, r) / N

    q = mean_a * I + mean_b
    return q * 255.0

def boxfilter(I, r):
    h, w = I.shape[:2]
    I_d = np.zeros((h, w), np.float)
    I_Cum = np.cumsum(I, 0)
    I_d[:r+1, :] = I_Cum[r:2*r+1, :]
    I_d[r+1:h-r, :] = I_Cum[2*r+1:h, :] - I_Cum[:h-2*r-1, :]
    I_d[h-r:h, :] = np.tile(I_Cum[h-1, :], (r,1)) - I_Cum[h-2*r-1:h-r-1, :]
    I_Cum = np.cumsum(I_d, 1)
    I_d[:, :r+1] = I_Cum[:, r:2*r+1]
    I_d[:, r+1:w-r] = I_Cum[:, 2*r+1:w] - I_Cum[:, :w-2*r-1]
    I_d[:, w-r:w] = np.transpose(np.tile(I_Cum[:, w-1], (r,1))) - I_Cum[:, w-2*r-1:w-r-1]
    return I_d

if __name__ == '__main__':
    #smoothing
    '''
    p = cv2.imread('baboon.bmp', 0)/255.0
    I = p
    r = np.array([2, 4, 8])
    eps = np.array([0.01, 0.04, 0.16])
    for i in range(3):
        for j in range(3):
            string = 'baboon%d%d.bmp'%(i,j)
            img = guidedfilter(I,p,r[i],eps[j])
            cv2.imwrite(string, img)
    '''
    #enhancement
    p = cv2.imread('monarch.bmp',3) / 255.0
    I = p
    r = 16
    eps = 0.01
    h, w = I.shape[:2]
    q = np.zeros((h, w, 3))
    q[:, :, 0] = guidedfilter(I[:, :, 0], p[:, :, 0], r, eps)
    q[:, :, 1] = guidedfilter(I[:, :, 1], p[:, :, 1], r, eps)
    q[:, :, 2] = guidedfilter(I[:, :, 2], p[:, :, 2], r, eps)
    I_enhanced = (I * 255.0 - q) * 10 + q
    cv2.imwrite('monarch_en_10.bmp', I_enhanced)
