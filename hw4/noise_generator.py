#encoding:utf-8
import cv2
import numpy as  np
import random
import equalize_hist as eq
import mean_filter as filters

def gaussian(img, mean, standard_var):
    m, n =img.shape[:2]
    new_img = np.zeros((m,n), np.int)
    new_img = img
    for x in range(0,m):
        for y in range(0,n,2):
            r1 = np.random.random_sample()
            r2 = np.random.random_sample()
            z1 = standard_var*np.cos(2*np.pi*r2)*np.sqrt((-2)*np.log(r1))+mean
            z2 = standard_var*np.sin(2*np.pi*r2)*np.sqrt((-2)*np.log(r2))+mean
            fxy = int(img[x,y] + z1)
            fxy1 = int(img[x,y+1] + z2)
            if fxy < 0:
                fxy_val = 0
            elif fxy > 255:
                fxy_val = 255
            else:
                fxy_val = fxy
            if fxy1 < 0:
                fxy1_val = 0
            elif fxy1 > 255:
                fxy1_val = 255
            else:
                fxy1_val = fxy1
            new_img[x,y] = fxy_val
            new_img[x,y+1] = fxy1_val
    return new_img
def salt_and_pepper(img, p):
    m, n = img.shape[:2]
    noise_num = int(p * m * n * 2)
    new_img = img
    for i in range(noise_num) :
        randX = random.randint(0, m-1)
        randY = random.randint(0, n-1)
        if random.randint(0, 1) == 0:
            new_img[randX, randY] = 0
        else:
            new_img[randX, randY] = 255
    return new_img
def salt(img, p):
    m, n = img.shape[:2]
    noise_num = int(p * m * n)
    new_img = img
    for i in range(noise_num) :
        randX = random.randint(0, m-1)
        randY = random.randint(0, n-1)
        new_img[randX, randY] = 255
    return new_img
if __name__ == '__main__':
    img = cv2.imread('task_2.png', 0)
    #salt_img = salt(img, 0.2)
    #python random里的seed好像有坑，如果是生成两个图片之后再依次保存，
    #盐噪声的图像就会发生改变。random.seed()设定种子
    '''
    cv2.imwrite('s_salt_img.png', salt_img)
    s_and_p_img = salt_and_pepper(img, 0.2)
    cv2.imwrite('task_2_of_s_and_p.png', s_and_p_img)
    '''
    pic = gaussian(img, 0, 40)
    cv2.imwrite('gauss_pic_3.png', pic)
    cv2.imwrite('gauss_ari.png', filters.various_filter(pic, 3, 'ari'))
    cv2.imwrite('gauss_geo.png', filters.various_filter(pic, 3, 'geo'))
    cv2.imwrite('gauss_med.png', filters.various_filter(pic, 3, 'med'))
    '''
    pic_1 = cv2.imread('gauss_pic.png',0)
    cv2.imwrite('hist.png', eq.calcAndDrawHist(pic_1))
    pic_2 = cv2.imread('gauss_pic_1.png',0)
    cv2.imwrite('hist2.png', eq.calcAndDrawHist(pic_2))
    '''

    '''
    salt = cv2.imread('s_salt_img.png',0)
    # 对添加了盐噪声的图像做谐波滤波：
    salt_ha = filters.various_filter(salt, 3, 'ha')
    cv2.imwrite('salt_ha.png', salt_ha)
    # 对添加了盐噪声的图像做q=1.5的逆谐波滤波
    salt_con_q2 = filters.various_filter(salt, 3, 'con')
    cv2.imwrite('salt_con_q2.png', salt_con_q2)
    salt_min = filters.various_filter(salt, 3, 'min')
    cv2.imwrite('salt_min.png', salt_min)
    '''
    '''
    s_p = cv2.imread('task_2_of_s_and_p.png',0)
    s_p_ari = filters.various_filter(s_p, 3, 'ari')
    cv2.imwrite('s_p_ari.png', s_p_ari)
    s_p_geo = filters.various_filter(s_p, 3, 'geo')
    cv2.imwrite('s_p_geo.png', s_p_geo)
    s_p_ha = filters.various_filter(s_p, 3, 'ha')
    cv2.imwrite('s_p_ha.png', s_p_ha)
    s_p_med = filters.various_filter(s_p, 3, 'med')
    cv2.imwrite('s_p_med.png', s_p_med)
    '''
